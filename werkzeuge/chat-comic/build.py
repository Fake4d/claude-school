#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die Comic-Anleitung „Claude im Gespräch" als HTML (danach -> PDF).

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
  <div class="bubble b-tail-l" style="max-width:560px">Alle reden davon, was Claude alles&nbsp;kann.</div>
  <div class="bubble b-tail-l" style="max-width:540px;margin-left:60px">Ich seh nur ein leeres&nbsp;Textfeld.</div>
</div>
<div class="cover-stage">
  {human("confused")}
  <div class="cloud">
    <span class="q">?</span>
    {chip("Artifacts","blue")}{chip("Projekte","green")}{chip("Gedächtnis","orange")}
    {chip("Research","red")}{chip("Verbindungen","blue")}{chip("Stile","green")}
    {chip("Dateien","orange")}{chip("Sprachmodus","red")}{chip("Modelle","blue")}
    {chip("Incognito","green")}{chip("Websuche","orange")}{chip("Deine Daten","blue")}
  </div>
  <div class="right-of-stage">
    <div class="bubble b-tail-r">Fang einfach an.</div>
    {bean("point")}
  </div>
</div></div>''',
    num=False)

# --- 1 Was das ist ---
panel("Was das ist",
  "Was ist Claude denn nun – eine Suchmaschine?",
  ["Nein. Eine Suchmaschine gibt Dir Fundstellen. Claude gibt Dir ein <b>Ergebnis</b>.",
   "Du beschreibst, was Du brauchst – Claude denkt nach, sucht bei Bedarf nach, rechnet, schreibt und baut Dir das Fertige hin."],
  breit(human("think",0.78), bean("right",0.78),
    f'''<div class="stage-wide">
<div class="half"><div class="half-title">Suchmaschine</div>
{chip("Deine Frage","blue")}{AD}{chip("10 blaue Links","blue")}
<div class="cap">Du liest und baust selbst</div></div>
<div class="divider"></div>
<div class="half"><div class="half-title t-green">Claude</div>
{chip("Dein Ziel","green")}{AD}{chip("Das fertige Ergebnis","green")}
<div class="cap c-green">Text, Tabelle, Auswertung, Entwurf</div></div></div>'''))

# --- 2 Wie man anfaengt ---
panel("Anfangen",
  "Und was muss ich dafür installieren?",
  ["Gar nichts. Browser auf, anmelden, lostippen. Es gibt Claude auch als App für den Rechner und fürs Handy – aber nötig ist keine davon.",
   "Und Du musst nicht lernen, wie man <i>richtig</i> fragt. Schreib es so hin, wie Du es einem Kollegen sagen würdest."],
  breit(human("point",0.78), bean("right",0.78),
    f'''<div class="mini-row">{chip("Browser","blue")}{chip("Desktop-App","green")}{chip("Handy","orange")}</div>''',
    AD,
    f'''<div class="saybox c-blue"><div class="say-label">Reicht als erste Nachricht:</div>
<div class="say-text">„Ich hab hier drei Angebote für eine neue Heizung. Sag mir, worin sie sich unterscheiden und worauf ich achten muss.“</div></div>''',
    '<div class="cap c-green">nichts einzurichten, nichts zu lernen</div>'))

# --- 3 Dateien hineingeben ---
panel("Dateien hineingeben",
  "Kann ich ihm auch meine eigenen Unterlagen&nbsp;geben?",
  ["Ja – zieh sie einfach ins Gespräch. PDFs, Fotos, Tabellen, Textdateien.",
   "Claude liest sie und arbeitet damit weiter: zusammenfassen, vergleichen, Zahlen herausziehen, Fragen dazu beantworten."],
  breit(human("think",0.78), bean("right",0.78),
    f'''<div class="mini-row">{doc("Angebot.pdf","red",2)}{doc("Foto.jpg","blue",2)}{doc("Liste.xlsx","green",2)}{doc("Notizen.txt","orange",2)}</div>''',
    AD,
    f'''{machine("Claude", 146)}''',
    AD,
    f'''<div class="mini-row">{chip("Zusammenfassung","blue")}{chip("Vergleich","green")}{chip("die Zahlen daraus","orange")}</div>'''))

# --- 4 Artifacts ---
panel("Artifacts",
  "Manchmal klappt rechts so ein Fenster auf. Was ist&nbsp;das?",
  ["Das ist ein <b>Artifact</b>. Wenn das Ergebnis kein Satz mehr ist, sondern ein Ding, legt Claude es daneben statt mitten ins Gespräch.",
   "Ein Dokument, eine Übersicht, ein Schaubild – oder eine kleine Anwendung, die wirklich läuft."],
  breit(human("think",0.78), bean("point",0.78),
    f'''<div class="stage-wide">
