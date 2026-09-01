#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Setzt die Claude-Code-Befehlsreferenz als HTML (danach -> PDF).

Baut BEIDE Sprachfassungen in einem Lauf — deutsch und englisch. Das ist
Absicht: eine einzelne Fassung kann so nicht vergessen werden und auch nicht
mit einer anderen Programmversion auseinanderlaufen.

    python3 build_ref.py            beide Sprachen
    python3 build_ref.py de         nur deutsch (zum schnellen Nachsehen)
    python3 build_ref.py --force    trotz fehlender Übersetzungen bauen
"""
import json, pathlib, datetime, sys
import texte_de, texte_en, aenderungen

VERSION = "2.1.252"
VORGAENGER = "2.1.251"
VORGAENGER_DATUM = datetime.date(2026, 8, 29)   # Erscheinungstag der Vorfassung
HERE = pathlib.Path(__file__).parent

# Sprachkennung -> (Textmodul, Änderungskasten, Dateiname ohne Endung)
SPRACHEN = {
    "de": (texte_de, aenderungen.DE, "Claude-Code-Befehlsreferenz"),
    "en": (texte_en, aenderungen.EN, "Claude-Code-Command-Reference"),
}

opts = json.loads((HERE / "opts.json").read_text())
subs = json.loads((HERE / "subs.json").read_text())
slash = json.loads((HERE / f"slash-{VERSION}.json").read_text())

# ---------------------------------------------------------------- Abgleich --
# Die deutschen Optionsschlüssel tragen eingedeutschte Platzhalter
# (<verzeichnisse...> statt <directories...>); englisch bleibt das Original.
def norm_opt(f, sprache):
    if sprache != "de":
        return f
    return (f.replace("<directories...>", "<verzeichnisse...>")
             .replace("<tools...>", "<werkzeuge...>")
             .replace("<prompt>", "<text>").replace("<level>", "<stufe>")
             .replace("<environment_id>", "<id>").replace("<model>", "<modell>")
             .replace("<path>", "<pfad>").replace("<configs...>", "<dateien...>")
             .replace("<format>", "<format>").replace("<mode>", "<modus>")
             .replace("<amount>", "<betrag>").replace("<specs...>", "<angaben...>")
             .replace("<value>", "<wert>").replace("<file-or-json>", "<datei-oder-json>")
             .replace("<sources>", "<quellen>").replace("<session>", "<sitzung>")
             .replace("<filter>", "<filter>").replace("<schema>", "<schema>")
             .replace("<betas...>", "<betas...>").replace("<prefix>", "<prefix>")
             .replace("<name>", "<name>").replace("<uuid>", "<uuid>")
             .replace("<agent>", "<agent>").replace("<json>", "<json>")
             .replace("<url>", "<url>").replace("[description|session_id|url]", "[beschreibung|id|url]")
             .replace("[value]", "[wert]").replace("[session]", "[sitzung]"))

fehlt = []
for sprache, (T, _, _) in SPRACHEN.items():
    for f, _d in opts:
        if norm_opt(f, sprache) not in T.OPTIONEN:
            fehlt.append(f"[{sprache}] OPTION " + f)
    for b in slash:
        if b["name"] not in T.SLASH:
            fehlt.append(f"[{sprache}] SLASH /" + b["name"])
if fehlt:
    print("FEHLENDE ÜBERSETZUNGEN:")
    for f in fehlt:
        print("   ", f)
    if "--force" not in sys.argv:
        sys.exit(1)

# ------------------------------------------------------------------ Bloecke --
def zeile(links, rechts, klasse=""):
    return (f'<div class="z {klasse}"><div class="l"><code>{links}</code></div>'
            f'<div class="r">{rechts}</div></div>')

def abschnitt(titel, inhalt, unter=""):
    u = f'<p class="unter">{unter}</p>' if unter else ""
    return f'<section><h2>{titel}</h2>{u}{inhalt}</section>'

def datum(d, S, form="datum_kurz"):
    """Datum in der Schreibweise der jeweiligen Sprache.

    Monatsnamen kommen aus dem Textmodul, nicht aus strftime: sonst haenge die
    Ausgabe daran, welches Locale gerade gesetzt ist - im cron ein anderes als
    in der Sitzung.
    """
    return S[form].format(t=d.day, m=d.month, j=d.year, mn=S["monate"][d.month - 1])

def baue(sprache):
    T, aend, dateiname = SPRACHEN[sprache]
    S = T.SEITE

    # Teil A
    start = "".join(zeile(l, r) for l, r in S["start_zeilen"])
    opt_html = "".join(zeile(norm_opt(f, sprache).replace("<", "&lt;").replace(">", "&gt;"),
                             T.OPTIONEN[norm_opt(f, sprache)]) for f, _ in opts)

    # Teil B
    sub_html = ""
    for gruppe, eintraege in subs.items():
        if gruppe not in T.UNTERBEFEHLE:
            continue
        sub_html += zeile(f"claude {gruppe}", T.UNTERBEFEHLE[gruppe], "kopf")
        for name, _ in eintraege:
            n = name.split(" ")[0]
            if n.endswith(":"):
                continue
            schluessel = f"{gruppe} {n}"
            if schluessel in T.UNTERBEFEHLE:
                sub_html += zeile(f"claude {gruppe} {n}", T.UNTERBEFEHLE[schluessel], "kind")

    # Teil C
    def slash_zeile(b):
        zusatz = []
        if b["aliases"]:
            zusatz.append(S["alias"] + ", ".join("/" + a for a in b["aliases"]))
        if b["hint"]:
            zusatz.append(b["hint"].replace("<", "&lt;").replace(">", "&gt;"))
        z = f' <span class="zus">{" · ".join(zusatz)}</span>' if zusatz else ""
        txt = T.SLASH[b["name"]]
        if not b["verfuegbar"]:
            txt += f' <span class="aus">{S["abgeschaltet"]}</span>'
        return zeile("/" + b["name"] + z, txt)

    verf = [b for b in slash if b["verfuegbar"]]
    aus = [b for b in slash if not b["verfuegbar"]]
    slash_html = "".join(slash_zeile(b) for b in sorted(verf, key=lambda b: b["name"]))
    aus_html = "".join(slash_zeile(b) for b in sorted(aus, key=lambda b: b["name"]))

    heute = datum(datetime.date.today(), S)
    werte = dict(v=VERSION, vorg=VORGAENGER, datum=heute,
                 vorg_datum=datum(VORGAENGER_DATUM, S, "datum_lang"), n_slash=len(slash))

    HTML = f"""<!doctype html>
