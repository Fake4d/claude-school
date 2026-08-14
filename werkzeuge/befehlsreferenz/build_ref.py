#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Setzt die Claude-Code-Befehlsreferenz als HTML (danach -> PDF)."""
import json, pathlib, datetime, re, sys
import texte_de as T

VERSION = "2.1.232"
VORGAENGER = "2.1.229"
HERE = pathlib.Path(__file__).parent

opts = json.loads((HERE / "opts.json").read_text())
subs = json.loads((HERE / "subs.json").read_text())
slash = json.loads((HERE / f"slash-{VERSION}.json").read_text())

# ---------------------------------------------------------------- Abgleich --
def norm_opt(f):
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
for f, _ in opts:
    if norm_opt(f) not in T.OPTIONEN:
        fehlt.append("OPTION " + f)
for b in slash:
    if b["name"] not in T.SLASH:
        fehlt.append("SLASH /" + b["name"])
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

# Teil A
start = "".join([
    zeile("claude", "Startet eine Sitzung im aktuellen Ordner."),
    zeile("claude &quot;deine Frage&quot;", "Startet mit einer ersten Nachricht."),
    zeile("claude -p &quot;…&quot;", "Antwortet einmal und beendet sich — für Skripte."),
])
opt_html = "".join(zeile(norm_opt(f).replace("<", "&lt;").replace(">", "&gt;"),
                         T.OPTIONEN[norm_opt(f)]) for f, _ in opts)

# Teil B
sub_html = ""
for gruppe, eintraege in subs.items():
    if gruppe not in T.UNTERBEFEHLE:
        continue
    kopf = zeile(f"claude {gruppe}", T.UNTERBEFEHLE[gruppe], "kopf")
    kinder = ""
    for name, _ in eintraege:
        n = name.split(" ")[0]
        if n.endswith(":"):
            continue
        schluessel = f"{gruppe} {n}"
        if schluessel in T.UNTERBEFEHLE:
            kinder += zeile(f"claude {gruppe} {n}", T.UNTERBEFEHLE[schluessel], "kind")
    sub_html += kopf + kinder

# Teil C
def slash_zeile(b):
    name = "/" + b["name"]
    zusatz = []
    if b["aliases"]:
        zusatz.append("auch " + ", ".join("/" + a for a in b["aliases"]))
    if b["hint"]:
        zusatz.append(b["hint"].replace("<", "&lt;").replace(">", "&gt;"))
    z = f' <span class="zus">{" · ".join(zusatz)}</span>' if zusatz else ""
    txt = T.SLASH[b["name"]]
    if not b["verfuegbar"]:
        txt += ' <span class="aus">im Programm angelegt, aber abgeschaltet</span>'
    return zeile(name + z, txt)

verf = [b for b in slash if b["verfuegbar"]]
aus = [b for b in slash if not b["verfuegbar"]]
slash_html = "".join(slash_zeile(b) for b in sorted(verf, key=lambda b: b["name"]))
aus_html = "".join(slash_zeile(b) for b in sorted(aus, key=lambda b: b["name"]))

heute = datetime.date.today().strftime("%d.%m.%Y").lstrip("0")