<div class="half"><div class="half-title">Im Gespräch</div>
{chip("Antwort","blue")}{chip("Erklärung","blue")}{chip("Rückfrage","blue")}
<div class="cap">zum Lesen</div></div>
<div class="divider"></div>
<div class="half"><div class="half-title t-green">Als Artifact</div>
{chip("Dokument","green")}{chip("Schaubild","green")}{chip("Kleine Anwendung","green")}
<div class="cap c-green">zum Benutzen und Behalten</div></div></div>'''))

# --- 5 Artifacts bearbeiten ---
panel("Artifacts ändern",
  "Und wenn mir etwas daran nicht passt?",
  ["Sagen, was anders soll – Claude baut es um. Text kannst Du auch direkt anfassen: markieren und ändern lassen.",
   "Jede Fassung bleibt erhalten, Du kannst zurückblättern. Herunterladen geht, und veröffentlichen auch: dann bekommst Du einen Link zum Weitergeben."],
  breit(human("point",0.78), bean("right",0.78),
    f'''<div class="chain">{chip("Fassung 1","blue")}{AR}{chip("Fassung 2","blue")}{AR}{chip("Fassung 3","green")}</div>''',
    AD,
    f'''<div class="mini-row">{chip("Herunterladen","orange",sub="liegt bei Dir")}{chip("Veröffentlichen","green",sub="Link zum Teilen")}</div>''',
    '<div class="cap">nichts geht verloren – Du kannst jederzeit zurück</div>'))

# --- 6 Echte Dateien ---
panel("Echte Dateien",
  "Bekomme ich auch eine richtige Excel-Datei?",
  ["Ja. Claude kann echte Dateien bauen – Tabellen mit funktionierenden Formeln, Präsentationen, Dokumente, PDFs.",
   "Gebaut wird das in einem abgeschotteten Bereich bei Anthropic, nicht auf Deinem Rechner. Du lädst die fertige Datei herunter."],
  breit(human("think",0.78), bean("right",0.78),
    f'''<div class="window"><div class="win-title">Abgeschotteter Bereich</div>
<div class="mini-row">{doc("Tabelle.xlsx","green",3)}{doc("Folien.pptx","orange",3)}{doc("Bericht.docx","blue",3)}</div></div>''',
    AD,
    f'''<div class="mini-row">{chip("Du lädst sie herunter","blue")}</div>''',
    '<div class="cap c-red">an Deine eigenen Ordner kommt Claude hier noch nicht</div>'))

# --- 7 Unterhaltungen ---
panel("Unterhaltungen",
  "Soll ich alles in ein Gespräch schreiben?",
  ["Lieber nicht. Ein Gespräch hat ein Arbeitsgedächtnis, und irgendwann ist es voll – dann wird es zäh und ungenau.",
   "Faustregel: neues Thema, neues Gespräch. Beim Thema bleiben kostet nichts und macht die Antworten besser."],
  breit(human("confused",0.78), bean("hips",0.78),
    f'''<div class="stage-wide">
