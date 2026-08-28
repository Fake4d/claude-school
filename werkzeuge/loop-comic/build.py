#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut das Loop-Engineering-Special als HTML (danach -> PDF). Kurzes Bonusheft
zur claude-anleitung, kein Teil der drei-Stufen-Leiter.

Erzeugt beide Sprachfassungen in einem Lauf: die deutsche direkt, die englische,
indem die fertige Seite durch i18n.uebersetze() mit dem Wörterbuch aus
texte_en.py läuft.

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
    return ('<div class="scene-col"><div class="figrow">' + links + rechts + '</div>'
            '<div class="wide">' + "".join(diagramm) + '</div></div>')

AR = '<div class="arw">&#8594;</div>'
AD = '<div class="arw">&#8595;</div>'

# ------------------------------------------------------------------ Inhalt ---

P = []
def panel(title, q, a, scene, num=True):
    P.append(dict(title=title, q=q, a=a, scene=scene, num=num))

# --- 1: Titel ---
panel(
    "Titel",
    None, None,
    f'''<div class="cover">
<div class="cover-bubbles">
  <div class="bubble b-tail-l" style="max-width:560px">Ich hab jetzt kapiert, was <code>/loop</code>&nbsp;macht.</div>
  <div class="bubble b-tail-l" style="max-width:600px;margin-left:60px">Aber Boris lässt Claude damit ja seine <b>ganze</b> App&nbsp;warten&nbsp;&#8211; wie&nbsp;geht&nbsp;das?</div>
</div>
<div class="cover-stage">
  {human("confused")}
  <div class="cloud">
    <span class="q">?</span>
    {chip("Auto-Pacing","blue")}{chip("Crash-Fuzzer","red")}{chip("Verifikation","green")}
    {chip("Worktrees","orange")}{chip("Tuning","blue")}{chip("Dup-Unifier","red")}
    {chip("Routinen-Werkstatt","orange")}
  </div>
  <div class="right-of-stage">
    <div class="bubble b-tail-r">Das nennt man <b>Loop&nbsp;Engineering</b>. Komm&#8217;, ich zeig&#8217;s&nbsp;dir.</div>
    {bean("point")}
  </div>
</div></div>''',
    num=False)

# --- 2 ---
panel("Mehr als /loop",
  "Moment &#8211; <code>/loop</code> kenn ich doch schon. Was soll <b>Loop&nbsp;Engineering</b> dann&nbsp;sein?",
  ["<code>/loop</code> ist nur der Baustein: eine Schleife, die einen Auftrag wiederholt.",
   "Loop Engineering ist das Handwerk drumherum &#8211; dafür sorgen, dass die Schleife <b>tagelang unbeaufsichtigt</b> laufen darf, ohne Schaden anzurichten."],
  f'''{human("think")}
<div class="stage-mid">{chip("/loop","blue",big=True)}
<div class="cap">der Baustein</div>
{AD}
{chip("Auto-Pacing + Verifikation + Tuning + Isolation","green",big=True)}
<div class="cap c-green">das Handwerk drumherum</div></div>
{bean("right")}''')

# --- 3 ---
panel("Ein Beispiel",
  "Gib mir mal ein Beispiel, wie das konkret&nbsp;aussieht.",
  ["Boris Cherny lässt in einem Slack-Kanal mehrere Routinen täglich über die eigenen Apps&nbsp;laufen.",
   "Ein Crash-Fuzzer tippt in der App herum und behebt Abstürze, ein Dup-Unifier findet doppelten Code, ein Dead-Code-Entferner räumt auf &#8211; jede Routine mit ihrem eigenen Auftrag."],
  breit(human("point",0.78), bean("thumbs",0.78),
    f'''<div class="mini-row">
{chip("Crash-Fuzzer","red")}{chip("Dup-Unifier","orange")}{chip("Dead-Code-Entferner","green")}{chip("Abstraktions-Polizei","blue")}</div>''',
    AD,
    f'''{chip("388 Pull Requests in wenigen Wochen","blue",big=True)}''',
    f'''<div class="cap c-green">180 davon nach Code-Review + Mensch gemerged</div>'''))

