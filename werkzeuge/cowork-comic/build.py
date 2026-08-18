#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die Claude-Cowork-Comic-Anleitung als HTML (danach -> PDF).

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

# --- Titel ---
panel(
    "Titel",
    None, None,
    f'''<div class="cover">
<div class="cover-bubbles">
  <div class="bubble b-tail-l" style="max-width:560px">Claude soll jetzt richtig <i>arbeiten</i>? Ich&nbsp;kann&nbsp;aber nicht programmieren.</div>
  <div class="bubble b-tail-l" style="max-width:540px;margin-left:60px">Und ein Terminal hab ich noch nie&nbsp;aufgemacht.</div>
</div>
<div class="cover-stage">
  {human("confused")}
  <div class="cloud">
    <span class="q">?</span>
    {chip("Ordner","blue")}{chip("Der Plan","green")}{chip("Tabellen","orange")}
    {chip("Folien","red")}{chip("Verbindungen","blue")}{chip("Projekte","green")}
    {chip("Rechte","orange")}{chip("Zeitplan","red")}{chip("Sicherheit","blue")}
    {chip("Helfer","green")}{chip("Chrome","orange")}{chip("Skills","blue")}
  </div>
  <div class="right-of-stage">
    <div class="bubble b-tail-r">Brauchst Du&nbsp;nicht.</div>
    {bean("point")}
  </div>
</div></div>''',
    num=False)

# --- Was ist Cowork ---
panel("Was ist Cowork",
  "Also – was ist Cowork überhaupt?",
  ["Dieselbe Technik, die hinter Claude Code steckt – aber Du bedienst sie in der ganz normalen Claude-App. Kein Terminal, nichts einzurichten.",
   "Sie ist für Büroarbeit gedacht: recherchieren, auswerten, Dokumente erstellen. Alles, was aus mehreren Schritten besteht."],
  breit(human("think",0.78), bean("right",0.78),
    f'''<div class="mini-row">{chip("Recherche","blue")}{chip("Auswertung","green")}{chip("Dokumente","orange")}{chip("Aufräumen","red")}</div>''',
    AD,
    f'''{chip("COWORK","green",big=True)}''',
    AD,
    '<div class="cap c-green">dieselbe Technik wie Claude Code – nur ohne Terminal</div>'))

# --- Chat oder Cowork ---
panel("Chat oder Cowork",
  "Aber ich kann Claude doch jetzt schon Fragen&nbsp;stellen?",
  ["Klar – und im Chat bekommst Du sogar fertige Dateien. Gebaut werden sie aber in einem abgeschotteten Bereich, und Du lädst sie Dir herunter.",
   "In Cowork arbeitet Claude <b>direkt in Deinen Ordnern</b>: liest, was dort liegt, und legt das Ergebnis daneben. Kein Hochladen, kein Herunterladen."],
  f'''<div class="stage-wide">
<div class="half"><div class="half-title">Im Chat</div>
{chip("Du lädst hoch","blue")}{AD}{chip("Claude baut","blue")}{AD}{chip("Du lädst herunter","blue")}
<div class="cap">alles geht durch Dich hindurch</div></div>
<div class="divider"></div>
<div class="half"><div class="half-title t-green">In Cowork</div>
{chip("Dein Ordner","green")}{AD}{chip("Claude arbeitet darin","green")}{AD}{doc("Ergebnis liegt da","green",3)}
<div class="cap c-green">nichts hoch, nichts herunter</div></div></div>''')

# --- Erste Schritte ---
panel("Erste Schritte",
  "Wie fange ich an?",
  ["Vier Schritte. Im Eingabefeld schaltest Du von <b>Chat</b> auf <b>Cowork</b> um – das ist schon der schwierigste Teil.",
   "Dann beschreibst Du, was herauskommen soll. Claude zeigt Dir seinen Plan. Du schaust drüber, und dann läuft es los."],
  breit(human("point",0.78), bean("right",0.78),
    f'''<div class="tabs"><div class="tab">Chat</div><div class="tab on">Cowork</div></div>''',
    f'''<div class="ladder">
<div class="rung c-blue"><b>1 · Umschalten</b><span>von Chat auf Cowork</span></div>
<div class="rung c-green"><b>2 · Beschreiben</b><span>„Sortiere meinen Download-Ordner“</span></div>
<div class="rung c-orange"><b>3 · Plan ansehen</b><span>Claude zeigt, was es vorhat</span></div>
<div class="rung c-red"><b>4 · Laufen lassen</b><span>zuschauen – oder später wiederkommen</span></div>
</div>'''))