<div class="half"><div class="half-title t-red">Ein Gespräch für alles</div>
{chip("Urlaub","red")}{chip("Steuer","red")}{chip("Bewerbung","red")}{chip("Rezept","red")}
<div class="cap c-red">verliert den Faden</div></div>
<div class="divider"></div>
<div class="half"><div class="half-title t-green">Ein Thema, ein Gespräch</div>
{chip("Urlaub","green")}{chip("Steuer","green")}
<div class="cap c-green">bleibt scharf</div></div></div>'''))

# --- 8 Gedaechtnis ---
panel("Gedächtnis",
  "Fange ich dann jedes Mal wieder bei null&nbsp;an?",
  ["Nein. Claude merkt sich Dinge über Gespräche hinweg und kann in früheren nachsehen. Du kannst ihm auch sagen „merk Dir das“.",
   "Was gemerkt wurde, kannst Du ansehen, ändern und löschen – oder das Gedächtnis ganz abschalten. Für einmalige Sachen gibt es Incognito: taucht nirgends auf."],
  breit(human("think",0.78), bean("right",0.78),
    f'''<div class="mini-row">{doc("Was Du magst","blue",2)}{doc("Woran Du arbeitest","green",2)}{doc("Wie Du schreibst","orange",2)}</div>''',
    AD,
    f'''<div class="mini-row">{chip("Ansehen","blue")}{chip("Ändern","green")}{chip("Löschen","orange")}{chip("Ganz aus","red")}</div>''',
    '<div class="cap">Incognito: kein Verlauf, kein Gedächtnis, nichts bleibt</div>'))

# --- 9 Projekte ---
panel("Projekte",
  "Kann ich das irgendwie ordnen?",
  ["Dafür gibt es Projekte. Jedes ist ein eigener Arbeitsbereich: eigene Gespräche, eigene Unterlagen, eigene Anweisungen – und ein eigenes Gedächtnis.",
   "Einmal hinterlegt, gilt es für alles darin. Du musst nicht in jedem Gespräch neu erklären, worum es geht."],
  breit(human("point",0.78), bean("right",0.78),
    f'''<div class="stage-wide">
<div class="half"><div class="half-title">Steuer 2026</div>
{chip("Deine Belege","blue")}{chip("„Antworte knapp“","green")}{chip("eigenes Gedächtnis","orange")}</div>
<div class="divider"></div>
<div class="half"><div class="half-title">Verein</div>
{chip("Satzung","blue")}{chip("„Immer förmlich“","green")}{chip("eigenes Gedächtnis","orange")}</div></div>''',
    '<div class="cap c-blue">getrennte Arbeitsbereiche – nichts vermischt sich</div>'))

# --- 10 Websuche und Nachdenken ---
panel("Suchen und Nachdenken",
  "Weiß Claude, was gestern passiert&nbsp;ist?",
  ["Von sich aus nicht – sein Wissen hat einen Stichtag. Aber es kann nachschlagen, und dann nennt es Dir die Quellen.",
   "Zwei verschiedene Knöpfe: <b>Suchen</b> holt kurz etwas von draußen. <b>Länger nachdenken</b> holt gar nichts, sondern denkt gründlicher – gut für Knobelaufgaben."],
  breit(human("think",0.78), bean("point",0.78),
    f'''<div class="stage-wide">