<html lang="{S['lang']}"><head><meta charset="utf-8"><title>{S['titel'].format(**werte)}</title>
<style>
@page {{ size: A4 portrait; margin: 17mm 15mm 15mm; }}
* {{ box-sizing: border-box; }}
body {{ font-family: 'Liberation Sans', 'Nimbus Sans', sans-serif; font-size: 9.6pt;
  line-height: 1.42; color: #1a1a1a; margin: 0; }}
code {{ font-family: 'DejaVu Sans Mono', monospace; font-size: 8.9pt; }}
h1 {{ font-size: 22pt; margin: 0 0 2mm; letter-spacing: -.3px; }}
h2 {{ font-size: 12.5pt; margin: 7mm 0 2mm; padding-bottom: 1.2mm;
  border-bottom: 1.6px solid #1a1a1a; break-after: avoid; }}
h3 {{ font-size: 10.2pt; margin: 4mm 0 1.5mm; color: #444; break-after: avoid; }}
section {{ break-inside: auto; }}
.kopfzeile {{ font-size: 8pt; letter-spacing: 1.6px; text-transform: uppercase;
  color: #666; margin-bottom: 3mm; }}
.lead {{ font-size: 10.4pt; color: #333; margin: 0 0 4mm; max-width: 155mm; }}
.meta {{ font-size: 8.4pt; color: #777; margin-bottom: 6mm; }}
.kasten {{ border: 1.4px solid #bbb; background: #fafafa; padding: 3.5mm 4mm;
  margin: 0 0 5mm; break-inside: avoid; }}
.kasten h3 {{ margin-top: 0; }}
.kasten p, .kasten li {{ font-size: 9.2pt; margin: 0 0 1.6mm; }}
.kasten ul {{ margin: 0 0 0 4mm; padding: 0; }}
.unter {{ font-size: 9pt; color: #555; margin: 0 0 2.5mm; }}
.z {{ display: flex; gap: 4mm; padding: 1.05mm 0; border-bottom: .5px solid #e8e8e8;
  break-inside: avoid; }}
.z .l {{ flex: 0 0 62mm; }}
.z .r {{ flex: 1; }}
.z.kopf {{ background: #f2f2f2; padding: 1.4mm 1.5mm; margin-top: 2mm;
  border-bottom: 1px solid #ccc; }}
.z.kopf code {{ font-weight: bold; }}
.z.kind .l {{ padding-left: 4mm; }}
.zus {{ color: #777; font-size: 8.2pt; font-family: 'Liberation Sans', sans-serif; }}
.aus {{ color: #a03; font-size: 8.4pt; }}
.fuss {{ margin-top: 6mm; font-size: 8.4pt; color: #777; border-top: .5px solid #ccc;
  padding-top: 2mm; }}
</style></head><body>

<div class="kopfzeile">{S['kopfzeile'].format(**werte)}</div>
<h1>{S['h1']}</h1>
<p class="lead">{S['lead']}</p>
<p class="meta">{S['meta'].format(**werte)}</p>

<div class="kasten">
<h3>{S['kasten1_titel']}</h3>
{S['kasten1'].format(**werte)}
</div>

<div class="kasten">
<h3>{S['kasten2_titel']}</h3>
{aend.format(**werte)}
</div>

{abschnitt(S['teilA_titel'],
           f'<h3>{S["teilA_h3_start"]}</h3>' + start + f'<h3>{S["teilA_h3_opt"]}</h3>' + opt_html,
           S['teilA_unter'])}

{abschnitt(S['teilB_titel'], sub_html, S['teilB_unter'])}

{abschnitt(S['teilC_titel'], slash_html, S['teilC_unter'].format(n=len(verf)))}

{abschnitt(S['anhang_titel'], aus_html, S['anhang_unter'])}

<div class="fuss">{S['fuss'].format(opt=len(opts), verf=len(verf), aus=len(aus), **werte)}</div>
</body></html>"""

    ziel = HERE / f"{dateiname}-{VERSION}.html"
    ziel.write_text(HTML, encoding="utf-8")
    return ziel, len(verf), len(aus)


gewuenscht = [a for a in sys.argv[1:] if a in SPRACHEN] or list(SPRACHEN)
namen = []
for sprache in gewuenscht:
    ziel, n_verf, n_aus = baue(sprache)
    namen.append(ziel.name)

# Die Zusammenfassungszeile liest anleitungen-veroeffentlichen.sh aus (Anzahl
# Optionen/Slash-Befehle/abgeschaltet) - Wortlaut bitte nicht ändern.
print(f"geschrieben: {', '.join(namen)} · {len(opts)} Optionen · {n_verf} Slash-Befehle "
      f"· {n_aus} abgeschaltet")