# --- Der Plan ---
panel("Der Plan",
  "Legt es dann einfach los?",
  ["Nein. Claude überlegt sich erst einen Plan und zeigt ihn Dir – bevor irgendetwas passiert.",
   "Und während es arbeitet, siehst Du bei jedem Schritt, was es gerade tut. Kein schwarzer Kasten."],
  breit(human("think",0.78), bean("point",0.78),
    f'''{chip("Deine Aufgabe","blue",big=True)}''',
    AD,
    f'''<div class="saybox c-green"><div class="say-label">Claude zeigt Dir zuerst:</div>
<div class="say-text">„Ich sehe mir die 34 Belege an, ordne sie nach Datum, ziehe die Beträge heraus und baue daraus eine Tabelle mit Summenformel.“</div></div>''',
    AD,
    f'''<div class="mini-row">{chip("Du nickst","green")}{chip("oder Du korrigierst","orange")}</div>'''))

# --- Ordner freigeben ---
panel("Ordner freigeben",
  "Woher weiß es, wo meine Sachen liegen?",
  ["Du gibst ihm einen Ordner frei. Claude liest und schreibt dann direkt darin – Du musst nichts hochladen und nichts herunterladen.",
   "Das geht über die Desktop-App, nur für die Ordner, die Du ausgewählt hast, und nur solange die App läuft."],
  breit(human("think",0.78), bean("right",0.78),
    f'''<div class="mini-row">{chip("Nur dieser Ordner","green",sub="von Dir ausgewählt")}{chip("Alles andere","red",sub="bleibt zu")}</div>''',
    AD,
    f'''<div class="mini-row">{doc("Beleg.pdf","blue",2)}{doc("Notizen.txt","orange",2)}{doc("Liste.xlsx","green",2)}</div>''',
    '<div class="cap c-blue">kein Hochladen, kein Herunterladen – Claude arbeitet direkt darin</div>'))

# --- Was kommt raus ---
panel("Was herauskommt",
  "Und was bekomme ich am Ende?",
  ["Richtige Dateien, keine Textwüste zum Abtippen.",
   "Tabellen mit <b>funktionierenden Formeln</b>, Präsentationen, sauber formatierte Dokumente. Zum Öffnen und Weiterschicken."],
  breit(human("happy",0.78), bean("thumbs",0.78),
    f'''<div class="mini-row">
{doc("Tabelle","green",4)}{doc("Präsentation","orange",4)}{doc("Bericht","blue",4)}</div>''',
    f'''<div class="mini-row">{chip("mit echten Formeln","green")}{chip("fertig formatiert","orange")}{chip("mit Quellenangabe","blue")}</div>'''))

# --- Beispiele ---
panel("Beispiele",
  "Gib mir mal ganz konkrete Beispiele.",
  ["Den Download-Ordner nach Art und Datum sortieren. Einen Stapel Belegfotos in eine fertige Abrechnung verwandeln.",
   "Dateien einheitlich umbenennen. Aus Notizen einen Bericht bauen. Vor einem Termin alles Wichtige zusammentragen."],
  breit(human("happy",0.78), bean("right",0.78),
    f'''<div class="mini-row">
{chip("Download-Ordner sortieren","blue")}{chip("Belege &#8594; Abrechnung","green")}</div>''',
    f'''<div class="mini-row">
{chip("Dateien umbenennen","orange",sub="2026-08-13-Rechnung.pdf")}{chip("Notizen &#8594; Bericht","red")}</div>''',
    f'''<div class="mini-row">
{chip("Termin vorbereiten","blue")}{chip("Recherche zusammenfassen","green")}{chip("Bericht jede Woche","orange")}</div>'''))