<div class="half"><div class="half-title">Suchen</div>
{chip("kurz nach draußen","blue")}{chip("mit Quellenangabe","blue")}
<div class="cap">„Was kostet das gerade?“</div></div>
<div class="divider"></div>
<div class="half"><div class="half-title t-green">Länger nachdenken</div>
{chip("bleibt drinnen","green")}{chip("dafür gründlicher","green")}
<div class="cap c-green">„Wo ist der Fehler in meiner Rechnung?“</div></div></div>'''))

# --- 11 Research ---
panel("Research",
  "Und wenn ich es richtig genau wissen&nbsp;will?",
  ["Dann nimm <b>Research</b>. Claude sucht dann selbstständig weiter, folgt Spuren, prüft mehrere Quellen gegeneinander – ein bis drei Minuten lang.",
   "Am Ende steht ein Bericht mit Belegen, keine schnelle Antwort. Für Vergleiche, Marktüberblicke, Entscheidungsvorlagen."],
  breit(human("point",0.78), bean("right",0.78),
    f'''<div class="chain">{chip("Deine Frage","blue")}{AR}{chip("sucht","green")}{AR}{chip("liest","green")}{AR}{chip("prüft nach","green")}{AR}{doc("Bericht","orange",3)}</div>''',
    AD,
    f'''<div class="mini-row">{chip("dauert 1–3 Minuten","orange")}{chip("mit Quellen zum Nachschlagen","blue")}</div>''',
    '<div class="cap">für die Fragen, bei denen eine schnelle Antwort nichts taugt</div>'))

# --- 12 Verbindungen ---
panel("Verbindungen",
  "Kommt es auch an meinen Kalender und meine&nbsp;Mails?",
  ["Wenn Du es verbindest, ja. Drive, Kalender, Mail und einiges mehr hängst Du unter <b>Customize</b> an.",
   "Danach holt Claude sich die Sachen selbst. Verbinde aber nur, was Du wirklich brauchst – und was Du kennst."],
  breit(human("think",0.78), bean("right",0.78),
    f'''<div class="mini-row">{chip("Drive","blue")}{chip("Kalender","green")}{chip("Mail","orange")}{chip("Slack","red")}</div>''',
    AD,
    f'''{machine("Claude", 165)}''',
    AD,
    '<div class="cap c-red">nur anschließen, was Du brauchst – Claude sieht dann, was Du siehst</div>'))

# --- 13 Antwortstil ---
panel("Antwortstil",
  "Mir ist das immer zu&nbsp;lang.",
  ["Dann stell den Stil um. Es gibt fertige – knapp, förmlich, erklärend – und Du kannst einen eigenen bauen.",
   "Für einen eigenen gibst Du Claude einfach ein paar Zeilen, die klingen wie Du. Ab dann schreibt es so."],
  breit(human("confused",0.78), bean("point",0.78),
    f'''<div class="ladder">
<div class="rung c-blue"><b>Knapp</b><span>kommt sofort zum Punkt</span></div>
<div class="rung c-green"><b>Erklärend</b><span>nimmt Dich mit, wenn Du es lernen willst</span></div>
<div class="rung c-orange"><b>Förmlich</b><span>für alles, was nach draußen geht</span></div>
<div class="rung c-red"><b>Dein eigener</b><span>klingt wie Du – aus Deinen Beispielen gebaut</span></div>
</div>'''))

# --- 14 Handy und Sprache ---
panel("Handy und Sprache",
  "Und unterwegs?",
  ["Dasselbe Gespräch, überall: Browser, Rechner-App, Handy. Du machst es auf, wo Du gerade bist.",
   "Am Handy kannst Du auch einfach reden statt tippen. Praktisch beim Gehen – und beim Sortieren von Gedanken."],
  breit(human("happy",0.78), bean("thumbs",0.78),
    f'''<div class="mini-row">{chip("Browser","blue")}{chip("Desktop-App","green")}{chip("Handy","orange")}</div>''',
    AD,
    f'''<div class="mini-row">{chip("Tippen","blue")}{chip("oder einfach reden","green")}</div>''',
    '<div class="cap c-blue">ein Gespräch, egal wo Du es aufmachst</div>'))

# --- 15 Modelle ---
panel("Modelle",
  "Da steht oben ein Name. Muss ich den&nbsp;ändern?",
  ["Meistens nicht. Die Voreinstellung passt für fast alles.",
   "Wenn eine Aufgabe wirklich schwer ist, nimm das stärkste Modell. Wenn es nur schnell gehen soll, das kleine. Stand August 2026 heißen sie so:"],
  breit(human("think",0.78), bean("right",0.78),
    f'''<div class="models">