# --- 4 ---
panel("Selbst-Pacing",
  "Muss ich der Schleife jedes Mal sagen, wie oft sie&nbsp;laufen&nbsp;soll?",
  ["Nicht zwingend. Ohne Zeitangabe wählt Claude den Abstand&nbsp;selbst.",
   "Kurz, solange sich gerade etwas tut &#8211; länger, wenn Ruhe ist. Genau das macht tagelanges Weiterlaufen erst praktikabel: niemand muss ständig ein Intervall nachjustieren."],
  breit(human("think",0.78), bean("point",0.78),
    f'''<div class="mini-row">
{chip("viel los","orange",sub="kurzer Abstand")}
{chip("Ruhephase","green",sub="langer Abstand")}
{chip("blockiert","red",sub="Fallback-Weckruf")}</div>''',
    '<div class="rewind">&#8635; &#8635; &#8635;</div>',
    '<div class="cap">Claude wählt selbst, wann der nächste Durchlauf sich lohnt</div>'))

# --- 5 ---
panel("Verifikation",
  "Und wenn dabei niemand zuschaut &#8211; wie soll ich der Schleife dann&nbsp;trauen?",
  ["Genau da steht oder fällt Loop Engineering: die Schleife muss ihre eigene Arbeit <b>selbst</b> prüfen können, end&#8209;to&#8209;end.",
   "Tests laufen lassen, ein zweites Modell gegenlesen &#8211; automatisches Code-Review und Sicherheits-Review &#8211; und erst danach den Vorschlag als Pull Request&nbsp;anbieten."],
  breit(human("confused",0.76), bean("hips",0.76),
    f'''<div class="chain">{chip("Änderung","blue")}{AR}{chip("Tests","green")}{AR}{chip("Code-Review","orange")}{AR}{chip("Sicherheits-Review","red")}{AR}{chip("Pull Request","blue")}</div>''',
    '<div class="cap c-red">fällt eine Prüfung durch, gibt es keinen Vorschlag &#8211; kein Mensch muss vorher draufschauen</div>'))

# --- 6 ---
panel("Tuning",
  "Und wenn die Schleife am Anfang noch Mist&nbsp;baut?",
  ["Dann justierst du die Routine nach &#8211; oder bittest Claude direkt darum, sie selbst zu&nbsp;verbessern.",
   "Manchmal reicht ein Tag, manchmal braucht es mehrere Anläufe, bis der Ablauf zuverlässig sitzt. Das ist eingeplant, kein Fehlschlag."],
  breit(human("think",0.76), bean("point",0.76),
    f'''<div class="chain">{chip("Tag 1","red",sub="trifft oft daneben")}{AR}{chip("Routine schärfen","orange")}{AR}{chip("Tag 2","blue",sub="schon besser")}{AR}{chip("Tag 3+","green",sub="sitzt zuverlässig")}</div>''',
    '<div class="cap">Claude bekommt Rückmeldung und tunt den eigenen Ablauf nach</div>'))

# --- 7 ---
panel("Isolation",
  "Laufen da nicht mehrere Schleifen im selben Ordner&nbsp;durcheinander?",
  ["Nein &#8211; jede Routine arbeitet in ihrer eigenen Arbeitskopie, einem <b>Worktree</b>.",
   "So stören sich parallele Läufe nicht gegenseitig, und ein missratener Versuch reißt nicht den Hauptstand mit&nbsp;runter."],
  breit(human("point",0.78), bean("right",0.78),
    f'''{chip("Hauptprojekt","blue",big=True)}
<div class="mini-row">{AR}{AR}{AR}</div>
<div class="mini-row">{doc("Worktree A","red",2)}{doc("Worktree B","orange",2)}{doc("Worktree C","green",2)}</div>
<div class="cap">jede Schleife für sich, nichts überschreibt sich gegenseitig</div>'''))