# --- Unteraufgaben ---
panel("Unteraufgaben",
  "Große Aufgaben dauern dann ewig, oder?",
  ["Nicht unbedingt. Claude teilt große Arbeit in kleinere Stücke auf und lässt mehrere Helfer gleichzeitig laufen.",
   "Jeder erledigt seinen Teil, am Ende wird alles zusammengeführt."],
  breit(human("think",0.78), bean("point",0.78),
    f'''{chip("Deine große Aufgabe","blue",big=True)}''',
    AD,
    f'''<div class="mini-row">{chip("Helfer 1","green",sub="liest die Unterlagen")}{chip("Helfer 2","orange",sub="sucht die Zahlen")}{chip("Helfer 3","red",sub="prüft nach")}</div>''',
    AD,
    f'''{chip("ein fertiges Ergebnis","green",big=True)}'''))

# --- Laeuft weiter ---
panel("Läuft weiter",
  "Muss ich dabei sitzen bleiben?",
  ["Nein. Du kannst den Laptop zuklappen – die Aufgabe läuft weiter.",
   "Und Du kannst dieselbe Sitzung später woanders wieder aufmachen: am Rechner, im Browser oder am Handy."],
  breit(human("happy",0.78), bean("thumbs",0.78),
    f'''<div class="chain">{chip("Du startest","blue")}{AR}{chip("Laptop zu","orange")}{AR}{chip("Claude arbeitet weiter","green")}{AR}{chip("Du kommst zurück","blue")}</div>''',
    AD,
    f'''<div class="mini-row">{chip("Desktop-App","blue")}{chip("Browser","green")}{chip("Handy","orange")}</div>''',
    '<div class="cap">dieselbe Sitzung, egal wo Du sie aufmachst</div>'))

# --- Dispatch ---
panel("Dispatch",
  "Du sagst Handy – kann ich auch von unterwegs etwas&nbsp;anstoßen?",
  ["Dafür gibt es <b>Dispatch</b>. Dein Handy wird zur Fernbedienung für den Claude, der zu Hause auf Deinem Rechner sitzt.",
   "In der Handy-App auf Cowork gehen, in der Seitenleiste <b>Dispatch</b> antippen, Aufgabe hinschreiben. Du bekommst eine Mitteilung, wenn es fertig ist – oder wenn Claude etwas von Dir wissen will."],
  breit(human("point",0.78), bean("right",0.78),
    f'''<div class="chain">{chip("Unterwegs","blue")}{AR}{chip("Auftrag tippen","green")}{AR}{chip("Rechner arbeitet","orange")}{AR}{chip("Mitteilung zurück","blue")}</div>''',
    f'''<div class="saybox c-green"><div class="say-label">Zum Beispiel unterwegs getippt:</div>
<div class="say-text">„Zieh die Zahlen aus der Quartalstabelle und leg mir eine Zusammenfassung auf den Schreibtisch.“</div></div>''',
    f'''<div class="mini-row">{chip("Rechner muss wach sein","red",sub="und die Claude-App offen")}{chip("Ein Gespräch","green",sub="Handy und Rechner, ohne Bruch")}</div>'''))

# --- Projekte ---
panel("Projekte",
  "Kann ich das irgendwie ordnen?",
  ["Ja, mit Projekten. Jedes Projekt ist ein eigener Arbeitsbereich mit eigenen Dateien und eigenen Anweisungen.",
   "Claude merkt sich darin auch, was es beim letzten Mal gelernt hat – Du fängst nicht jedes Mal von vorn an."],
  breit(human("think",0.78), bean("right",0.78),
    f'''<div style="display:flex; gap:16px; width:100%; justify-content:center">
<div class="window" style="min-width:0; flex:0 1 300px"><div class="win-title">Steuer 2026</div>
<div class="win-stack">{chip("eigene Dateien","blue")}{chip("eigene Anweisungen","green")}{chip("eigenes Gedächtnis","orange")}</div></div>
<div class="window" style="min-width:0; flex:0 1 300px"><div class="win-title">Verein</div>
<div class="win-stack">{chip("eigene Dateien","blue")}{chip("eigene Anweisungen","green")}{chip("eigenes Gedächtnis","orange")}</div></div>
</div>''',
    '<div class="cap c-blue">getrennte Arbeitsbereiche – nichts vermischt sich</div>'))

