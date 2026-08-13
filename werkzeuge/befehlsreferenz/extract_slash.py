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
import re, json, pathlib, sys

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


def variable_aufloesen(bezeichner):
    """`description:CQE` -> den Text hinter `CQE=\'...\'` im Programm suchen."""
    if bezeichner in VARCACHE:
        return VARCACHE[bezeichner]
    m = re.search(r'(?:var\s+)?' + re.escape(bezeichner) +
                  r'\s*=\s*(["\'])((?:[^\\]|\\.)*?)\1', data)
    text = ""
    if m:
        try:
            text = m.group(2).encode().decode("unicode_escape")
        except Exception:
            text = m.group(2)
    VARCACHE[bezeichner] = text.strip()
    return VARCACHE[bezeichner]


def entschluesseln(s):
    try:
        return s.encode().decode("unicode_escape")
    except Exception:
        return s


befehle = {}
# Anker sind die Beschreibungen. Ein Objekt gilt als Slash-Befehl, wenn es auf
# oberster Ebene einen kleingeschriebenen `name` und eine Beschreibung hat und
# zusaetzlich mindestens ein befehlstypisches Feld (type / isEnabled / aliases /
# requires). `inputSchema` schliesst Werkzeuge und Agenten aus. Diese Regel ist
# unabhaengig von den Minifier-Namen und damit ueber Versionen hinweg vergleichbar.
ANKER = re.compile(r'description:(?:"|[A-Za-z_$][\w$]{0,6}[,}])|get description\(\)\s*\{')
for t in ANKER.finditer(data):
    obj = klammer_bereich(data, t.start())
    if obj is None or "inputSchema" in obj[:400]:
        continue
    nm = feld_oberste_ebene(obj, r'name:"([a-z0-9][a-z0-9:_-]{2,30})"')
    if not nm:
        continue
    typ = feld_oberste_ebene(obj, r'type:"(local|local-jsx|prompt)"')
    hat_merkmal = typ or feld_oberste_ebene(obj, r'(isEnabled|aliases|requires|userInvocable|getPromptForCommand)[:(]') \
        or None
    if not hat_merkmal:
        continue
    name = nm.group(1)

    ds = feld_oberste_ebene(obj, r'description:"((?:[^"\\]|\\.)*)"')
    if ds:
        desc, variabel = entschluesseln(ds.group(1)).strip(), False
    else:
        tx = getter_texte(obj)
        desc, variabel = (tx[-1] if tx else ""), len(tx) > 1
        if not desc:
            # description verweist auf eine Variable (so liegen die Skill-Texte vor)
            vr = feld_oberste_ebene(obj, r'description:([A-Za-z_$][\w$]{0,6})')
            if vr:
                desc = variable_aufloesen(vr.group(1))
    if not desc:
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
    alt = befehle.get(name)
    if alt is None or (not alt["desc"] and desc):
        befehle[name] = eintrag

out = sorted(befehle.values(), key=lambda b: b["name"])
pathlib.Path(f"slash-{VERSION}.json").write_text(
    json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")

aus = [b for b in out if not b["verfuegbar"]]
ohne = [b for b in out if not b["desc"]]
print(f"{len(out)} Slash-Befehle · {len(aus)} abgeschaltet · {len(ohne)} ohne Text"
      f"  ->  slash-{VERSION}.json")
if len(sys.argv) > 2:
    for b in out:
        mark = "  << ABGESCHALTET" if not b["verfuegbar"] else ""
        al = f"  (auch: {', '.join(b['aliases'])})" if b["aliases"] else ""
        print(f"  /{b['name']:<20} {b['desc'][:58]}{al}{mark}")