<div class="model c-blue"><b>Opus 5</b><span>die schweren Sachen</span><i>denkt am gründlichsten</i></div>
<div class="model c-green"><b>Sonnet 5</b><span>der Alltag</span><i>die Voreinstellung</i></div>
<div class="model c-orange"><b>Haiku 4.5</b><span>schnell &amp; günstig</span><i>für Kurzes</i></div>
</div>''',
    '<div class="cap">im Zweifel: einfach lassen</div>'))

# --- 16 Gut fragen ---
panel("Gut fragen",
  "Wie sage ich es denn am&nbsp;besten?",
  ["Sag das Ziel, nicht die Schritte – den Weg findet Claude selbst. Und sag dazu, woran man merkt, dass es fertig ist.",
   "Gib den Zusammenhang mit: für wen, wofür, und was auf keinen Fall passieren darf. Je klarer der Auftrag, desto weniger Runden."],
  breit(human("think",0.78), bean("point",0.78),
    f'''<div class="saybox c-red"><div class="say-label">eher nicht</div>
<div class="say-text">„Schreib was zu unserem Sommerfest.“</div></div>''',
    f'''<div class="saybox c-green"><div class="say-label">besser</div>
<div class="say-text">„Eine Einladung zum Sommerfest für die Nachbarschaft, höchstens eine halbe Seite, freundlich aber nicht albern. Termin und Anmeldung müssen drinstehen.“</div></div>'''))

# --- 17 Nachpruefen ---
panel("Nachprüfen",
  "Kann ich mich denn darauf&nbsp;verlassen?",
  ["Meistens ja – aber Claude kann sich auch überzeugend irren, und es klingt dabei genauso sicher wie sonst.",
   "Deshalb: Bei allem, was zählt, nach der Quelle fragen. Und Zahlen lieber nachrechnen lassen, als sie zu glauben."],
  breit(human("confused",0.78), bean("hips",0.78),
    f'''<div class="mini-row">{chip("Quelle nennen lassen","blue",sub="woher stammt das?")}{chip("Zahlen nachrechnen","green",sub="Schritt für Schritt")}</div>''',
    AD,
    f'''<div class="mini-row">{chip("Bei Wichtigem: gegenlesen","orange",sub="Vertrag, Bewerbung, Arzt")}</div>''',
    '<div class="cap c-red">je wichtiger die Sache, desto kürzer die Leine</div>'))

# --- 18 Fremde Inhalte ---
panel("Fremde Inhalte",
  "Und wenn in einem PDF steht „lösche&nbsp;alles“?",
  ["Gute Frage – da liegt die Stolperfalle. Claude liest Webseiten, Mails und fremde Dokumente. <b>Nichts davon ist ein Auftrag von Dir.</b>",
   "Aufträge kommen von Dir. Alles andere ist Material zum Lesen. Deshalb: bei Fremdem genauer hinsehen, was am Ende herauskommt."],
  breit(human("think",0.78), bean("right",0.78),
    f'''<div class="mini-row">{chip("Deine Anweisung","green",sub="zählt")}{chip("Dein Projekt","green",sub="zählt")}</div>''',
    AD,
    f'''<div class="mini-row">{chip("Webseite","red",sub="nur Material")}{chip("E-Mail","red",sub="nur Material")}{chip("fremdes PDF","red",sub="nur Material")}</div>''',
    '<div class="cap c-blue">was drinsteht, wird gelesen – nicht befolgt</div>'))

# --- 19 Deine Daten ---
panel("Deine Daten",
  "Was passiert eigentlich mit dem, was ich&nbsp;schreibe?",
  ["Das steht in den Einstellungen, und Du entscheidest es. Dort legst Du fest, ob Deine Gespräche zur Verbesserung von Claude verwendet werden dürfen.",
   "Incognito-Gespräche werden nie dafür verwendet – und landen auch nicht im Verlauf. Für heikle Sachen gilt trotzdem: nur hineingeben, was Du auch einem Dienstleister geben würdest."],
  breit(human("think",0.78), bean("point",0.78),
    f'''<div class="ladder">