# --- Verbindungen ---
panel("Verbindungen",
  "Kommt es auch an meine anderen Programme?",
  ["Wenn Du es verbindest, ja. Google Drive, Slack und andere Dienste hängst Du unter <b>Customize</b> in der Seitenleiste an.",
   "Danach holt Claude sich die Sachen selbst – Du kopierst nichts mehr hin und her."],
  breit(human("point",0.78), bean("right",0.78),
    f'''<div class="mini-row">{chip("Google Drive","blue")}{chip("Slack","green")}{chip("weitere Dienste","orange")}</div>''',
    AD,
    f'''{chip("COWORK","green",big=True)}''',
    AD,
    f'''{doc("Dein fertiges Ergebnis","blue",2)}'''))

# --- Skills ---
panel("Skills",
  "Ich hab von „Skills“ gehört. Brauch ich die?",
  ["Erst mal nicht. Ein Skill ist ein gespeicherter Ablauf für etwas, das Du immer wieder gleich brauchst.",
   "Fertige Pakete gibt es für ganze Berufsfelder. Auch die schaltest Du unter <b>Customize</b> dazu."],
  breit(human("think",0.78), bean("right",0.78),
    f'''<div class="mini-row">{doc("Deine Anweisung","blue",2)}{doc("Dein Ablauf","orange",2)}{doc("Dein Beispiel","green",2)}</div>''',
    AD,
    f'''{chip("SKILL","blue",big=True)}''',
    AD,
    f'''<div class="mini-row">{chip("einmal einrichten","blue")}{chip("immer wieder aufrufen","green")}</div>'''))

# --- Chrome ---
panel("Im Browser",
  "Und was ist, wenn etwas nur auf einer Webseite geht?",
  ["Dann kann Claude den Browser mitbenutzen: klicken, tippen, Formulare ausfüllen.",
   "Das ist praktisch – aber genau da wäre ich vorsichtig. Für Bank, Arzt und alles Persönliche lieber nicht."],
  breit(human("think",0.78), bean("hips",0.78),
    f'''<div class="mini-row">{chip("Seite öffnen","blue")}{AR}{chip("klicken","green")}{AR}{chip("ausfüllen","orange")}{AR}{chip("Ergebnis holen","blue")}</div>''',
    AD,
    f'''<div class="mini-row">
{chip("Gut geeignet","green",sub="öffentliche Seiten, Recherche")}
{chip("Lieber nicht","red",sub="Bank, Gesundheit, Privates")}</div>'''))

# --- Berechtigungen ---
panel("Berechtigungen",
  "Darf es dann einfach alles machen?",
  ["Du entscheidest, wie weit die Leine ist. Es gibt drei Stufen.",
   "Für heikle Sachen nimmst Du <b>Manuell</b>. Die unterste Stufe schaltet <i>alle</i> Kontrollen ab – die würde ich nur nehmen, wenn Du genau weißt, warum."],
  breit(human("confused",0.78), bean("hips",0.78),
    f'''<div class="ladder">
<div class="rung c-blue"><b>Manuell</b><span>fragt vor jedem Schritt – für alles Heikle</span></div>
<div class="rung c-green"><b>Automatisch</b><span>arbeitet durch, prüft sich dabei selbst auf Sicherheit</span></div>
<div class="rung c-red"><b>Ohne Rückfrage</b><span>fragt nie, nichts prüft mit – nur mit gutem Grund</span></div>
</div>''',
    '<div class="cap c-green">Endgültig löschen darf Claude nie ohne Dein ausdrückliches Ja – in jeder Stufe</div>'))