# --- 8 ---
panel("Die Leiter",
  "Wann lohnt sich das ganze Handwerk dann &#8211; reicht <code>/loop</code> nicht&nbsp;meistens?",
  ["Für einen einzelnen Nachmittag reicht <code>/loop</code> tatsächlich völlig.",
   "Loop Engineering lohnt sich, sobald mehrere solcher Routinen dauerhaft nebeneinander laufen sollen &#8211; dann wird aus einzelnen Schleifen eine kleine Werkstatt, die sich selbst instand&nbsp;hält."],
  f'''<div class="stage-wide">
<div class="half"><div class="half-title">/loop</div>
{chip("eine Schleife","blue")}{chip("für heute Nachmittag","blue")}
<div class="cap c-blue">reicht meistens</div></div>
<div class="divider"></div>
<div class="half"><div class="half-title t-green">Loop Engineering</div>
{chip("mehrere abgestimmte Routinen","green")}{chip("mit Verifikation, Tuning, Isolation","green")}
<div class="cap c-green">für Dauerbetrieb</div></div></div>''')

# --- 9: Fazit ---
panel("Fazit",
  "Jetzt macht der Slack-Kanal von Boris endlich&nbsp;Sinn.",
  ["Genau darum geht's."],
  f'''<div class="finale">
<div class="fin-figs">{human("happy")}<div class="bulb">&#128161;</div>{bean("thumbs")}</div>
<div class="fin-box">
<div class="fin-line"><b>/loop</b> &#8211; der Baustein, wiederholt einen Auftrag</div>
<div class="fin-line"><b>Auto-Pacing</b> &#8211; Claude wählt den Abstand selbst</div>
<div class="fin-line"><b>Verifikation</b> &#8211; Tests, Review, erst dann ein Vorschlag</div>
<div class="fin-line"><b>Tuning</b> &#8211; ein paar Tage, bis die Routine sitzt</div>
<div class="fin-line"><b>Worktree-Isolation</b> &#8211; jede Schleife für sich</div>
<div class="fin-line"><b>Loop Engineering</b> &#8211; mehrere davon als Werkstatt im Dauerbetrieb</div>
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
<title>Loop Engineering</title>
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

.cover {{ display:flex; flex-direction:column; height:100%; }}
.cover-bubbles {{ display:flex; flex-direction:column; gap:22px; margin-bottom:7mm; }}
.cover-bubbles .bubble {{ font-size:29px; }}
.cover-stage {{ flex:1; display:flex; align-items:center; justify-content:space-between; }}
.cover-stage .fig {{ height:236px; }}
.cloud {{ flex:1; display:flex; flex-wrap:wrap; gap:10px; justify-content:center;
  align-items:center; padding:0 8px; position:relative; }}
.cloud .chip:nth-child(2n) {{ transform:rotate(-4deg); }}
.cloud .chip:nth-child(3n) {{ transform:rotate(3deg); }}
.cloud .q {{ font-size:74px; color:#1a3a8f; }}
.cloud .chip {{ font-size:22px; padding:7px 15px 9px; }}
.right-of-stage {{ display:flex; flex-direction:column; align-items:center; gap:10px; }}
.right-of-stage .bubble {{ font-size:23px; max-width:230px; }}

.half {{ flex:1; display:flex; flex-direction:column; align-items:center;
  justify-content:center; gap:12px; }}
.half-title {{ font-size:27px; border:3px solid currentColor; border-radius:8px; padding:4px 14px 6px; }}
.divider {{ width:0; border-left:3px dashed #999; }}
.rewind {{ font-size:36px; color:#2a7a3a; letter-spacing:8px;
  font-family:'DejaVu Sans', sans-serif; }}
.scene-col {{ flex:1; align-self:stretch; display:flex; flex-direction:column;
  width:100%; gap:4px; }}
.figrow {{ display:flex; justify-content:space-between; align-items:flex-end; width:100%; }}
.wide {{ flex:1; display:flex; flex-direction:column; align-items:center;
  justify-content:center; gap:13px; width:100%; }}
.chain {{ display:flex; align-items:center; gap:5px; flex-wrap:nowrap; }}
.chain .chip {{ font-size:18px; padding:5px 9px 7px; white-space:nowrap; }}
.chain .arw {{ font-size:24px; }}

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
    out = HERE / "loop-anleitung.html"
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
    en = en.replace("<title>Loop Engineering</title>",
                    f"<title>{texte_en.TITEL}</title>", 1)
    out = HERE / "loop-comic-en.html"
    out.write_text(en, encoding="utf-8")
    print(f"geschrieben: {out}  ({len(en)/1024:.0f} KB, {len(P)} Seiten)")
