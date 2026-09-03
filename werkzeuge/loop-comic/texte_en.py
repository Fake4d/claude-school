# -*- coding: utf-8 -*-
"""English wording for the Loop Engineering special.

Key = the German text exactly as it ends up in the built page, value = its
English counterpart. The keys are produced by i18n.einheiten(); if the German
side changes, the build stops and prints the new key, so nothing can silently
stay German.

Keep the inline markup (<b>, <code>, <span class="chip-sub">) identical on
both sides — it carries the layout.
"""

TITEL = "Loop Engineering"

TEXTE = {

"Claude": "Claude",

# --- Titelseite ---
"Ich hab jetzt kapiert, was <code>/loop</code>&nbsp;macht.":
    "I get what <code>/loop</code>&nbsp;does now.",
"Aber Boris lässt Claude damit ja seine <b>ganze</b> App&nbsp;warten&nbsp;&#8211; wie&nbsp;geht&nbsp;das?":
    "But Boris uses it to have Claude maintain his <b>whole</b> app&nbsp;&#8211; how&nbsp;does&nbsp;that&nbsp;work?",
"Auto-Pacing": "Auto-pacing",
"Crash-Fuzzer": "Crash fuzzer",
"Verifikation": "Verification",
"Worktrees": "Worktrees",
"Tuning": "Tuning",
"Dup-Unifier": "Dup unifier",
"Routinen-Werkstatt": "Routine workshop",
"Ralph-Loop": "Ralph loop",
"Squad": "Squad",
"Harness": "Harness",
"Das nennt man <b>Loop&nbsp;Engineering</b>. Komm&#8217;, ich zeig&#8217;s&nbsp;dir.":
    "That&#8217;s called <b>Loop&nbsp;Engineering</b>. Come on, I&#8217;ll show&nbsp;you.",

# --- Mehr als /loop ---
"Moment &#8211; <code>/loop</code> kenn ich doch schon. Was soll <b>Loop&nbsp;Engineering</b> dann&nbsp;sein?":
    "Hold on &#8211; I already know <code>/loop</code>. So what is <b>Loop&nbsp;Engineering</b>&nbsp;then?",
"<code>/loop</code> ist nur der Baustein: eine Schleife, die einen Auftrag wiederholt.":
    "<code>/loop</code> is just the building block: a loop that repeats a task.",
"Loop Engineering ist das Handwerk drumherum &#8211; dafür sorgen, dass die Schleife <b>tagelang unbeaufsichtigt</b> laufen darf, ohne Schaden anzurichten.":
    "Loop Engineering is the craft around it &#8211; making sure the loop can run <b>unattended for days</b> without causing harm.",
"/loop": "/loop",
"der Baustein": "the building block",
"Auto-Pacing + Verifikation + Tuning + Isolation": "Auto-pacing + verification + tuning + isolation",
"das Handwerk drumherum": "the craft around it",

# --- Ein Beispiel ---
"Gib mir mal ein Beispiel, wie das konkret&nbsp;aussieht.":
    "Give me an example of what that looks&nbsp;like in practice.",
"Boris Cherny lässt in einem Slack-Kanal mehrere Routinen täglich über die eigenen Apps&nbsp;laufen.":
    "Boris Cherny runs several routines daily over his own apps, in a Slack&nbsp;channel.",
"Ein Crash-Fuzzer tippt in der App herum und behebt Abstürze, ein Dup-Unifier findet doppelten Code, ein Dead-Code-Entferner räumt auf &#8211; jede Routine mit ihrem eigenen Auftrag.":
    "A crash fuzzer taps around the app and fixes crashes, a dup unifier finds duplicate code, a dead-code remover cleans up &#8211; each routine with its own job.",
"Dead-Code-Entferner": "Dead-code remover",
"Abstraktions-Polizei": "Abstraction police",
"388 Pull Requests in wenigen Wochen": "388 pull requests in a few weeks",
"180 davon nach Code-Review + Mensch gemerged": "180 of them merged after code review + human review",

# --- Selbst-Pacing ---
"Muss ich der Schleife jedes Mal sagen, wie oft sie&nbsp;laufen&nbsp;soll?":
    "Do I have to tell the loop every time how often it should&nbsp;run?",
"Nicht zwingend. Ohne Zeitangabe wählt Claude den Abstand&nbsp;selbst.":
    "Not necessarily. Without a time given, Claude picks the interval&nbsp;itself.",
"Kurz, solange sich gerade etwas tut &#8211; länger, wenn Ruhe ist. Genau das macht tagelanges Weiterlaufen erst praktikabel: niemand muss ständig ein Intervall nachjustieren.":
    "Short while things are actually happening &#8211; longer during quiet stretches. That&#8217;s exactly what makes running for days practical: nobody has to keep adjusting an interval.",
"viel los<span class=\"chip-sub\">kurzer Abstand</span>":
    "busy<span class=\"chip-sub\">short interval</span>",
"Ruhephase<span class=\"chip-sub\">langer Abstand</span>":
    "quiet stretch<span class=\"chip-sub\">long interval</span>",
"blockiert<span class=\"chip-sub\">Fallback-Weckruf</span>":
    "blocked<span class=\"chip-sub\">fallback wake-up</span>",
"Claude wählt selbst, wann der nächste Durchlauf sich lohnt":
    "Claude decides for itself when the next run is worth it",

# --- Ralph-Loop ---
"Diese Schleife, die einfach immer wieder plant, macht, prüft &#8211; hat das auch einen&nbsp;Namen?":
    "This loop that just keeps planning, doing, checking &#8211; does that have a&nbsp;name&nbsp;too?",
"Ja &#8211; das nennt man einen <b>Ralph&#8209;Loop</b>: planen, ausführen, prüfen, von&nbsp;vorn.":
    "Yes &#8211; that&#8217;s called a <b>Ralph&#8209;loop</b>: plan, execute, check, from the&nbsp;top.",
"Robust, aber roh &#8211; ohne Bremse frisst er Token weiter, auch wenn er längst am&nbsp;Ziel&nbsp;ist. Genau dafür gibt's Auto-Pacing, und die Verifikation, die als Nächstes&nbsp;kommt.":
    "Robust, but crude &#8211; without a brake it keeps burning tokens even after it&#8217;s long since done. That&#8217;s exactly what auto-pacing is for, and the verification that comes&nbsp;next.",
"Planen": "Plan",
"Ausführen": "Execute",
"Prüfen": "Check",
"&#8635; von vorn, bis fertig": "&#8635; from the top, until done",
"robust, aber ohne Bremse teuer im Token-Verbrauch":
    "robust, but expensive in tokens without a brake",

# --- Verifikation ---
"Und wenn dabei niemand zuschaut &#8211; wie soll ich der Schleife dann&nbsp;trauen?":
    "But if nobody&#8217;s watching &#8211; how am I supposed to trust the&nbsp;loop?",
"Genau da steht oder fällt Loop Engineering: die Schleife muss ihre eigene Arbeit <b>selbst</b> prüfen können, end&#8209;to&#8209;end.":
    "That&#8217;s exactly where Loop Engineering stands or falls: the loop has to be able to verify its own work <b>itself</b>, end&#8209;to&#8209;end.",
"Tests laufen lassen, ein zweites Modell gegenlesen &#8211; automatisches Code-Review und Sicherheits-Review &#8211; und erst danach den Vorschlag als Pull Request&nbsp;anbieten.":
    "Run the tests, have a second model review it &#8211; automated code review and security review &#8211; and only then offer the change as a pull&nbsp;request.",
"Änderung": "Change",
"Tests": "Tests",
"Code-Review": "Code review",
"Sicherheits-Review": "Security review",
"Pull Request": "Pull request",
"fällt eine Prüfung durch, gibt es keinen Vorschlag &#8211; kein Mensch muss vorher draufschauen":
    "if a check fails, there is no proposal &#8211; no human has to look at it beforehand",

# --- Tuning ---
"Und wenn die Schleife am Anfang noch Mist&nbsp;baut?":
    "And what if the loop makes a mess of it at&nbsp;first?",
"Dann justierst du die Routine nach &#8211; oder bittest Claude direkt darum, sie selbst zu&nbsp;verbessern.":
    "Then you adjust the routine &#8211; or just ask Claude to improve it&nbsp;itself.",
"Manchmal reicht ein Tag, manchmal braucht es mehrere Anläufe, bis der Ablauf zuverlässig sitzt. Das ist eingeplant, kein Fehlschlag.":
    "Sometimes one day is enough, sometimes it takes several attempts before the routine sits reliably. That&#8217;s expected, not a failure.",
"Tag 1<span class=\"chip-sub\">trifft oft daneben</span>":
    "Day 1<span class=\"chip-sub\">often misses</span>",
"Routine schärfen": "Sharpen the routine",
"Tag 2<span class=\"chip-sub\">schon besser</span>":
    "Day 2<span class=\"chip-sub\">already better</span>",
"Tag 3+<span class=\"chip-sub\">sitzt zuverlässig</span>":
    "Day 3+<span class=\"chip-sub\">reliably solid</span>",
"Claude bekommt Rückmeldung und tunt den eigenen Ablauf nach":
    "Claude gets feedback and tunes its own routine",

# --- Hill Climbing ---
"Ist das Nachjustieren von eben auch mit der Zeit systematisch, oder rät man da nur&nbsp;rum?":
    "Is that tuning from before systematic over time, or is it just guesswork?",
"Systematisch heißt <b>Hill&nbsp;Climbing</b>: man misst die Qualität mit einer festen Prüfliste &#8211; einem&nbsp;Eval &#8211; und schraubt gezielt an der Routine.":
    "The systematic version is called <b>hill&nbsp;climbing</b>: you measure quality with a fixed checklist &#8211; an&nbsp;eval &#8211; and adjust the routine on purpose.",
"Kein Rätselraten: jede Änderung wird gegen den Eval getestet, nur was wirklich besser abschneidet bleibt&nbsp;drin.":
    "No guesswork: every change gets tested against the eval, only what actually scores better stays&nbsp;in.",
"Eval definieren": "Define eval",
"Routine anpassen": "Adjust routine",
"gegen Eval testen": "Test against eval",
"&#8599; Schritt für Schritt bergauf": "&#8599; step by step, uphill",
"nur behalten, was der Eval bestätigt &#8211; das ist Hill Climbing":
    "keep only what the eval confirms &#8211; that&#8217;s hill climbing",

# --- Isolation ---
"Laufen da nicht mehrere Schleifen im selben Ordner&nbsp;durcheinander?":
    "Don&#8217;t several loops in the same folder get in each other&#8217;s&nbsp;way?",
"Nein &#8211; jede Routine arbeitet in ihrer eigenen Arbeitskopie, einem <b>Worktree</b>.":
    "No &#8211; each routine works in its own copy of the project, a <b>worktree</b>.",
"So stören sich parallele Läufe nicht gegenseitig, und ein missratener Versuch reißt nicht den Hauptstand mit&nbsp;runter.":
    "That way parallel runs don&#8217;t interfere with each other, and a failed attempt doesn&#8217;t drag the main branch down with&nbsp;it.",
"Hauptprojekt": "Main project",
"Worktree A": "Worktree A",
"Worktree B": "Worktree B",
"Worktree C": "Worktree C",
"jede Schleife für sich, nichts überschreibt sich gegenseitig":
    "each loop on its own, nothing overwrites anything else",

# --- Squads & Fleets ---
"Die Worktrees von eben &#8211; laufen die dann alle als eigene, einzelne&nbsp;Claudes?":
    "The worktrees from before &#8211; do they each run as their own, separate&nbsp;Claude?",
"Meistens ja: jede Routine ihr eigener Claude &#8211; viele davon gleichzeitig nennt man eine <b>Fleet</b>.":
    "Mostly yes: each routine its own Claude &#8211; many of them at once is called a <b>fleet</b>.",
"Manchmal arbeiten mehrere Claudes aber auch <b>zusammen</b> an einer einzigen Aufgabe, mit verteilten Rollen &#8211; das ist ein <b>Squad</b>: einer plant, einer baut, einer&nbsp;prüft.":
    "But sometimes several Claudes work <b>together</b> on a single task, with roles split up &#8211; that&#8217;s a <b>squad</b>: one plans, one builds, one&nbsp;reviews.",
"Fleet": "Fleet",
"viele, unabhängig, parallel": "many, independent, parallel",
"Planer": "Planner",
"Bauer": "Builder",
"Prüfer": "Reviewer",
"wenige, mit verteilten Rollen, an einer Aufgabe": "a few, with split roles, on one task",

# --- Harnesses ---
"Auto-Pacing, Verifikation, Tuning, Isolation &#8211; hat dieses ganze Gerüst auch einen&nbsp;Namen?":
    "Auto-pacing, verification, tuning, isolation &#8211; does this whole scaffolding have a&nbsp;name&nbsp;too?",
"Ja &#8211; die Summe aus Werkzeugen, Rechten, Gedächtnis und Ablaufsteuerung um das Modell herum heißt <b>Harness</b>.":
    "Yes &#8211; the sum of tools, permissions, memory, and orchestration around the model is called a <b>harness</b>.",
"Loop Engineering ist genau das: einen Harness bauen, in dem Claude tagelang unbeaufsichtigt arbeiten&nbsp;darf.":
    "Loop Engineering is exactly that: building a harness Claude can work in, unattended, for&nbsp;days.",
"Werkzeuge": "Tools",
"Rechte": "Permissions",
"Gedächtnis": "Memory",
"Ablaufsteuerung": "Orchestration",
"alles zusammen: der <b>Harness</b>": "all of it together: the <b>harness</b>",

# --- Die Leiter ---
"Wann lohnt sich das ganze Handwerk dann &#8211; reicht <code>/loop</code> nicht&nbsp;meistens?":
    "So when is all this craft actually worth it &#8211; isn&#8217;t <code>/loop</code> enough most of the&nbsp;time?",
"Für einen einzelnen Nachmittag reicht <code>/loop</code> tatsächlich völlig.":
    "For a single afternoon, <code>/loop</code> really is completely enough.",
"Loop Engineering lohnt sich, sobald mehrere solcher Routinen dauerhaft nebeneinander laufen sollen &#8211; dann wird aus einzelnen Schleifen eine kleine Werkstatt, die sich selbst instand&nbsp;hält.":
    "Loop Engineering pays off once several such routines are meant to run alongside each other permanently &#8211; then individual loops turn into a small workshop that maintains&nbsp;itself.",
"eine Schleife": "one loop",
"für heute Nachmittag": "for this afternoon",
"reicht meistens": "usually enough",
"Loop Engineering": "Loop Engineering",
"mehrere abgestimmte Routinen": "several coordinated routines",
"mit Verifikation, Tuning, Isolation": "with verification, tuning, isolation",
"für Dauerbetrieb": "for permanent operation",

# --- Fazit ---
"Jetzt macht der Slack-Kanal von Boris endlich&nbsp;Sinn.":
    "Now Boris&#8217; Slack channel finally makes&nbsp;sense.",
"Genau darum geht's.": "That&#8217;s exactly the point.",
"<b>/loop</b> &#8211; der Baustein, wiederholt einen Auftrag":
    "<b>/loop</b> &#8211; the building block, repeats a task",
"<b>Ralph-Loop</b> &#8211; planen, ausführen, prüfen, von vorn":
    "<b>Ralph loop</b> &#8211; plan, execute, check, from the top",
"<b>Auto-Pacing</b> &#8211; Claude wählt den Abstand selbst":
    "<b>Auto-pacing</b> &#8211; Claude picks the interval itself",
"<b>Verifikation</b> &#8211; Tests, Review, erst dann ein Vorschlag":
    "<b>Verification</b> &#8211; tests, review, only then a proposal",
"<b>Hill Climbing</b> &#8211; Tuning mit Eval statt Rätselraten":
    "<b>Hill climbing</b> &#8211; tuning with an eval instead of guesswork",
"<b>Worktree-Isolation</b> &#8211; jede Schleife für sich":
    "<b>Worktree isolation</b> &#8211; each loop on its own",
"<b>Squad / Fleet</b> &#8211; verteilte Rollen oder viele parallel":
    "<b>Squad / fleet</b> &#8211; split roles, or many in parallel",
"<b>Harness</b> &#8211; Werkzeuge, Rechte, Gedächtnis, Ablaufsteuerung":
    "<b>Harness</b> &#8211; tools, permissions, memory, orchestration",
"<b>Loop Engineering</b> &#8211; all das als Werkstatt im Dauerbetrieb":
    "<b>Loop Engineering</b> &#8211; all of it as a workshop in permanent operation",

}