# --- Nach Zeitplan ---
panel("Nach Zeitplan",
  "Kann es auch regelmäßig von allein laufen?",
  ["Ja. Unter <b>Scheduled</b> in der Seitenleiste legst Du wiederkehrende Aufgaben an – jeden Montag der Bericht, jeden Morgen die Zusammenfassung.",
   "Fang mit etwas Harmlosem an. Und schau ab und zu nach, was dabei herauskommt."],
  breit(human("think",0.78), bean("point",0.78),
    f'''{chip("Jeden Montag: Wochenbericht aus dem Projektordner","blue",big=True)}''',
    AD,
    f'''<div class="chain">{chip("läuft von allein","green")}{AR}{chip("Ergebnis liegt da","blue")}{AR}{chip("Du schaust drüber","orange")}</div>''',
    '<div class="cap c-orange">mit kleinen, ungefährlichen Aufgaben anfangen</div>'))

# --- Wo laeuft das ---
panel("Wo es läuft",
  "Läuft das alles auf meinem Rechner?",
  ["Nein – die eigentliche Arbeit passiert abgeschottet auf den Servern von Anthropic. An Dein Heimnetz kommt sie nicht heran.",
   "Aber Vorsicht bei der Denkweise: Das schützt Deinen Rechner. Es begrenzt <b>nicht</b>, was Claude mit dem anfangen kann, was Du ihm freigegeben hast."],
  breit(human("think",0.78), bean("right",0.78),
    f'''<div class="stage-wide" style="width:100%">
<div class="half"><div class="half-title t-green">Geschützt</div>
{chip("Dein Rechner","green")}{chip("Dein Heimnetz","green")}
<div class="cap c-green">da kommt sie nicht heran</div></div>
<div class="divider"></div>
<div class="half"><div class="half-title t-red">Trotzdem offen</div>
{chip("freigegebene Ordner","red")}{chip("verbundene Dienste","red")}
<div class="cap c-red">was Du freigibst, ist freigegeben</div></div></div>'''))

# --- Untergeschobene Anweisungen ---
panel("Fremde Anweisungen",
  "Gibt es etwas, das wirklich schiefgehen kann?",
  ["Der wichtigste Fall: In einer Webseite, einer Mail oder einem Dokument stecken versteckte Anweisungen – und Claude liest sie mit, während es Deine Aufgabe erledigt.",
   "Deshalb: nur Quellen einbeziehen, denen Du traust. Und bei Fremdem lieber die Stufe <b>Manuell</b>."],
  breit(human("confused",0.78), bean("hips",0.78),
    f'''<div class="chain">{chip("fremde Webseite","red")}{AR}{chip("versteckte Anweisung","red")}{AR}{chip("Claude liest mit","orange")}</div>''',
    AD,
    f'''<div class="mini-row">
{chip("Quellen prüfen","green",sub="nur was Du kennst")}
{chip("Manuell schalten","blue",sub="bei allem Fremden")}
{chip("Ergebnis ansehen","orange",sub="nicht blind vertrauen")}</div>'''))

# --- Sicherheitsregeln ---
panel("Sicher arbeiten",
  "Was soll ich mir merken, damit nichts passiert?",
  ["Einen eigenen Arbeitsordner anlegen statt alles freizugeben. Sicherungskopien behalten. Und Finanzunterlagen, Zugangsdaten und Persönliches draußen lassen.",
   "Du musst nicht jeden Schritt prüfen – aber schau, ob das Ganze plausibel aussieht."],
  breit(human("point",0.78), bean("point",0.78),
    f'''<div class="ladder">
<div class="rung c-green"><b>Eigener Ordner</b><span>nur das freigeben, was für die Aufgabe nötig ist</span></div>
<div class="rung c-blue"><b>Sicherungskopie</b><span>von allem, was wehtut, wenn es weg ist</span></div>
<div class="rung c-orange"><b>Klein anfangen</b><span>erst harmlose Aufgaben, dann die wichtigen</span></div>
<div class="rung c-red"><b>Draußen lassen</b><span>Finanzen, Zugangsdaten, Gesundheit, Privates</span></div>
</div>'''))

