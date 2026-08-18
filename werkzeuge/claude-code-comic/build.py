#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die Claude-Code-Comic-Anleitung als HTML (danach -> PDF).

Erzeugt beide Sprachfassungen in einem Lauf: die deutsche direkt, die englische,
indem die fertige Seite durch i18n.uebersetze() mit dem Wörterbuch aus
texte_en.py läuft. Es gibt also nur EIN Bauskript und nur EIN Layout.

    python3 build.py            beide Sprachen
    python3 build.py de         nur deutsch
"""
import base64, pathlib, sys

HERE = pathlib.Path(__file__).parent

def schrift(name):
    """Schriftdatei: neben dem Skript oder im gemeinsamen Ordner ../schriften."""
    for kandidat in (HERE / name, HERE.parent / "schriften" / name):
        if kandidat.exists():
            return kandidat
    raise FileNotFoundError(f"Schrift nicht gefunden: {name}")

def b64(p):
    return base64.b64encode(schrift(p).read_bytes()).decode()

PATRICK = b64("PatrickHand.ttf")
CAVEAT = b64("Caveat.ttf")
CAVEAT_B = b64("CaveatBold.ttf")

# ---------------------------------------------------------------- Figuren ---

HAIR = ('<path d="M55 44 q4-16 18-22 q12-14 30-9 q20-4 28 12 q14 4 12 20 '
        'q-6-7-14-6 q-6-11-20-8 q-14-8-26 2 q-14-2-20 11 q-6 0-8 0z" fill="#141414"/>'
        '<path d="M52 40 q-6 8-2 16 q4-8 10-10z" fill="#141414"/>'
        '<path d="M116 30 q10 2 12 12 q-8-6-14-6z" fill="#141414"/>')

def human(pose="confused", scale=1.0):
    """Der ratlose Mensch."""
    arms = {
        "confused": ('<path d="M63 128 q-22 6 -30 -14 q-6 -16 6 -26" class="ln"/>'
                     '<path d="M117 130 q26 8 34 -2" class="ln"/>'
                     '<path d="M147 122 q10 2 12 8 q-6 3 -12 0" class="ln"/>'),
        "think":    ('<path d="M63 128 q-16 20 4 30 q14 6 22 -6" class="ln"/>'
                     '<path d="M117 130 q22 12 18 34" class="ln"/>'),
        "point":    ('<path d="M117 128 q30 -6 44 -18" class="ln"/>'
                     '<path d="M158 108 q10 -2 14 2 q-4 5 -12 6" class="ln"/>'
                     '<path d="M63 130 q-18 14 -14 34" class="ln"/>'),
        "happy":    ('<path d="M63 130 q-18 16 -12 36" class="ln"/>'
                     '<path d="M117 128 q22 -10 24 -30" class="ln"/>'),
    }[pose]
    mouth = {
        "confused": '<ellipse cx="90" cy="86" rx="7" ry="9" fill="#141414"/>',
        "think":    '<ellipse cx="90" cy="86" rx="6" ry="8" fill="#141414"/>',
        "point":    '<ellipse cx="90" cy="86" rx="8" ry="8" fill="#141414"/>',
        "happy":    '<path d="M78 82 q12 16 24 0" class="ln" stroke-width="4"/>',
    }[pose]
    return f'''<svg class="fig" viewBox="0 0 190 300" style="--s:{scale}">
<defs><pattern id="jeans" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(58)">
<rect width="7" height="7" fill="#2c49a8"/><line x1="0" y1="0" x2="0" y2="7" stroke="#16266b" stroke-width="2.6"/>
</pattern></defs>
<g class="ink">
{HAIR}
<circle cx="90" cy="72" r="34" class="sk"/>
<circle cx="78" cy="64" r="5" fill="#141414"/><circle cx="101" cy="64" r="5" fill="#141414"/>
{mouth}
<path d="M63 128 q-6 46 -2 76 l58 0 q6 -32 -2 -76 q-14 -12 -54 0z" class="sk"/>
{arms}
<path d="M62 200 q-4 44 0 68 l24 0 q2 -34 4 -46 q4 14 5 46 l24 0 q4 -30 0 -68z" fill="url(#jeans)" stroke="#141414" stroke-width="3.4" stroke-linejoin="round"/>
<ellipse cx="72" cy="277" rx="20" ry="10" class="sk"/><ellipse cx="112" cy="277" rx="20" ry="10" class="sk"/>
<g class="hatch"><line x1="44" y1="290" x2="70" y2="290"/><line x1="52" y1="297" x2="80" y2="297"/><line x1="98" y1="291" x2="128" y2="291"/><line x1="106" y1="298" x2="140" y2="298"/></g>
</g></svg>'''

def bean(pose="point", scale=1.0):
    """Die schwarze Claude-Bohne."""
    arms = {
        "point":  ('<path d="M40 150 q-24 -6 -30 8" class="lnb"/><circle cx="8" cy="160" r="7" fill="#141414"/>'
                   '<path d="M140 130 q26 -14 30 -40" class="lnb"/>'
                   '<path d="M166 86 q6 -8 12 -6 q0 8 -6 12z" fill="#141414"/>'),
        "right":  ('<path d="M140 140 q30 -4 44 -20" class="lnb"/><circle cx="186" cy="118" r="7" fill="#141414"/>'
                   '<path d="M40 152 q-22 8 -22 26" class="lnb"/><circle cx="18" cy="180" r="7" fill="#141414"/>'),
        "thumbs": ('<path d="M42 132 q-26 -14 -34 -34" class="lnb"/>'
                   '<path d="M6 100 q-9 2 -9 11 q1 8 9 9 q9 -1 10 -10 q6 -13 -1 -16 q-7 1 -9 9z" fill="#141414"/>'
                   '<path d="M142 152 q22 10 22 28" class="lnb"/><circle cx="164" cy="182" r="7" fill="#141414"/>'),
        "hips":   ('<path d="M40 148 q-26 4 -24 26 q10 6 20 -4" class="lnb"/>'
                   '<path d="M142 148 q26 4 24 26 q-10 6 -20 -4" class="lnb"/>'),
    }[pose]
    return f'''<svg class="fig" viewBox="0 0 200 300" style="--s:{scale}">
<g class="ink">
{arms}
<ellipse cx="92" cy="140" rx="58" ry="76" fill="#141414"/>
<ellipse cx="72" cy="118" rx="11" ry="13" fill="#fff"/><ellipse cx="110" cy="118" rx="11" ry="13" fill="#fff"/>
<path d="M64 158 q28 26 54 -2" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round"/>
<path d="M70 214 q-8 30 -10 46" class="lnb"/><path d="M112 214 q8 30 10 46" class="lnb"/>
<ellipse cx="56" cy="266" rx="17" ry="9" fill="#141414"/><ellipse cx="126" cy="266" rx="17" ry="9" fill="#141414"/>
<g class="hatch"><line x1="30" y1="280" x2="58" y2="280"/><line x1="40" y1="288" x2="72" y2="288"/><line x1="112" y1="281" x2="146" y2="281"/><line x1="120" y1="289" x2="156" y2="289"/></g>
</g></svg>'''

MSCALE = 1.3

def machine(label="Claude", w=300):
    """Die Claude-Maschine (Toaster-Motiv aus dem Original)."""
    return f'''<svg class="machine" viewBox="0 0 300 200" style="width:{w*MSCALE:.0f}px">
<g class="ink">
<path d="M20 60 l40 -30 l224 0 l-40 30 z" class="sk"/>
<path d="M284 30 l0 108 l-40 30 l0 -108 z" class="sk"/>
<rect x="20" y="60" width="224" height="108" rx="8" class="sk"/>
<circle cx="40" cy="80" r="5" fill="none" stroke="#2a7a3a" stroke-width="3"/>
<circle cx="40" cy="98" r="5" fill="none" stroke="#d97b20" stroke-width="3"/>
<circle cx="40" cy="116" r="5" fill="none" stroke="#c8322b" stroke-width="3"/>
<circle cx="106" cy="96" r="6" fill="#141414"/><circle cx="150" cy="96" r="6" fill="#141414"/>
<path d="M100 118 q28 22 56 0" class="ln" stroke-width="4"/>
<text x="128" y="152" text-anchor="middle" class="mlabel">{label}</text>
<rect x="256" y="76" width="14" height="46" rx="4" class="sk" transform="skewY(-37) translate(0,196)"/>
<g class="hatch"><line x1="16" y1="178" x2="60" y2="178"/><line x1="30" y1="186" x2="80" y2="186"/><line x1="200" y1="178" x2="248" y2="178"/><line x1="212" y1="186" x2="266" y2="186"/></g>
</g></svg>'''

# --------------------------------------------------------------- Bausteine ---

def chip(text, color="blue", sub=None, big=False):
    s = f'<span class="chip-sub">{sub}</span>' if sub else ""
    return f'<div class="chip c-{color}{" big" if big else ""}">{text}{s}</div>'

def doc(title, color="blue", lines=3):
    ls = "".join(f'<i style="width:{w}%"></i>' for w in ([88, 70, 80, 60, 74][:lines]))
    return f'<div class="doc c-{color}"><b>{title}</b><div class="lines">{ls}</div></div>'

def row(*items, gap=18):
    return f'<div class="row" style="gap:{gap}px">' + "".join(items) + "</div>"

def col(*items, gap=14):
    return f'<div class="col" style="gap:{gap}px">' + "".join(items) + "</div>"

def breit(links, rechts, *diagramm):
    """Figuren oben, Schaubild darunter ueber die volle Seitenbreite."""
    return ('<div class="scene-col"><div class="figrow">' + links + rechts + '</div>'
            '<div class="wide">' + "".join(diagramm) + '</div></div>')

AR = '<div class="arw">&#8594;</div>'
AD = '<div class="arw">&#8595;</div>'

# ------------------------------------------------------------------ Inhalt ---

P = []
def panel(title, q, a, scene, num=True):
    P.append(dict(title=title, q=q, a=a, scene=scene, num=num))

# --- 1 ---------------------------------------------------------------------
panel(
    "Titel",
    None, None,
    f'''<div class="cover">
<div class="cover-bubbles">
  <div class="bubble b-tail-l" style="max-width:520px">Alle bauen gerade krasse Sachen mit&nbsp;Claude.</div>
  <div class="bubble b-tail-l" style="max-width:560px;margin-left:60px">Und ich versteh&nbsp;kein&nbsp;Wort davon.</div>
</div>
<div class="cover-stage">
  {human("confused")}
  <div class="cloud">
    <span class="q">?</span>
    {chip("CLAUDE.md","blue")}{chip("Skills","red")}{chip("Plugins","orange")}
    {chip("MCP","green")}{chip("Hooks","blue")}{chip("Subagents","red")}
    {chip("/Commands","orange")}{chip("Memory","green")}{chip("Checkpoints","blue")}
    {chip("Cowork","green")}{chip("Routinen","red")}{chip("Plan-Modus","orange")}{chip("/loop","blue")}
  </div>
  <div class="right-of-stage">
    <div class="bubble b-tail-r">Komm, ich erklär&#8217;s dir.</div>
    {bean("point")}
  </div>
</div></div>''',
    num=False)

# --- 2 ---
panel("CLAUDE.md",
  "Fangen wir mit CLAUDE.md an. Warum legt die&nbsp;jeder&nbsp;an?",
  ["CLAUDE.md ist im Grunde eine Bedienungs&shy;anleitung, die du Claude gibst.",
   "Da steht drin, wie dein Projekt funktioniert, welche Regeln gelten – und was Claude auf keinen Fall tun soll."],
  f'''{human("think")}
<div class="stage-mid">{doc("CLAUDE.md","blue",4)}
<div class="mini-row">{chip("Projekt&shy;struktur","blue")}{chip("Regeln","green")}{chip("Verboten!","red")}</div></div>
{bean("right")}''')

# --- 3 ---
panel("CLAUDE.md wird geladen",
  "Ich muss also nicht in jeder Sitzung dasselbe&nbsp;erklären?",
  ["Genau. Claude liest die Datei automatisch, sobald du im Projekt startest.",
   "Es gibt sogar drei Ebenen: global in <code>~/.claude/</code>, im Projekt&shy;ordner und pro Unter&shy;ordner. <code>/init</code> schreibt dir eine erste Fassung."],
  f'''{human("think",0.86)}
<div class="stage-mid">{doc("CLAUDE.md","blue",3)}{machine("Claude", 195)}
<div class="mini-row">{chip("Nutze diesen Stil","blue")}{chip("Führe diese Tests aus","red")}{chip("Ordner nie ändern","orange")}</div>
{chip("Claude hält sich an die Projektregeln","green")}</div>
{bean("point",0.86)}''')

# --- 4 ---
panel("Skills",
  "Okay. Und was sind dann Skills?",
  ["Ein Skill bringt Claude bei, <b>wie</b> eine bestimmte Aufgabe richtig läuft.",
   "Statt jedes Mal deinen ganzen Ablauf zu erklären, machst du daraus einen wieder&shy;verwendbaren Skill."],
  f'''{human("think")}
<div class="stage-mid"><div class="scatter">{doc("Ablauf","blue",2)}{doc("Notiz","red",2)}{doc("Regel","orange",2)}{doc("Vorlage","green",2)}</div>
<div class="arw">&#8595;</div>{chip("SKILL","blue",big=True)}</div>
{bean("right")}''')

# --- 5 ---
panel("Skill-Beispiel",
  "Gib mir mal ein Beispiel.",
  ["Sagen wir, du willst jede Woche denselben Auswertungs&shy;bericht.",
   "Deine Anweisungen, dein Ablauf, deine Beispiele – daraus wird ein Skill, den du nur noch aufrufst."],
  f'''{human("think")}
<div class="stage-mid"><div class="mini-row">{doc("Deine Anweisungen","blue",3)}{doc("Dein Ablauf","orange",3)}{doc("Beispiele","green",3)}</div>
<div class="arw">&#8595;</div>{machine("Claude",230)}<div class="arw">&#8595;</div>
{chip("Skill: Wochen&shy;bericht","blue",big=True)}</div>
{bean("right")}''')

# --- 6 ---
panel("SKILL.md",
  "Und diese SKILL.md-Dateien, die alle von GitHub laden – das sind einfach&nbsp;Anweisungen?",
  ["Ziemlich genau. Ein Skill ist ein Ordner mit einer <code>SKILL.md</code>, dazu Skripte, Vorlagen und Referenz&shy;dateien.",
   "Claude liest zuerst nur Name und Beschreibung – den Rest erst, wenn er ihn wirklich braucht. Aufrufen kannst du ihn auch selbst mit <code>/skill-name</code>."],
  f'''{human("point")}
<div class="stage-mid">{chip("SKILL.md","blue",big=True)}
<div class="mini-row">{doc("scripts/","red",2)}{doc("references/","orange",2)}{doc("assets/","green",2)}</div>
<div class="arw">&#8595;</div>{chip("Wieder&shy;verwendbarer Claude-Ablauf","blue",big=True)}</div>
{bean("right")}''')

# --- 7 ---
panel("Plugins",
  "Und Plugins? Sind das nicht auch einfach&nbsp;Skills?",
  ["Nicht ganz. Ein Skill ist <b>eine</b> Fähigkeit.",
   "Ein Plugin ist eher ein <b>Paket</b>: Skills + Hooks + Subagents + MCP-Server + eigene Befehle in einem Rutsch. Installiert wird&#8217;s über einen Marktplatz mit <code>/plugin</code>."],
  f'''{human("think")}
<div class="stage-mid"><div class="pkg"><div class="pkg-label">PLUGIN</div>
<div class="pkg-grid">{chip("Skills","blue")}{chip("Hooks","red")}{chip("Subagents","orange")}{chip("MCP-Server","green")}</div></div>
<div class="pkg-side">{chip("Skill","blue",big=True)}</div></div>
{bean("right")}''')

# --- 8 ---
panel("MCP",
  "Moment – MCP-Server. Was ist das?",
  ["MCP ist im Grunde die Art, wie Claude sich mit Dingen <b>außerhalb</b> von Claude verbindet.",
   "Ein einheitlicher Stecker für fremde Programme und Dienste."],
  f'''{human("point")}
<div class="stage-mid">{machine("Claude",250)}<div class="arw">&#8595;</div>{chip("MCP","blue",big=True)}
<div class="mini-row">{chip("GitHub","blue")}{chip("Slack","red")}{chip("Daten&shy;bank","orange")}{chip("Drive","green")}{chip("Kalender","blue")}</div></div>
{bean("right")}''')

# --- 9 ---
panel("MCP praktisch",
  "Ich muss also nicht mehr alles von Hand rein&shy;kopieren …",
  ["Claude verbindet sich selbst, holt sich die Information – und darf dort auch handeln, wenn du es erlaubst.",
   "Mit <code>/mcp</code> siehst du, was gerade verbunden ist."],
  f'''<div class="stage-wide">
<div class="half"><div class="half-title t-red">Ohne MCP</div>
{chip("GitHub","blue")}{AD}{human("confused",0.55)}{AD}{machine("Claude",150)}
<div class="cap c-red">du kopierst alles von Hand</div></div>
<div class="divider"></div>
<div class="half"><div class="half-title t-green">Mit MCP</div>
{chip("GitHub","blue")}{AD}{chip("MCP","green")}{AD}{machine("Claude",150)}
<div class="cap c-green">Claude holt es sich selbst</div></div></div>''')

# --- 10 ---
panel("Hooks",
  "Gut. Und Hooks? Das klingt noch verwirrender.",
  ["Hooks sind anders, weil <b>nicht Claude</b> entscheidet, ob sie passieren.",
   "Sie laufen automatisch los, sobald ein bestimmtes Ereignis eintritt. Eingerichtet in <code>settings.json</code> oder über <code>/hooks</code>."],
  f'''{human("think")}
<div class="stage-mid">{machine("Claude",210)}</div>
<div class="stage-mid">{chip("Ereignis passiert","red",big=True)}<div class="arw">&#8595;</div>
{chip("löst automatisch den Hook aus","blue")}<div class="arw">&#8595;</div>{chip("Hook läuft","green",big=True)}</div>
{bean("point")}''')

# --- 11 ---
panel("Hooks Beispiele",
  "Zum Beispiel?",
  ["Ein Hook kann nach jeder Datei&shy;änderung deinen Formatierer starten – oder Claude stoppen, <b>bevor</b> ein gefährlicher Befehl läuft.",
   "Typische Ereignisse: <code>PreToolUse</code>, <code>PostToolUse</code>, <code>UserPromptSubmit</code>, <code>SessionStart</code>, <code>Stop</code>."],
  f'''{human("think",0.82)}
<div class="stage-mid">{machine("Claude",165)}<div class="cap">Claude ändert eine Datei</div><div class="arw">&#8595;</div>
{chip("HOOK läuft automatisch","orange",big=True)}
<div class="mini-row">{chip("Formatieren","blue")}{chip("Testen","green")}{chip("Prüfen","orange")}{chip("Melden","blue")}{chip("STOPP","red")}</div>
<div class="cap c-red">Stopp vor gefährlichen Befehlen</div></div>
{bean("right",0.82)}''')

# --- 12 ---
panel("Subagents",
  "Was ist mit Subagents? Sind das buchstäblich mehrere&nbsp;Claudes?",
  ["Das sind eigen&shy;ständige Arbeiter, denen Claude klar umrissene Aufgaben geben kann – jeder mit eigenem Kontext&shy;fenster und eigenem Modell.",
   "Einer recherchiert, einer prüft Code, einer testet. Danach berichten sie zurück an den Haupt-Claude. Verwaltet über <code>/agents</code>."],
  f'''{human("think")}
<div class="stage-mid">{machine("HAUPT-CLAUDE",260)}
<div class="mini-row">{AD}{AD}{AD}</div>
<div class="mini-row">{chip("Recherche-Agent","green")}{chip("Code-Agent","orange")}{chip("Test-Agent","blue")}</div>
<div class="cap c-blue">Ergebnisse zurück an Claude</div></div>
{bean("point")}''')

# --- 13 ---
panel("Slash-Befehle",
  "Und was sind diese ganzen /irgendwas-Befehle, die alle benutzen?",
  ["Der Schrägstrich ist das Kurzbefehl-Menü von Claude Code.",
   "Es gibt eingebaute wie <code>/clear</code> und <code>/compact</code> – und Skills bringen eigene Befehle mit, die du selbst aufrufen kannst."],
  f'''{human("point",0.78)}
<div class="stage-mid">{machine("/",210)}
<div class="cmds">
<div class="cmd c-green"><b>/clear</b><span>neu anfangen</span></div>
<div class="cmd c-orange"><b>/compact</b><span>Kontext eindampfen</span></div>
<div class="cmd c-blue"><b>/context</b><span>Wer frisst den Platz?</span></div>
<div class="cmd c-red"><b>/rewind</b><span>zurückspulen</span></div>
<div class="cmd c-blue"><b>/model</b><span>Modell wechseln</span></div>
<div class="cmd c-green"><b>/usage</b><span>Verbrauch ansehen</span></div>
</div></div>
{bean("right",0.78)}''')

# --- Berechtigungen ---
panel("Berechtigungen",
  "Darf Claude einfach alles auf meinem Rechner?",
  ["Nein. Von Haus aus darf es lesen – für alles andere fragt es vorher und zeigt Dir genau, was es vorhat.",
   "Wie streng es zugeht, schaltest Du mit <kbd>Shift</kbd>+<kbd>Tab</kbd> um. Im Plan-Modus schaut Claude sich erst alles an und legt Dir einen Vorschlag hin, bevor irgendetwas passiert."],
  breit(human("confused",0.78), bean("hips",0.78),
    f'''<div class="ladder">
<div class="rung c-blue"><b>Manuell</b><span>liest von allein, fragt vor jedem Eingriff</span></div>
<div class="rung c-green"><b>Änderungen ok</b><span>darf Dateien anfassen, der Rest bleibt Rückfrage</span></div>
<div class="rung c-orange"><b>Plan</b><span>schaut nur und schlägt vor – ändert nichts</span></div>
<div class="rung c-red"><b>Automatisch</b><span>arbeitet durch, mit Sicherheitsnetz im Hintergrund</span></div>
</div>''',
    '<div class="cap c-blue">umschalten mit Shift + Tab</div>'))

# --- Tastenkuerzel ---
panel("Kniffe",
  "Gibt es Abkürzungen, die man kennen sollte?",
  ["Vier Zeichen sparen die meiste Tipparbeit – und zwei Tasten sind der Notausgang.",
   "Merk Dir vor allem <kbd>Esc</kbd>: Du musst nicht warten, bis Claude fertig ist. Anhalten, richtigstellen, weitermachen."],
  breit(human("point",0.78), bean("point",0.78),
    f'''<div class="cmds">
<div class="cmd c-blue"><b>@datei</b><span>eine Datei ins Gespräch holen</span></div>
<div class="cmd c-orange"><b>!befehl</b><span>selbst etwas ausführen</span></div>
<div class="cmd c-green"><b>/</b><span>das Befehlsmenü öffnen</span></div>
<div class="cmd c-blue"><b>Shift+Tab</b><span>Berechtigungen umschalten</span></div>
<div class="cmd c-red"><b>Esc</b><span>Claude sofort anhalten</span></div>
<div class="cmd c-red"><b>Esc Esc</b><span>zurückspulen</span></div>
</div>'''))

# --- 14 ---
panel("Context Window",
  "Letzte Frage: Was genau ist dieses Kontext&shy;fenster?",
  ["Das ist Claudes Arbeits&shy;gedächtnis für das laufende Gespräch.",
   "Deine Eingaben, Claudes Antworten, gelesene Dateien und Werkzeug-Ergebnisse belegen alle Platz darin."],
  f'''{human("point")}
<div class="stage-mid"><div class="window"><div class="win-title">Kontextfenster</div>
<div class="win-grid">{chip("Deine Eingaben","green")}{chip("Claudes Antworten","orange")}{chip("Gelesene Dateien","blue")}{chip("Werkzeug-Ergebnisse","red")}</div>
</div></div>
{bean("right")}''')

# --- 15 ---
panel("Kontext voll",
  "Wenn Leute also sagen &#8222;Claude hat den Faden verloren&#8220; …",
  ["… dann ist meist so viel zusammen&shy;gekommen, dass nicht mehr alles gleich&shy;zeitig ins Arbeits&shy;gedächtnis passt.",
   "Claude Code fasst dann automatisch zusammen. Mit <code>/context</code> siehst du, was den Platz belegt, mit <code>/clear</code> fängst du sauber neu an."],
  f'''{human("point",0.7)}
<div class="stage-mid"><div class="window full"><div class="win-title">KONTEXTFENSTER</div>
<div class="win-stack">{chip("Deine Eingaben","green")}{chip("Claudes Antworten","orange")}{chip("Gelesene Dateien","blue")}{chip("Werkzeug-Ergebnisse","red")}{chip("Deine Eingaben","green")}</div>
<div class="spill">{chip("Gelesene Dateien","blue")}{chip("Werkzeug-Ergebnisse","red")}{chip("Deine Eingaben","green")}</div>
</div><div class="arw">&#8595;</div>{chip("Was Claude gerade präsent hat","blue",big=True)}</div>
{bean("hips",0.7)}''')

# --- 16 ---
panel("Checkpoints",
  "Und wenn Claude Mist baut? Alles verloren?",
  ["Nein – Claude Code setzt automatisch Sicherungs&shy;punkte, bevor es Dateien ändert.",
   "Zweimal <kbd>Esc</kbd> oder <code>/rewind</code>, und du spulst zurück: nur das Gespräch, nur die Dateien oder beides."],
  f'''{human("think",0.84)}
<div class="stage-mid">
<div class="chain">{chip("Stand A","green")}{AR}{chip("Stand B","blue")}{AR}{chip("Stand C","red")}</div>
<div class="cap c-red">hier ging&#8217;s schief</div>
<div class="rewind">&#8592; &#8592; &#8592;</div>
{chip("/rewind &#8211; zurück auf Stand&nbsp;B","green",big=True)}</div>
{bean("thumbs",0.84)}''')

# --- 17 ---
panel("Memory",
  "Merkt sich Claude auch etwas über eine Sitzung hinaus?",
  ["Ja – dafür gibt es das Gedächtnis: kleine Notiz&shy;dateien, die Claude selbst schreibt und beim nächsten Start wieder liest.",
   "Deine Vorlieben, Projekt&shy;stände, wiederkehrende Entscheidungen. Anders als CLAUDE.md pflegt Claude das selbst."],
  f'''{human("think")}
<div class="stage-mid">{machine("Claude",210)}
<div class="mini-row">{AD}{AD}</div>
<div class="mini-row">{doc("MEMORY.md","blue",3)}{doc("notiz.md","green",3)}</div>
<div class="cap c-blue">bleibt über Sitzungen hinweg erhalten</div></div>
{bean("point")}''')

# --- 18 ---
panel("Überall",
  "Und das läuft alles nur im Terminal?",
  ["Längst nicht mehr. Claude Code gibt&#8217;s als Terminal-Befehl, als Desktop-App, im Browser unter <code>claude.ai/code</code> und als Erweiterung für VS&nbsp;Code und JetBrains.",
   "Dazu Agenten, die im Hintergrund oder in der Cloud weiter&shy;arbeiten, während du etwas anderes machst."],
  f'''{human("happy",0.86)}
<div class="stage-mid"><div class="mini-row">{chip("Terminal","blue")}{chip("Desktop-App","red")}{chip("Browser","orange")}{chip("VS&nbsp;Code / JetBrains","green")}</div>
{machine("Claude",190)}
{chip("dieselbe Sitzung, überall","blue",big=True)}</div>
{bean("right",0.86)}''')

# --- Desktop: drei Reiter ---
panel("Desktop",
  "Es gibt das alles auch zum Anklicken?",
  ["Ja. Die Claude-App für den Rechner hat drei Reiter: <b>Chat</b> ist das Gespräch, <b>Cowork</b> erledigt Büroarbeit, <b>Code</b> ist Claude Code mit Oberfläche.",
   "Es gibt sie für Mac und Windows, für Linux als Beta."],
  breit(human("think",0.78), bean("right",0.78),
    '<div class="tabs"><div class="tab">Chat</div><div class="tab">Cowork</div><div class="tab on">Code</div></div>',
    f'''<div class="mini-row">
{chip("Reden","blue",sub="Fragen, Entwürfe, Ideen")}
{chip("Arbeiten lassen","green",sub="Dokumente und Ordner")}
{chip("Entwickeln","orange",sub="Quelltext und Git")}</div>'''))

# --- Desktop: parallele Sitzungen ---
panel("Parallele Sitzungen",
  "Was kann die App, was das Terminal nicht kann?",
  ["Mehrere Sitzungen nebeneinander – jede in ihrer eigenen Git-Arbeitskopie. So kommen sie sich nicht in die Quere, auch wenn sie an derselben Stelle werkeln.",
   "Dazu Editor, Terminal, Vorschau und die Durchsicht der Änderungen im selben Fenster. Losschicken kannst Du eine Sitzung sogar vom Handy."],
  breit(human("point",0.78), bean("point",0.78),
    f'''<div class="mini-row">
{chip("Sitzung 1","blue",sub="eigene Arbeitskopie")}
{chip("Sitzung 2","green",sub="eigene Arbeitskopie")}
{chip("Sitzung 3","orange",sub="eigene Arbeitskopie")}</div>''',
    AD,
    f'''<div class="mini-row">{chip("Editor","blue")}{chip("Terminal","blue")}{chip("Vorschau","blue")}{chip("Änderungen prüfen","blue")}</div>''',
    '<div class="cap c-blue">alles in einem Fenster</div>'))

# --- Cowork: was ist das ---
panel("Cowork",
  "Und was ist dann Cowork?",
  ["Dieselbe Technik wie Claude Code – nur in der ganz normalen Claude-App statt im Terminal, ohne Einrichten.",
   "Du gibst Ordner frei, beschreibst das Ziel, und Claude arbeitet los: Tabellen mit echten Formeln, Präsentationen, fertige Dokumente."],
  breit(human("think",0.78), bean("right",0.78),
    f'''<div class="mini-row">{chip("Deine Ordner","blue")}{chip("Deine Zugänge","blue")}</div>''',
    AD,
    f'''{chip("COWORK","green",big=True)}''',
    AD,
    f'''<div class="mini-row">{doc("Tabelle","green",3)}{doc("Präsentation","orange",3)}{doc("Bericht","blue",3)}</div>'''))

# --- Cowork: konkret ---
panel("Cowork konkret",
  "Was macht es denn so?",
  ["Einen Ordner voller Belegfotos in eine Abrechnung verwandeln. Aus einem Stapel Notizen einen Bericht schreiben. Eine Ablage aufräumen. Dafür bedient es notfalls auch Chrome – klicken, tippen, Formulare ausfüllen.",
   "Wie viel es allein entscheiden darf, legst Du fest."],
  breit(human("happy",0.78), bean("thumbs",0.78),
    f'''<div class="mini-row">
{chip("Belege &#8594; Abrechnung","green")}{chip("Notizen &#8594; Bericht","orange")}{chip("Ablage aufräumen","blue")}</div>''',
    '<div class="cap">und wenn nötig direkt im Browser</div>',
    f'''<div class="mini-row">
{chip("Fragt jedes Mal","blue",sub="Du nickst alles ab")}
{chip("Entscheidet selbst","green",sub="mit Sicherheitsnetz")}
{chip("Macht einfach","orange",sub="ohne Rückfrage")}</div>'''))

# --- Cowork oder Code ---
panel("Die drei Stufen",
  "Wann nehme ich denn was?",
  ["Die Frage ist immer, wie weit Claude an Deine Sachen darf. Cowork bekommt einzelne Ordner, läuft abgeschottet und braucht keine Einrichtung.",
   "Claude Code bekommt den ganzen Rechner. Nur hier kannst Du ihm eigene Werkzeuge beibringen – und nur hier läuft er weiter, wenn Du weg bist."],
  breit(human("think",0.78), bean("point",0.78),
    f'''<div class="ladder">
<div class="rung c-blue"><b>1 · Im Gespräch</b><span>nichts einzurichten – Du lädst hoch, Du lädst herunter</span></div>
<div class="rung c-green"><b>2 · Cowork</b><span>Desktop-App: Claude arbeitet in Deinen Ordnern</span></div>
<div class="rung c-orange"><b>3 · Claude Code</b><span>hier bist Du: der ganze Rechner, eigene Werkzeuge, läuft ohne Dich</span></div>
</div>''',
    '<div class="cap c-blue">erledigen lassen → Cowork · Werkzeuge bauen, die von allein laufen → Code</div>'))

# --- Routinen ---
panel("Routinen",
  "Und wenn etwas regelmäßig von allein laufen soll?",
  ["Dann legst Du eine Routine an: Auftrag, Projekt und Zugänge einmal gespeichert – danach läuft sie ohne Dich.",
   "Und zwar in der Cloud. Dein Rechner darf ausgeschaltet sein. Angelegt wird sie mit <code>/schedule</code>, in der App oder im Browser."],
  breit(human("think",0.78), bean("point",0.78),
    f'''{chip("/schedule täglich um 9 Uhr die neuen Pull Requests durchsehen","blue")}''',
    AD,
    f'''<div class="mini-row">{chip("Auftrag","blue")}{chip("Projekt","green")}{chip("Zugänge","orange")}</div>''',
    AD,
    f'''{chip("läuft in der Cloud – Rechner aus","green",big=True)}'''))

# --- Routinen: Ausloeser ---
panel("Auslöser",
  "Und was bringt so eine Routine ins Rollen?",
  ["Drei Dinge, einzeln oder in Kombination: ein Zeitplan, ein Aufruf von außen, oder ein Ereignis auf GitHub.",
   "Der kürzeste Abstand ist eine Stunde. Einmalige Termine gehen auch – <code>/schedule in zwei Wochen …</code> Das Ganze ist noch im Vorschau-Stadium."],
  breit(human("point",0.78), bean("thumbs",0.78),
    f'''<div class="mini-row">
{chip("Zeitplan","green",sub="stündlich bis wöchentlich")}
{chip("Aufruf","orange",sub="von Deinen Werkzeugen")}
{chip("GitHub","blue",sub="neuer Pull Request")}</div>''',
    AD,
    f'''{chip("Routine läuft","blue",big=True)}''',
    AD,
    f'''{chip("Ergebnis liegt morgens da","green")}'''))

# --- /loop ---
panel("Schleife",
  "Und wenn es nur für die nächste Stunde sein soll?",
  ["Dann nimm <code>/loop</code>. Der wiederholt einen Auftrag in der offenen Sitzung – auf Deinem Rechner, mit Deinen Dateien.",
   "Lässt Du die Zeitangabe weg, sucht sich Claude den Abstand selbst: kurz, solange sich etwas tut, länger, wenn Ruhe ist. <kbd>Esc</kbd> beendet die Schleife."],
  breit(human("think",0.76), bean("point",0.76),
    f'''{chip("/loop 5m schau nach, ob der Bau durch ist","blue")}''',
    '<div class="rewind">&#8635; &#8635; &#8635;</div>',
    f'''<div class="mini-row">
{chip("mit Zeitangabe","green",sub="alle 5 Minuten")}
{chip("ohne Zeitangabe","orange",sub="Claude entscheidet")}
{chip("ganz ohne Auftrag","blue",sub="räumt selbst auf")}</div>''',
    '<div class="cap">läuft nur, solange die Sitzung offen ist – und endet nach sieben Tagen</div>'))

# --- Schleife oder Routine ---
panel("Schleife oder Routine",
  "Das klingt doch fast wie eine Routine.",
  ["Der Unterschied ist, wo es läuft. Die Schleife braucht Deine offene Sitzung und Deinen eingeschalteten Rechner – dafür sieht sie Deine Dateien.",
   "Die Routine läuft in der Cloud, ohne Dich. Faustregel: Schleife für heute Nachmittag, Routine für jeden Montag."],
  f'''<div class="stage-wide">
<div class="half"><div class="half-title t-green">/loop</div>
{chip("auf Deinem Rechner","green")}{chip("Sitzung muss offen sein","green")}{chip("sieht Deine Dateien","green")}
<div class="cap c-green">für jetzt gerade</div></div>
<div class="divider"></div>
<div class="half"><div class="half-title">/schedule</div>
{chip("in der Cloud","blue")}{chip("Rechner darf aus sein","blue")}{chip("frische Kopie des Projekts","blue")}
<div class="cap c-blue">für jede Woche</div></div></div>''')

# --- 19 ---
panel("Modelle",
  "Und welches Modell arbeitet da eigentlich?",
  ["Stand August 2026: <b>Opus&nbsp;5</b> für die schweren Sachen, <b>Sonnet&nbsp;5</b> für den Alltag, <b>Haiku&nbsp;4.5</b> für schnell und günstig.",
   "Umschalten mit <code>/model</code>. Mit <code>/fast</code> antwortet Opus schneller – es wird dabei nicht durch ein kleineres Modell ersetzt."],
  f'''{human("think",0.8)}
<div class="stage-mid"><div class="models">
<div class="model c-blue"><b>Opus 5</b><span>die schweren Aufgaben</span><i>1 Mio. Kontext</i></div>
<div class="model c-green"><b>Sonnet 5</b><span>der Alltag</span><i>1 Mio. Kontext</i></div>
<div class="model c-orange"><b>Haiku 4.5</b><span>schnell &amp; günstig</span><i>200 Tsd. Kontext</i></div>
</div>
<div class="cap c-blue">wechseln mit /model</div></div>
{bean("right",0.8)}''')

# --- Gut fragen ---
panel("Gut fragen",
  "Und wie sage ich es am besten?",
  ["Sag das Ziel, nicht die einzelnen Schritte – den Weg findet Claude selbst. Sag dazu, woran man merkt, dass es fertig ist.",
   "Und gib den Zusammenhang mit: für wen das gedacht ist, wozu, und was auf keinen Fall passieren darf. Je klarer der Auftrag, desto weniger Runden."],
  breit(human("think",0.74), bean("right",0.74),
    f'''<div class="saybox c-red"><div class="say-label">eher nicht</div>
<div class="say-text">&#8222;Mach die Tabelle mal schöner.&#8220;</div></div>
{AD}
<div class="saybox c-green"><div class="say-label">besser</div>
<div class="say-text">&#8222;Die Tabelle geht an den Vorstand. Zahlen rechtsbündig, Summenzeile fett, keine Farben. Prüf am Ende, dass die Summen stimmen.&#8220;</div></div>'''))

# --- Nachpruefen ---
panel("Nachprüfen",
  "Kann ich mich denn darauf verlassen?",
  ["Meistens ja – aber Claude kann sich auch überzeugend irren. Lass Dir zeigen, was es getan hat, statt es nur zu glauben.",
   "Und was sich prüfen lässt, soll Claude gleich selbst prüfen: Tests laufen lassen, Zahlen nachrechnen, Quellen nennen."],
  breit(human("think",0.78), bean("thumbs",0.78),
    f'''<div class="mini-row">
{chip("Änderungen ansehen","blue",sub="nicht nur die Zusammenfassung")}
{chip("Tests laufen lassen","green",sub="am besten automatisch")}</div>''',
    f'''<div class="mini-row">
{chip("Quellen nennen lassen","orange",sub="woher stammt die Zahl?")}
{chip("Im Zweifel zurückspulen","red",sub="Esc Esc kostet nichts")}</div>''',
    '<div class="cap">Vertrauen ist gut. Nachsehen ist schneller als Reparieren.</div>'))

# --- Fremde Inhalte ---
panel("Fremde Inhalte",
  "Und wenn in einer Datei steht &#8222;lösche alles&#8220;?",
  ["Gute Frage – genau da liegt die Stolperfalle. Claude liest Webseiten, Mails, Tickets und fremden Quelltext. Nichts davon ist ein Auftrag von Dir.",
   "Aufträge kommen von Dir, aus Deinen Projektregeln und aus dem, was Du erlaubst. Alles andere ist Material zum Lesen – deshalb sind die Berechtigungen keine Schikane."],
  breit(human("confused",0.76), bean("hips",0.76),
    f'''<div class="mini-row">{chip("Deine Anweisung","green",sub="zählt")}{chip("CLAUDE.md","green",sub="zählt")}</div>''',
    f'''<div class="mini-row">{chip("Webseite","red",sub="nur Material")}{chip("E-Mail","red",sub="nur Material")}{chip("fremdes Ticket","red",sub="nur Material")}</div>''',
    '<div class="cap c-blue">Je weiter Claude nach draußen darf, desto enger halte die Leine</div>'))

# --- 20 ---
panel("Fazit",
  "Ohh. Ich glaub, jetzt hab ich&#8217;s.",
  ["Das freut mich zu hören."],
  f'''<div class="finale">
<div class="fin-figs">{human("happy")}<div class="bulb">&#128161;</div>{bean("thumbs")}</div>
<div class="fin-box">
<div class="fin-line"><b>CLAUDE.md</b> &#8211; die Regeln deines Projekts</div>
<div class="fin-line"><b>Skills</b> &#8211; wie eine Aufgabe richtig läuft</div>
<div class="fin-line"><b>Plugins</b> &#8211; alles davon als ein Paket</div>
<div class="fin-line"><b>MCP</b> &#8211; die Verbindung nach draußen</div>
<div class="fin-line"><b>Hooks</b> &#8211; laufen automatisch bei Ereignissen</div>
<div class="fin-line"><b>Subagents</b> &#8211; Helfer mit eigenem Kopf</div>
<div class="fin-line"><b>Kontextfenster</b> &#8211; das Arbeitsgedächtnis</div>
<div class="fin-line"><b>Checkpoints &amp; Memory</b> &#8211; zurückspulen und behalten</div>
<div class="fin-line"><b>Cowork</b> &#8211; dasselbe in Deinen Ordnern, ohne Terminal</div>
<div class="fin-line"><b>Routinen</b> &#8211; laufen nach Plan in der Cloud</div>
<div class="fin-line"><b>Berechtigungen</b> &#8211; Du bestimmst, wie weit Claude darf</div>
<div class="fin-line"><b>/loop</b> &#8211; wiederholt etwas, solange Du dabei bist</div>
</div></div>''')

# ------------------------------------------------------------------- Bau ----

def bubbles(q, a):
    out = ""
    if q:
        out += f'<div class="bubble b-q b-tail-l">{q}</div>'
    if a:
        body = "".join(f"<p>{x}</p>" for x in a)
        out += f'<div class="bubble b-a b-tail-r">{body}</div>'
    return f'<div class="bubbles">{out}</div>' if out else ""

pages = []
total = len(P) - 1
n = 0
for p in P:
    if p["num"]:
        n += 1
        badge = f'<div class="badge">{n}/{total}</div>'
    else:
        badge = ""
    pages.append(f'<section class="page">{badge}{bubbles(p["q"], p["a"])}'
                 f'<div class="scene">{p["scene"]}</div></section>')

HTML = f'''<!doctype html>
<html lang="de"><head><meta charset="utf-8">
<title>Claude Code – die Anleitung</title>
<style>
@font-face {{ font-family:'PH'; src:url(data:font/ttf;base64,{PATRICK}) format('truetype'); }}
@font-face {{ font-family:'CV'; font-weight:400; src:url(data:font/ttf;base64,{CAVEAT}) format('truetype'); }}
@font-face {{ font-family:'CV'; font-weight:700; src:url(data:font/ttf;base64,{CAVEAT_B}) format('truetype'); }}

@page {{ size: 210mm 262mm; margin: 0; }}
* {{ box-sizing: border-box; }}
html, body {{ margin:0; padding:0; background:#fff; color:#141414;
  font-family:'PH', sans-serif; -webkit-font-smoothing:antialiased; }}

.page {{ width:210mm; height:262mm; padding:14mm 14mm 11mm; position:relative;
  display:flex; flex-direction:column; page-break-after:always; overflow:hidden; }}
.page:last-child {{ page-break-after:auto; }}

.badge {{ position:absolute; top:4.5mm; right:11mm; background:#7a7a7a; color:#fff;
  border-radius:20px; padding:2px 15px 4px; font-size:18px; letter-spacing:.5px; z-index:5; }}

/* ---- Sprechblasen ---- */
.bubbles {{ display:flex; gap:16px; align-items:flex-start; margin-bottom:6mm; }}
.bubble {{ border:3.4px solid #141414; background:#fff; padding:14px 20px 16px;
  font-size:25px; line-height:1.28; position:relative;
  border-radius:34px 28px 36px 30px / 28px 34px 26px 32px; }}
.bubble p {{ margin:0 0 12px; }} .bubble p:last-child {{ margin-bottom:0; }}
.bubble code {{ font-family:'DejaVu Sans Mono', monospace; font-size:19px;
  background:#f0f0f0; border-radius:5px; padding:1px 5px; }}
.bubble kbd {{ font-family:'DejaVu Sans Mono', monospace; font-size:17px;
  border:2px solid #141414; border-radius:5px; padding:0 5px; }}
.b-q {{ flex:0 1 40%; align-self:flex-start; }}
.b-a {{ flex:1 1 58%; }}
.b-tail-l::after, .b-tail-r::after {{ content:''; position:absolute; bottom:-22px;
  width:0; height:0; border-top:24px solid #141414; }}
.b-tail-l::after {{ left:34px; border-right:26px solid transparent; }}
.b-tail-r::after {{ right:44px; border-left:26px solid transparent; }}
.b-tail-l::before, .b-tail-r::before {{ content:''; position:absolute; bottom:-15px;
  width:0; height:0; border-top:22px solid #fff; z-index:1; }}
.b-tail-l::before {{ left:39px; border-right:20px solid transparent; }}
.b-tail-r::before {{ right:49px; border-left:20px solid transparent; }}

/* ---- Bühne ---- */
.scene {{ flex:1; display:flex; align-items:center; justify-content:space-between;
  gap:10px; padding-top:6mm; }}
.fig {{ height:calc(252px * var(--s,1)); flex:0 0 auto; }}
.ink .sk {{ fill:#fff; stroke:#141414; stroke-width:3.4; stroke-linejoin:round; }}
.ink .ln {{ fill:none; stroke:#141414; stroke-width:3.4; stroke-linecap:round; }}
.ink .lnb {{ fill:none; stroke:#141414; stroke-width:5; stroke-linecap:round; }}
.ink .hatch line {{ stroke:#141414; stroke-width:2.6; stroke-linecap:round; }}
.machine {{ flex:0 0 auto; }}
.mlabel {{ font-family:'CV'; font-weight:700; font-size:30px; fill:#1a3a8f; }}

.stage-mid {{ flex:1; display:flex; flex-direction:column; align-items:center;
  justify-content:center; gap:14px; min-width:0; }}
.stage-wide {{ flex:1; display:flex; align-items:stretch; gap:14px; }}
.row {{ display:flex; align-items:center; justify-content:center; flex-wrap:wrap; }}
.col {{ display:flex; flex-direction:column; align-items:center; }}
.mini-row {{ display:flex; gap:12px; justify-content:center; flex-wrap:wrap; align-items:center; }}
.arw {{ font-size:40px; line-height:1; color:#1a3a8f; font-family:'DejaVu Sans', sans-serif; }}

/* ---- Kästchen ---- */
.chip {{ border:3px solid; border-radius:8px 6px 9px 7px / 7px 9px 6px 8px;
  padding:9px 18px 11px; font-size:26px; background:#fff; display:flex;
  flex-direction:column; align-items:center; text-align:center; line-height:1.15; }}
.chip.big {{ font-size:31px; padding:12px 28px 15px; }}
.chip-sub {{ font-size:18px; opacity:.75; }}
.c-blue {{ border-color:#1a3a8f; color:#1a3a8f; }}
.c-red {{ border-color:#c8322b; color:#c8322b; }}
.c-orange {{ border-color:#d97b20; color:#c26a12; }}
.c-green {{ border-color:#2a7a3a; color:#2a7a3a; }}
.t-red {{ color:#c8322b; }} .t-green {{ color:#2a7a3a; }}

.doc {{ border:3px solid; border-radius:6px; background:#fff; padding:9px 12px 11px;
  min-width:142px; }}
.doc b {{ font-size:23px; font-weight:400; display:block; margin-bottom:7px; }}
.doc .lines i {{ display:block; height:3.5px; background:currentColor; opacity:.5;
  margin-bottom:5px; border-radius:2px; }}
.scatter {{ display:flex; gap:12px; flex-wrap:wrap; justify-content:center; }}
.cap {{ font-size:23px; color:#555; }}
.cap.c-blue {{ color:#1a3a8f; }} .cap.c-red {{ color:#c8322b; }} .cap.c-green {{ color:#2a7a3a; }}

/* ---- Titelseite ---- */
.cover {{ display:flex; flex-direction:column; height:100%; }}
.cover-bubbles {{ display:flex; flex-direction:column; gap:22px; margin-bottom:7mm; }}
.cover-bubbles .bubble {{ font-size:31px; }}
.cover-stage {{ flex:1; display:flex; align-items:center; justify-content:space-between; }}
.cover-stage .fig {{ height:236px; }}
.cloud {{ flex:1; display:flex; flex-wrap:wrap; gap:10px; justify-content:center;
  align-items:center; padding:0 8px; position:relative; }}
.cloud .chip:nth-child(2n) {{ transform:rotate(-4deg); }}
.cloud .chip:nth-child(3n) {{ transform:rotate(3deg); }}
.cloud .q {{ font-size:74px; color:#1a3a8f; }}
.cloud .chip {{ font-size:23px; padding:7px 15px 9px; }}
.right-of-stage {{ display:flex; flex-direction:column; align-items:center; gap:10px; }}
.right-of-stage .bubble {{ font-size:24px; }}

/* ---- Spezialbausteine ---- */
.pkg {{ border:3.4px solid #1a3a8f; border-radius:10px; padding:14px; background:#fff; }}
.pkg-label {{ font-family:'CV'; font-weight:700; font-size:52px; color:#1a3a8f;
  text-align:center; margin-bottom:10px; }}
.pkg-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:10px; }}
.pkg-side {{ margin-top:14px; }}
.half {{ flex:1; display:flex; flex-direction:column; align-items:center;
  justify-content:center; gap:12px; }}
.half-title {{ font-size:27px; border:3px solid currentColor; border-radius:8px; padding:4px 14px 6px; }}
.divider {{ width:0; border-left:3px dashed #999; }}
.cmds {{ display:grid; grid-template-columns:auto auto; gap:11px; margin-top:8px; }}
.cmd {{ border:3px solid; border-radius:8px; padding:8px 16px 10px; background:#fff;
  display:flex; flex-direction:column; align-items:flex-start; gap:1px; min-width:186px; }}
.cmd b {{ font-weight:400; font-size:26px; font-family:'DejaVu Sans Mono', monospace; }}
.cmd span {{ font-size:20px; color:#444; }}
.window {{ border:3.4px solid #141414; border-radius:6px; padding:14px 16px 16px;
  background:#fff; min-width:372px; }}
.win-title {{ font-family:'CV'; font-weight:700; font-size:40px; color:#1a3a8f;
  text-align:center; margin-bottom:12px; }}
.win-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:10px; }}
.win-stack {{ display:flex; flex-direction:column; gap:6px; }}
.win-stack .chip {{ font-size:22px; padding:5px 14px 7px; }}
.spill {{ display:flex; gap:8px; margin-top:10px; justify-content:center; opacity:.45; }}
.spill .chip {{ font-size:17px; padding:3px 9px 5px; transform:rotate(-7deg); }}
.ladder {{ display:flex; flex-direction:column; gap:9px; width:92%; }}
.rung {{ border:3px solid; border-radius:8px; padding:8px 18px 10px; background:#fff;
  display:flex; align-items:baseline; gap:14px; }}
.rung b {{ font-weight:400; font-size:26px; min-width:210px; }}
.rung span {{ font-size:20px; color:#444; }}
.saybox {{ border:3px solid; border-radius:10px; padding:10px 20px 14px; background:#fff; width:88%; }}
.say-label {{ font-size:19px; opacity:.8; margin-bottom:3px; }}
.say-text {{ font-size:25px; color:#141414; line-height:1.3; }}
.scene-col {{ flex:1; align-self:stretch; display:flex; flex-direction:column;
  width:100%; gap:4px; }}
.figrow {{ display:flex; justify-content:space-between; align-items:flex-end; width:100%; }}
.wide {{ flex:1; display:flex; flex-direction:column; align-items:center;
  justify-content:center; gap:13px; width:100%; }}
.tabs {{ display:flex; gap:0; border-bottom:3.4px solid #141414; }}
.tab {{ border:3px solid #141414; border-bottom:none; border-radius:9px 9px 0 0;
  padding:9px 26px 11px; font-size:26px; background:#f2f2f2; color:#666; margin-right:7px; }}
.tab.on {{ background:#fff; color:#1a3a8f; border-color:#1a3a8f; font-size:29px; padding:11px 30px 13px; }}
.chain {{ display:flex; align-items:center; gap:8px; flex-wrap:nowrap; }}
.chain .chip {{ font-size:22px; padding:7px 13px 9px; white-space:nowrap; }}
.chain .arw {{ font-size:32px; }}
.rewind {{ font-size:36px; color:#2a7a3a; letter-spacing:8px;
  font-family:'DejaVu Sans', sans-serif; }}
.models {{ display:flex; gap:12px; }}
.model {{ border:3px solid; border-radius:8px; padding:12px 14px 14px; background:#fff;
  text-align:center; min-width:138px; }}
.model b {{ font-weight:400; font-size:32px; display:block; }}
.model span {{ font-size:21px; color:#444; display:block; margin:4px 0; }}
.model i {{ font-style:normal; font-size:19px; opacity:.7; }}
.finale {{ flex:1; display:flex; flex-direction:column; align-items:center;
  justify-content:center; gap:18px; }}
.fin-figs {{ display:flex; align-items:flex-end; gap:30px; }}
.fin-figs .fig {{ height:210px; }}
.bulb {{ font-size:52px; align-self:flex-start; margin-top:20px;
  font-family:'Noto Color Emoji', sans-serif; }}
.fin-box {{ border:3.4px solid #1a3a8f; border-radius:12px; padding:16px 26px 18px; }}
.fin-line {{ font-size:23px; line-height:1.45; }}
.fin-line b {{ font-weight:400; color:#1a3a8f; }}
</style></head>
<body>
{"".join(pages)}
</body></html>'''

gewuenscht = [a for a in sys.argv[1:] if a in ("de", "en")] or ["de", "en"]

if "de" in gewuenscht:
    out = HERE / "claude-anleitung.html"
    out.write_text(HTML, encoding="utf-8")
    print(f"geschrieben: {out}  ({len(HTML)/1024:.0f} KB, {len(P)} Seiten)")

if "en" in gewuenscht:
    import i18n, texte_en
    en, fehlt = i18n.uebersetze(HTML, texte_en.TEXTE)
    if fehlt:
        print("FEHLENDE ÜBERSETZUNGEN (texte_en.py):")
        for f in fehlt:
            print("   ", repr(f))
        sys.exit(1)
    en = en.replace('<html lang="de">', '<html lang="en">', 1)
    en = en.replace("<title>Claude Code – die Anleitung</title>",
                    f"<title>{texte_en.TITEL}</title>", 1)
    out = HERE / "claude-code-comic-en.html"
    out.write_text(en, encoding="utf-8")
    print(f"geschrieben: {out}  ({len(en)/1024:.0f} KB, {len(P)} Seiten)")