HTML = f"""<!doctype html>
<html lang="de"><head><meta charset="utf-8"><title>Claude Code · Befehlsreferenz {VERSION}</title>
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

<div class="kopfzeile">Vollständige Referenz · geprüft gegen Version {VERSION}</div>
<h1>Claude Code<br>Befehlsreferenz</h1>
<p class="lead">Alle Terminal-Befehle, alle Optionen und alle Slash-Befehle innerhalb einer
Sitzung — mit einer Erklärung, was sie tun.</p>
<p class="meta">Zusammengestellt von Christians virtuellem Server · {heute} ·
Aktualisierung der Fassung vom 5. August 2026 ({VORGAENGER})</p>

<div class="kasten">
<h3>Wie diese Liste entstanden ist</h3>
<p>Terminal-Befehle und Optionen (Teil A und B) sind direkt aus der installierten Fassung
{VERSION} ausgelesen — <code>claude --help</code> und die Hilfe jedes Unterbefehls.</p>
<p>Die Slash-Befehle (Teil C) stammen aus den Befehlsdefinitionen im Programm selbst. Das
Ausleseverfahren erkennt auch Befehle, deren Beschreibung erst zur Laufzeit gebildet oder
aus einer Variablen geholt wird, und seit dieser Fassung ebenso solche, deren <i>Name</i>
in einer Variablen steht statt als Text im Programm. Beides kommt durch das Verdichten
des Programmcodes beim Bauen zustande und sagt nichts über den Befehl selbst aus.</p>
<p>Befehle, die im Programm angelegt, aber per Schalter abgeschaltet sind, stehen
gesondert am Ende, damit nichts als verfügbar erscheint, was es nicht ist.</p>
</div>

<div class="kasten">
<h3>Was sich seit der letzten Fassung geändert hat</h3>
<p><code>claude --help</code> und die Hilfetexte aller Unterbefehle sind Zeichen für
Zeichen identisch zu {VORGAENGER}; kein Terminal-Befehl, keine Option ist dazugekommen
oder weggefallen (Teil A und B).</p>
<p>Bei den Slash-Befehlen (Teil C) sind gegenüber {VORGAENGER} genau zwei dazugekommen:
<code>/artifact-components</code> und <code>/claude-api</code>. <b>Weggefallen ist
keiner</b>, und an den übrigen hat sich inhaltlich nichts geändert — gleiche
Beschreibungen, gleiche Zweitnamen, gleiche Argumenthinweise.</p>
<p><b>Trotzdem ist die Liste deutlich länger geworden, von 114 auf {len(slash)}
Einträge.</b> Das liegt nicht an neuen Befehlen, sondern am verbesserten Ausleseverfahren:
13 Befehle standen schon vorher zur Verfügung, wurden aber übersehen, weil ihr Name im
Programm nicht als Text, sondern in einer Variablen abgelegt ist. Darunter
<code>/dataviz</code>, <code>/workshop</code>, <code>/whiteboard</code>,
<code>/prototype</code>, <code>/verify</code>, <code>/simplify</code> und
<code>/commit</code>. Sie sind also nicht neu — sie fehlten vorher zu Unrecht.</p>
<p class="unter" style="margin-top:2mm">Anlass für die Verbesserung war ein Fehlalarm:
Beim ersten Abgleich sah es so aus, als sei <code>/loop</code> entfallen. Tatsächlich war
nur dessen Name in eine Variable gewandert; den Befehl gibt es unverändert. Das Verfahren
prüft solche Fälle jetzt mit — und ein scheinbarer Wegfall führt nicht mehr
ungeprüft in diese Liste.</p>
</div>

{abschnitt("Teil A · Terminal-Befehle und Optionen",
           '<h3>Sitzung starten</h3>' + start + '<h3>Optionen</h3>' + opt_html,
           "Aufrufform: <code>claude [optionen] [befehl] [eingabe]</code>. "
           "Ohne Angaben startet eine Sitzung im aktuellen Ordner.")}

{abschnitt("Teil B · Unterbefehle", sub_html,
           "Aufrufe der Form <code>claude &lt;unterbefehl&gt;</code>. "
           "Eingerückt die jeweils zugehörigen Unter-Unterbefehle.")}

{abschnitt("Teil C · Slash-Befehle in der Sitzung", slash_html,
           f"{len(verf)} verfügbare Befehle, alphabetisch. Grau dahinter: Zweitnamen "
           "und erwartete Argumente.")}

{abschnitt("Anhang · Angelegt, aber abgeschaltet", aus_html,
           "Diese Namen existieren im Programm, sind in dieser Fassung aber per Schalter "
           "deaktiviert und stehen in einer Sitzung nicht zur Verfügung.")}

<div class="fuss">Claude Code {VERSION} · {len(opts)} Optionen · {len(verf)} verfügbare
Slash-Befehle · {len(aus)} abgeschaltet · Stand {heute}</div>
</body></html>"""

ziel = HERE / f"Claude-Code-Befehlsreferenz-{VERSION}.html"
ziel.write_text(HTML, encoding="utf-8")
print(f"geschrieben: {ziel.name} · {len(opts)} Optionen · {len(verf)} Slash-Befehle "
      f"· {len(aus)} abgeschaltet")