# --- Cowork oder Code ---
panel("Die drei Stufen",
  "Und wann nehme ich das andere – Claude Code?",
  ["Das hängt daran, wie weit Du Claude an Deine Sachen lässt. Cowork ist die mittlere Stufe: Deine Ordner, sonst nichts.",
   "Claude Code darf auf den ganzen Rechner. Dafür kannst Du ihm eigene Werkzeuge beibringen – und es läuft auch weiter, wenn Du nicht dabei bist."],
  breit(human("think",0.78), bean("point",0.78),
    f'''<div class="ladder">
<div class="rung c-blue"><b>1 · Im Gespräch</b><span>nichts einzurichten – Du lädst hoch, Du lädst herunter</span></div>
<div class="rung c-green"><b>2 · Cowork</b><span>hier bist Du: Claude arbeitet in Deinen Ordnern</span></div>
<div class="rung c-orange"><b>3 · Claude Code</b><span>Terminal: der ganze Rechner, eigene Werkzeuge, läuft ohne Dich</span></div>
</div>''',
    '<div class="cap c-blue">für Stufe 1 und 3 gibt es je ein eigenes Heft</div>'))

# --- Wo bekomme ich es ---
panel("Wo es das gibt",
  "Und wo finde ich das jetzt?",
  ["In der Claude-App – als Umschalter direkt neben dem Chat. Am Rechner für Windows und Mac, dazu im Browser und am Handy.",
   "Es gehört zu den bezahlten Zugängen. Wenn Du schon einen hast, ist es einfach da."],
  breit(human("happy",0.78), bean("thumbs",0.78),
    f'''<div class="tabs"><div class="tab">Chat</div><div class="tab on">Cowork</div></div>''',
    f'''<div class="mini-row">{chip("Windows","blue")}{chip("Mac","blue")}{chip("Browser","green")}{chip("Handy","orange")}</div>''',
    '<div class="cap">in den bezahlten Zugängen enthalten – Stand August 2026</div>'))

# --- Fazit ---
panel("Fazit",
  "Das klingt machbar. Ich probier&#8217;s aus.",
  ["Genau richtig. Fang mit dem Download-Ordner an."],
  f'''<div class="finale">
<div class="fin-figs">{human("happy")}<div class="bulb">&#128161;</div>{bean("thumbs")}</div>
<div class="fin-box">
<div class="fin-line"><b>Umschalten</b> &#8211; im Eingabefeld von Chat auf Cowork</div>
<div class="fin-line"><b>Beschreiben</b> &#8211; sag, was herauskommen soll, nicht wie</div>
<div class="fin-line"><b>Plan ansehen</b> &#8211; Claude zeigt erst, was es vorhat</div>
<div class="fin-line"><b>Ordner freigeben</b> &#8211; nur den, um den es geht</div>
<div class="fin-line"><b>Ergebnis</b> &#8211; fertige Tabellen, Folien, Dokumente</div>
<div class="fin-line"><b>Dispatch</b> &#8211; vom Handy aus anstoßen, Rechner muss wach sein</div>
<div class="fin-line"><b>Projekte</b> &#8211; getrennte Arbeitsbereiche mit Gedächtnis</div>
<div class="fin-line"><b>Verbindungen</b> &#8211; Drive, Slack und mehr unter „Customize“</div>
<div class="fin-line"><b>Berechtigungen</b> &#8211; drei Stufen, Du bestimmst</div>
<div class="fin-line"><b>Nach Zeitplan</b> &#8211; wiederkehrende Aufgaben unter „Scheduled“</div>
<div class="fin-line"><b>Vorsicht</b> &#8211; fremde Inhalte, Finanzen, Zugangsdaten</div>
<div class="fin-line"><b>Die drei Stufen</b> &#8211; wie weit Claude an Deine Sachen darf</div>
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
<title>Claude Cowork – die Anleitung</title>
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
    out = HERE / "cowork-anleitung.html"
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
    en = en.replace("<title>Claude Cowork – die Anleitung</title>",
                    f"<title>{texte_en.TITEL}</title>", 1)
    out = HERE / "cowork-comic-en.html"
    out.write_text(en, encoding="utf-8")
    print(f"geschrieben: {out}  ({len(en)/1024:.0f} KB, {len(P)} Seiten)")