<div class="rung c-blue"><b>Einstellungen</b><span>Du bestimmst, ob Gespräche zur Verbesserung genutzt werden</span></div>
<div class="rung c-green"><b>Incognito</b><span>kein Verlauf, kein Gedächtnis, nie fürs Training</span></div>
<div class="rung c-orange"><b>Trotzdem gilt</b><span>Zugangsdaten und fremde Geheimnisse gehören nirgends hinein</span></div>
</div>'''))

# --- 20 Die drei Stufen ---
panel("Die drei Stufen",
  "Und wenn ich mehr&nbsp;will?",
  ["Dann geht es in Stufen weiter – die Frage ist immer, wie weit Du Claude an Deine Sachen lässt.",
   "Hier, im Gespräch, geht alles durch Dich hindurch: Du gibst hinein, Du nimmst heraus. Das reicht für erstaunlich viel."],
  breit(human("point",0.78), bean("right",0.78),
    f'''<div class="ladder">
<div class="rung c-green"><b>1 · Im Gespräch</b><span>nichts einzurichten – Du lädst hoch, Du lädst herunter</span></div>
<div class="rung c-blue"><b>2 · Cowork</b><span>Claude arbeitet direkt in Deinen Ordnern</span></div>
<div class="rung c-orange"><b>3 · Claude Code</b><span>Terminal: Claude arbeitet auf dem ganzen Rechner – und läuft ohne Dich weiter</span></div>
</div>''',
    '<div class="cap c-blue">für Stufe 2 und 3 gibt es je ein eigenes Heft</div>'))

# --- 21 Fazit ---
panel("Fazit",
  "Ohh. Das ist ja gar nicht so&nbsp;wild.",
  ["Eben. Fang mit einer echten Aufgabe an, nicht mit einem Test."],
  f'''<div class="finale">
<div class="fin-figs">{human("happy",0.9)}<div class="bulb">💡</div>{bean("thumbs",0.9)}</div>
<div class="fin-box"><div class="fin-line">
<b>Artifacts</b> &#8211; wenn Claude etwas baut statt es zu beschreiben<br>
<b>Dateien</b> &#8211; hineinziehen, und echte Dateien zurückbekommen<br>
<b>Gespräche</b> &#8211; neues Thema, neues Gespräch<br>
<b>Gedächtnis</b> &#8211; merkt sich Dinge, Du kannst es abschalten<br>
<b>Projekte</b> &#8211; getrennte Arbeitsbereiche mit eigenen Regeln<br>
<b>Suchen &amp; Research</b> &#8211; der kurze Griff und der lange Bericht<br>
<b>Verbindungen</b> &#8211; Drive, Kalender, Mail unter „Customize“<br>
<b>Stil</b> &#8211; knapp, förmlich, erklärend oder Dein eigener<br>
<b>Gut fragen</b> &#8211; das Ziel sagen, nicht die Schritte<br>
<b>Nachprüfen</b> &#8211; überzeugend klingen heißt nicht richtig liegen<br>
<b>Fremde Inhalte</b> &#8211; werden gelesen, nicht befolgt<br>
<b>Weiter geht&#8217;s</b> &#8211; Cowork für Deine Ordner, Code für den ganzen Rechner
</div></div></div>''')
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
<title>Claude im Gespräch – die Anleitung</title>
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
    out = HERE / "chat-anleitung.html"
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
    en = en.replace("<title>Claude im Gespräch – die Anleitung</title>",
                    f"<title>{texte_en.TITEL}</title>", 1)
    out = HERE / "chat-comic-en.html"
    out.write_text(en, encoding="utf-8")
    print(f"geschrieben: {out}  ({len(en)/1024:.0f} KB, {len(P)} Seiten)")
