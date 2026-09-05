#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Liest die Slash-Befehls-Definitionen aus der installierten Claude-Code-Binaerdatei.

Vorgehen: Jede Stelle `type:"local"|"local-jsx"|"prompt"` ist der Anker einer
Befehlsdefinition. Von dort werden die Grenzen des umschliessenden Objektliterals
per Klammerzaehlung bestimmt; Name und Beschreibung werden nur auf der obersten
Ebene *dieses* Objekts gelesen. Das verhindert, dass Angaben aus Nachbarobjekten
in einen Eintrag wandern (minifizierter Code liegt dicht an dicht).

Die Beschreibung steht entweder als fester Text (`description:"..."`) oder als
Getter (`get description(){...}`), der je nach Umgebung verschiedene Texte
zurueckgibt — dann werden alle Textbausteine gesammelt.

Aufruf:  python3 extract_slash.py [version]
"""
import re, json, pathlib, sys, bisect

VERSION = sys.argv[1] if len(sys.argv) > 1 else "2.1.228"
BIN = pathlib.Path.home() / f".local/share/claude/versions/{VERSION}"
data = BIN.read_bytes().decode("utf-8", "replace")

TYPE = re.compile(r'type:"(local|local-jsx|prompt)"')
AUS = re.compile(r'^\s*(!1|false)\s*$')
MAX_OBJ = 4000


def klammer_bereich(text, pos):
    """Grenzen des Objektliterals, das die Stelle `pos` enthaelt."""
    tiefe, i = 0, pos - 1
    start = None
    while i >= 0 and pos - i < MAX_OBJ:
        c = text[i]
        if c == '}':
            tiefe += 1
        elif c == '{':
            if tiefe == 0:
                start = i
                break
            tiefe -= 1
        i -= 1
    if start is None:
        return None
    tiefe, j = 0, start + 1
    while j < len(text) and j - start < MAX_OBJ:
        c = text[j]
        if c == '{':
            tiefe += 1
        elif c == '}':
            if tiefe == 0:
                return text[start:j + 1]
            tiefe -= 1
        j += 1
    return None


def feld_oberste_ebene(obj, muster):
    """Sucht `muster` nur auf der obersten Ebene des Objekts (Tiefe 0).

    Die oeffnende Klammer von `obj` selbst wird uebersprungen, sonst laege der
    gesamte Inhalt auf Tiefe 1 und nichts wuerde gefunden.
    """
    tiefe = 0
    for m in re.finditer(r'[{}]|' + muster, obj[1:]):
        s = m.group(0)
        if s == '{':
            tiefe += 1
        elif s == '}':
            tiefe -= 1
        elif tiefe == 0 and m.lastindex:
            return m
    return None


def getter_texte(obj):
    """Textbausteine aus `get description(){ ... }` sammeln."""
    g = re.search(r'get description\(\)\s*\{', obj)
    if not g:
        return []
    tiefe, j = 1, g.end()
    while j < len(obj) and tiefe:
        if obj[j] == '{':
            tiefe += 1
        elif obj[j] == '}':
            tiefe -= 1
        j += 1
    koerper = obj[g.end():j - 1]
    texte = re.findall(r'"((?:[^"\\]|\\.)*)"|`([^`]{0,200})`', koerper)
    raus = []
    for a, b in texte:
        t = (a or b).strip()
        if len(t) > 12 and not t.startswith(("tengu_", "http")):
            try:
                t = t.encode().decode("unicode_escape")
            except Exception:
                pass
            raus.append(re.sub(r'\$\{[^}]*\}', '…', t).strip())
    return raus


VARCACHE = {}


def _text_suchen(bezeichner, feld):
    m = re.search(r'(?:var\s+|[,;{}\s])' + re.escape(bezeichner) +
                  r'\s*=\s*(["\'])((?:[^\\]|\\.)*?)\1', feld)
    if not m:
        # Manche Beschreibungen liegen als Array mehrerer Textbausteine vor
        # (Kurzbeschreibung + Trigger-/Skip-Hinweise). Dann zaehlt nur der
        # erste String im Array als Kurzbeschreibung.
        m = re.search(r'(?:var\s+|[,;{}\s])' + re.escape(bezeichner) +
                      r'\s*=\s*\[\s*(["\'])((?:[^\\]|\\.)*?)\1', feld)
    if not m:
        return ""
    try:
        return m.group(2).encode().decode("unicode_escape").strip()
    except Exception:
        return m.group(2).strip()


def variable_aufloesen(bezeichner, vor_position):
    """`description:kd` -> den Text hinter `kd='...'` suchen.

    Wie bei den Namen gilt seit 2.1.243: erst im eigenen Modul suchen, sonst
    greift man bei einbuchstabigen Bezeichnern einen fremden Text ab. Steht der
    Bezeichner nicht im Modul, ist er importiert - dann im Herkunftsmodul.
    """
    i = modul_von(vor_position)
    if i is None:
        return ""
    schluessel = (bezeichner, i)
    if schluessel in VARCACHE:
        return VARCACHE[schluessel]
    start, ende = modul_bereich(i)
    text = _text_suchen(bezeichner, data[start:ende])
    if not text:
        herkunft = IMPORTE[i].get(bezeichner)
        if herkunft:
            chunk, export = herkunft
            j, lokal = herkunft_modul(chunk, export)
            if j is not None and lokal:
                qstart, qende = modul_bereich(j)
                text = _text_suchen(lokal, data[qstart:qende])
    VARCACHE[schluessel] = text
    return text


# Kurze Zuweisungen `VAR="wert"` einmalig einsammeln, MIT Position. Einzeln zu
# suchen waere unbezahlbar: die Datei hat ~300 Mio Zeichen und es gibt hunderte
# Bezeichner. Derselbe kurze Bezeichner (z.B. `$ne`) wird im minifizierten Bundle
# aber fuer VIELE unabhaengige Variablen in verschiedenen Modulen wiederverwendet -
# ein globales "letzter Treffer gewinnt" greift dann leicht daneben (so verschwand
# /artifact-capabilities am 23.08.2026 aus der Liste: seine echte Zuweisung
# `$ne="artifact-capabilities"` lag 18 Mio Zeichen VOR der Objektstelle, eine
# voellig fremde `$ne="trigger-hover"` aus einer UI-Bibliothek aber 14 Mio Zeichen
# DANACH - und gewann als letzter Fund im Dict. Deshalb je Bezeichner eine nach
# Position sortierte Liste vorhalten und bei Bedarf die naechste vorangehende
# Zuweisung vor der Objektstelle waehlen - Variablen sind an dieser Stelle im
# Bundle immer schon zugewiesen, eine nachfolgende ist zwangslaeufig ein anderer
# Gueltigkeitsbereich.
NAMEN_POS = {}
for m in re.finditer(r'([A-Za-z_$][\w$]{0,8})\s*=\s*["\']([a-z0-9][a-z0-9:_-]{2,30})["\']', data):
    NAMEN_POS.setdefault(m.group(1), []).append((m.start(), m.group(2)))


# ------------------------------------------------------------ Module --------
# Seit 2.1.243 ist das Bundle nicht mehr ein durchgehender Block, sondern in
# Module ("chunks") zerlegt, die sich gegenseitig importieren:
#
#   import{Ofb as Qe}from"/$bunfs/root/chunk-vtt3ymv6.js";  ...  {name:Qe,...}
#
# `Qe` ist damit KEINE Zuweisung mehr, sondern ein Import-Alias - die Suche nach
# `Qe="..."` geht ins Leere. Genau daran fielen am 25.08.2026 vierzehn Befehle
# aus der Liste (alle gebuendelten Skills: /dataviz, /loop, /simplify, ...) und
# sahen im Versionsvergleich aus wie geloescht.
#
# Zusaetzlich sind die modulinternen Bezeichner auf EINEN Buchstaben geschrumpft
# (`k="dataviz"`). Ein Bezeichner wie `b` kommt im Bundle zehntausendfach vor,
# eine bundleweite Suche nach der naechsten vorangehenden Zuweisung trifft also
# fast immer daneben. Beides loest derselbe Schritt: erst das Modul bestimmen,
# dann nur noch INNERHALB des Moduls suchen - und wenn der Bezeichner dort
# importiert wird, dem Import ins Herkunftsmodul folgen.
# 2.1.246 benennt Module zusaetzlich als `_668.js` statt `chunk-vtt3ymv6.js`.
# Beide Formen muessen erkannt werden, sonst landet `modul_von()` im falschen
# Modul und Namen/Beschreibungen lassen sich nicht mehr aufloesen - die Befehle
# sehen dann im Versionsvergleich aus wie geloescht.
CHUNKNAME = r'(?:chunk-[a-z0-9]+|_[0-9]+)\.js'
MODULKOPF = re.compile(r'/\$bunfs/root/(' + CHUNKNAME + r')\x00// @bun')
MODUL_START = [(m.start(), m.group(1)) for m in MODULKOPF.finditer(data)]

# 2.1.246 hat das Layout erneut geaendert: der Modulpfad steht nicht mehr
# unmittelbar vor dem Kopf (der Marker heisst dort `\x00// @bun @bytecode`).
# Dafuer endet jedes Modul sichtbar mit seinem Export-Satz
# `export{u as sxd,v as txd,...};`, und die Import-Saetze der anderen Module
# nennen genau diese Aliase. Ein Modul laesst sich also ueber seine Exporte
# identifizieren statt ueber den Pfad - das bleibt gueltig, egal wie die
# Chunk-Dateien beim naechsten Umbau heissen.
LAYOUT = "pfad" if MODUL_START else "export"
if LAYOUT == "export":
    MODUL_START = [(m.start(), None) for m in re.finditer(r'\x00// @bun', data)]
MODUL_POS = [p for p, _ in MODUL_START]


def modul_von(pos):
    """Index des Moduls, in dem `pos` liegt (oder None ausserhalb)."""
    i = bisect.bisect_right(MODUL_POS, pos) - 1
    return i if i >= 0 else None


def modul_bereich(i):
    start = MODUL_POS[i]
    ende = MODUL_POS[i + 1] if i + 1 < len(MODUL_POS) else len(data)
    return start, ende


# Export-Layout: je Modul `Exportalias -> lokaler Bezeichner` aus dem
# abschliessenden `export{...}` lesen, dazu global `Exportalias -> Modulindex`.
EXPORT_LOKAL = [dict() for _ in MODUL_START]
ALIAS_MODUL = {}
if LAYOUT == "export":
    EXPORT_SATZ = re.compile(r'export\{([^}]{1,8000})\};?\s*$')
    for i in range(len(MODUL_START)):
        start = MODUL_POS[i]
        ende = MODUL_POS[i + 1] if i + 1 < len(MODUL_POS) else len(data)
        m = EXPORT_SATZ.search(data[max(start, ende - 9000):ende])
        if not m:
            continue
        for paar in m.group(1).split(","):
            teile = paar.split(" as ")
            if len(teile) == 2:
                lokal, alias = teile[0].strip(), teile[1].strip()
            elif len(teile) == 1:
                lokal = alias = teile[0].strip()
            else:
                continue
            if lokal and alias:
                EXPORT_LOKAL[i][alias] = lokal
                ALIAS_MODUL.setdefault(alias, i)   # erster Fund gewinnt

# Importe je Modul einsammeln: lokaler Alias -> (Herkunftsmodul, Exportname).
IMPORTE = [dict() for _ in MODUL_START]
IMPORT_SATZ = re.compile(r'import\{([^}]{1,4000})\}from"/\$bunfs/root/(' + CHUNKNAME + r')"')
GEFRAGT = {}              # chunkname -> Menge der von aussen genutzten Exportnamen
for m in IMPORT_SATZ.finditer(data):
    i = modul_von(m.start())
    if i is None:
        continue
    quelle = m.group(2)
    for paar in m.group(1).split(","):
        teile = paar.split(" as ")
        if len(teile) == 2:
            export, lokal = teile[0].strip(), teile[1].strip()
        elif len(teile) == 1:
            # Ohne Umbenennung (`import{fut}from"..."`) ist der lokale Name
            # identisch mit dem Exportnamen - seit 2.1.248 kommt das vor und
            # liess z.B. /dataviz (Export "fut") aus der Liste fallen, weil
            # nur `Export as Lokal`-Paare erkannt wurden.
            export = lokal = teile[0].strip()
        else:
            continue
        if export and lokal:
            IMPORTE[i][lokal] = (quelle, export)
            GEFRAGT.setdefault(quelle, set()).add(export)

# Modulname -> Index (ein Chunk kommt genau einmal als Modulkopf vor)
NACH_NAME = {}
for i, (_, nm) in enumerate(MODUL_START):
    NACH_NAME.setdefault(nm, i)

def herkunft_modul(chunk, export):
    """(Modulindex, lokaler Bezeichner) fuer einen Import - fuer beide Layouts."""
    if LAYOUT == "export":
        j = ALIAS_MODUL.get(export)
        return (j, EXPORT_LOKAL[j].get(export)) if j is not None else (None, None)
    j = NACH_NAME.get(chunk)
    return j, export_tabelle(chunk).get(export)


EXPORT_CACHE = {}


def export_tabelle(chunk):
    """Exportname -> lokaler Bezeichner fuer ein Modul.

    Vor jedem Modulkopf steht eine Symboltabelle als reiner ASCII-Lauf, in der
    Export- und lokaler Name unmittelbar hintereinander stehen, ohne Trenner:
    `IfbbJfbSKfbM...` = Ifb->b, Jfb->S, Kfb->M. Weil die Laengen variieren, wird
    an den bekannten Exportnamen verankert (die stehen in den Import-Saetzen der
    anderen Module) und das Stueck bis zum naechsten Exportnamen als lokaler
    Bezeichner gelesen.
    """
    if chunk in EXPORT_CACHE:
        return EXPORT_CACHE[chunk]
    zuordnung = {}
    i = NACH_NAME.get(chunk)
    wanted = GEFRAGT.get(chunk)
    if i is not None and wanted:
        kopf = MODUL_POS[i]
        feld = data[max(0, kopf - 60000):kopf]
        # Unmittelbar vor dem Modulkopf steht die Liste der importierten
        # Chunk-Pfade. Sie wird abgeschnitten; was davor liegt, endet mit der
        # Symboltabelle. (Nicht die ERSTE Pfadstelle im Fenster nehmen - die
        # gehoert noch zu einem frueheren Modul.)
        pfadliste = re.search(r'(?:/\$bunfs/root/' + CHUNKNAME + r')+$', feld)
        if pfadliste:
            feld = feld[:pfadliste.start()]
        funde = []
        for name in wanted:
            p = feld.rfind(name)
            if p >= 0:
                funde.append((p, name))
        funde.sort()
        for k, (p, name) in enumerate(funde):
            ende = funde[k + 1][0] if k + 1 < len(funde) else len(feld)
            lokal = feld[p + len(name):ende]
            if re.fullmatch(r'[A-Za-z_$][\w$]{0,3}', lokal):
                zuordnung[name] = lokal
    EXPORT_CACHE[chunk] = zuordnung
    return zuordnung


def name_aufloesen(bezeichner, vor_position):
    """`name:Qe` -> "dataviz".

    Erst im eigenen Modul nach einer Zuweisung suchen, dann dem Import folgen.
    """
    i = modul_von(vor_position)
    if i is not None:
        start, ende = modul_bereich(i)
        # 1. Zuweisung im selben Modul, die naechste VOR der Fundstelle
        beste = ""
        for pos, wert in NAMEN_POS.get(bezeichner, ()):
            if pos >= vor_position:
                break
            if pos >= start:
                beste = wert
        if beste:
            return beste
        # 2. Import-Alias: ins Herkunftsmodul wechseln
        herkunft = IMPORTE[i].get(bezeichner)
        if herkunft:
            chunk, export = herkunft
            j, lokal = herkunft_modul(chunk, export)
            if j is not None and lokal:
                qstart, qende = modul_bereich(j)
                for pos, wert in NAMEN_POS.get(lokal, ()):
                    if qstart <= pos < qende:
                        return wert
    return ""


def entschluesseln(s):
    try:
        return s.encode().decode("unicode_escape")
    except Exception:
        return s


befehle = {}
# Wird ein Anker gefunden, dessen Name und Merkmale stimmen, aus dem sich aber
# kein Beschreibungstext aufloesen laesst, faellt der Befehl still aus der Liste.
# Genau so ist `/artifact-pr-review` seit mindestens 2.1.235 unbemerkt gefehlt:
# Die Handbremse vergleicht nur zwei Fassungen und sieht deshalb nie, was schon
# vorher verschwunden war. VERWORFEN sammelt diese Faelle, damit sie in der
# Tagesmeldung auftauchen statt lautlos zu verschwinden.
VERWORFEN = []
# Kein Slash-Befehl, sondern ein zufaellig passendes Objekt (`files_with_matches`
# ist ein Grep-Parameter). Bekannte Fehltreffer werden nicht gemeldet, sonst
# gewoehnt man sich an die Meldung und liest sie nicht mehr.
VERWORFEN_FEHLTREFFER = {"files_with_matches"}
# Echte Befehle, deren Bauform der Auslesecode noch nicht beherrscht. Bekannt und
# offen - sie werden gemeldet, aber als Altlast, nicht als Neuigkeit. Wer einen
# davon auslesbar macht, nimmt ihn hier heraus.
VERWORFEN_BEKANNT = {"code-review", "ultrareview", "exit", "claude-code-docs"}
# Anker sind die Beschreibungen. Ein Objekt gilt als Slash-Befehl, wenn es auf
# oberster Ebene einen kleingeschriebenen `name` und eine Beschreibung hat und
# zusaetzlich mindestens ein befehlstypisches Feld (type / isEnabled / aliases /
# requires). `inputSchema` schliesst Werkzeuge und Agenten aus. Diese Regel ist
# unabhaengig von den Minifier-Namen und damit ueber Versionen hinweg vergleichbar.
ANKER = re.compile(r'description:(?:"|\(\)\s*=>|[A-Za-z_$][\w$]{0,6}[,}])'
                   r'|get description\(\)\s*\{')
for t in ANKER.finditer(data):
    obj = klammer_bereich(data, t.start())
    if obj is None or "inputSchema" in obj[:400]:
        continue
    nm = feld_oberste_ebene(obj, r'name:"([a-z0-9][a-z0-9:_-]{2,30})"')
    name_aus_variable = False
    if nm:
        name = nm.group(1)
    else:
        # Seit 2.1.232 steht der Name teilweise in einer Variablen: `name:TEn`
        # statt `name:"loop"`. Ohne diese Aufloesung fielen solche Befehle aus
        # der Liste - und sahen im Versionsvergleich aus wie geloescht.
        nv = feld_oberste_ebene(obj, r'name:([A-Za-z_$][\w$]{0,8})\s*[,}]')
        name = name_aufloesen(nv.group(1), t.start()) if nv else ""
        if not re.fullmatch(r'[a-z0-9][a-z0-9:_-]{2,30}', name):
            continue
        name_aus_variable = True
    typ = feld_oberste_ebene(obj, r'type:"(local|local-jsx|prompt)"')
    hat_merkmal = typ or feld_oberste_ebene(obj, r'(isEnabled|aliases|requires|userInvocable|getPromptForCommand)[:(]') \
        or None
    if not hat_merkmal:
        continue

    ds = feld_oberste_ebene(obj, r'description:"((?:[^"\\]|\\.)*)"')
    if ds:
        desc, variabel = entschluesseln(ds.group(1)).strip(), False
    else:
        pf = feld_oberste_ebene(obj, r'description:\(\)\s*=>\s*"((?:[^"\\]|\\.)*)"')
        if pf:
            desc, variabel = entschluesseln(pf.group(1)).strip(), False
            tx = []
        else:
            tx = getter_texte(obj)
            desc, variabel = (tx[-1] if tx else ""), len(tx) > 1
        if not desc:
            # description verweist auf eine Variable (so liegen die Skill-Texte vor)
            vr = feld_oberste_ebene(obj, r'description:([A-Za-z_$][\w$]{0,6})')
            if vr:
                desc = variable_aufloesen(vr.group(1), t.start())
    if not desc:
        # Seit 2.1.260 kann die Beschreibung eine Pfeilfunktion sein, die je nach
        # Umgebung einen von mehreren Textbausteinen zurueckgibt:
        # `description:()=>ze()==="live"?ds:cs` (so bei /whiteboard, seit die
        # Mehrspieler-Fassung /whiteboard-mp darin aufgegangen ist). Anders als
        # beim schon bekannten `description:()=>"fester Text"` steht hier kein
        # Literal, sondern ein Ausdruck ueber Variablen. Alle darin genannten
        # Bezeichner aufloesen und den laengsten Text nehmen - kurze Treffer sind
        # Funktionsnamen und Vergleichswerte ("live"), keine Beschreibungen.
        af = feld_oberste_ebene(obj, r'description:\(\)\s*=>\s*([^,}]{0,200})')
        if af:
            kand = [variable_aufloesen(b, t.start())
                    for b in re.findall(r'[A-Za-z_$][\w$]{0,6}', af.group(1))]
            kand = [k for k in kand if len(k) > 20]
            if kand:
                desc, variabel = max(kand, key=len), len(set(kand)) > 1
    if not desc:
        VERWORFEN.append(name)
        continue

    h = feld_oberste_ebene(obj, r'argumentHint:"((?:[^"\\]|\\.)*)"')
    a = feld_oberste_ebene(obj, r'aliases:\[([^\]]{0,160})\]')
    e = feld_oberste_ebene(obj, r'isEnabled:\s*\(\)\s*=>\s*([^,}]{0,120})')

    eintrag = {
        "name": name, "typ": typ.group(1) if typ else "registriert",
        "desc": desc, "variabel": variabel,
        "hint": h.group(1) if h else "",
        "aliases": [x.strip() for x in a.group(1).replace('"', '').split(",") if x.strip()] if a else [],
        "enabled": e.group(1).strip() if e else "true",
    }
    eintrag["verfuegbar"] = not AUS.match(eintrag["enabled"])
    # Bei ueber eine Variable aufgeloesten Namen ist die Verwechslungsgefahr groesser:
    # ein beliebiges Objekt kann zufaellig `name` und `description` tragen. Eine
    # Beschreibung, die nur ein einzelnes kurzes Wort ist (z.B. "method"), ist keine -
    # solche Treffer verwerfen. Bei Namen als Literal bleibt es wie bisher.
    if name_aus_variable and " " not in desc and len(desc) < 20:
        continue
    # Manche Namen kommen im Bundle mehrfach vor - etwa `/design` als Hub UND
    # als enger `consent|revoke`-Variante. Welcher Eintrag frueher in der Datei
    # steht, wechselt zwischen Fassungen; ein "der erste gewinnt" liesse die
    # Referenz deshalb grundlos hin- und herspringen. Deterministisch den
    # aussagekraeftigsten Eintrag waehlen: mit Text vor ohne, dann laengerer
    # Argument-Hinweis (ein Hub listet alle Unterbefehle), dann laengerer Text.
    guete = (bool(desc), len(eintrag["hint"]), len(desc))
    alt = befehle.get(name)
    if alt is None or guete > (bool(alt["desc"]), len(alt["hint"]), len(alt["desc"])):
        befehle[name] = eintrag

out = sorted(befehle.values(), key=lambda b: b["name"])
pathlib.Path(f"slash-{VERSION}.json").write_text(
    json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")

aus = [b for b in out if not b["verfuegbar"]]
ohne = [b for b in out if not b["desc"]]
print(f"{len(out)} Slash-Befehle · {len(aus)} abgeschaltet · {len(ohne)} ohne Text"
      f"  ->  slash-{VERSION}.json")

# Nur melden, was es auch wirklich nicht in die Liste geschafft hat: derselbe
# Name kann an einer Fundstelle scheitern und an einer anderen gelingen.
fehlend = {n for n in VERWORFEN if n not in befehle} - VERWORFEN_FEHLTREFFER
neu = sorted(fehlend - VERWORFEN_BEKANNT)
offen = sorted(fehlend & VERWORFEN_BEKANNT)
print(f"VERWORFEN: {len(neu)} neu · {len(offen)} bekannt offen"
      + (f" · NEU: {', '.join('/' + n for n in neu)}" if neu else "")
      + (f" · offen: {', '.join('/' + n for n in offen)}" if offen else ""))
if len(sys.argv) > 2:
    for b in out:
        mark = "  << ABGESCHALTET" if not b["verfuegbar"] else ""
        al = f"  (auch: {', '.join(b['aliases'])})" if b["aliases"] else ""
        print(f"  /{b['name']:<20} {b['desc'][:58]}{al}{mark}")
