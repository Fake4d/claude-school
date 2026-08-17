# -*- coding: utf-8 -*-
"""English wording for the Claude Code comic.

Key = the German text exactly as it ends up in the built page, value = its
English counterpart. The keys are produced by i18n.einheiten(); if the German
side changes, the build stops and prints the new key, so nothing can silently
stay German.

Keep the inline markup (<b>, <code>, <kbd>, <span class="chip-sub">) identical
on both sides — it carries the layout. Soft hyphens (&shy;) are German
line-break hints and are usually not needed in English.
"""

TEXTE = {

# --- Titelseite ---
"Alle bauen gerade krasse Sachen mit&nbsp;Claude.":
    "Everyone is building amazing things with&nbsp;Claude right now.",
"Und ich versteh&nbsp;kein&nbsp;Wort davon.":
    "And I don&#8217;t understand a&nbsp;word&nbsp;of&nbsp;it.",
"CLAUDE.md": "CLAUDE.md",
"Skills": "Skills",
"Plugins": "Plugins",
"MCP": "MCP",
"Hooks": "Hooks",
"Subagents": "Subagents",
"/Commands": "/Commands",
"Memory": "Memory",
"Checkpoints": "Checkpoints",
"Cowork": "Cowork",
"Routinen": "Routines",
"Plan-Modus": "Plan mode",
"/loop": "/loop",
"Komm, ich erklär&#8217;s dir.": "Come on, I&#8217;ll explain.",

# --- CLAUDE.md ---
"Fangen wir mit CLAUDE.md an. Warum legt die&nbsp;jeder&nbsp;an?":
    "Let&#8217;s start with CLAUDE.md. Why does&nbsp;everyone&nbsp;have one?",
"CLAUDE.md ist im Grunde eine Bedienungs&shy;anleitung, die du Claude gibst.":
    "CLAUDE.md is basically a user manual that you hand to Claude.",
"Da steht drin, wie dein Projekt funktioniert, welche Regeln gelten – und was Claude auf keinen Fall tun soll.":
    "It says how your project works, which rules apply – and what Claude must never do.",
"Projekt&shy;struktur": "Project structure",
"Regeln": "Rules",
"Verboten!": "Forbidden!",

"Ich muss also nicht in jeder Sitzung dasselbe&nbsp;erklären?":
    "So I don&#8217;t have to explain the same thing&nbsp;every&nbsp;session?",
"Genau. Claude liest die Datei automatisch, sobald du im Projekt startest.":
    "Exactly. Claude reads the file automatically as soon as you start inside the project.",
"Es gibt sogar drei Ebenen: global in <code>~/.claude/</code>, im Projekt&shy;ordner und pro Unter&shy;ordner. <code>/init</code> schreibt dir eine erste Fassung.":
    "There are even three levels: globally in <code>~/.claude/</code>, in the project folder and per subfolder. <code>/init</code> writes you a first draft.",
"Claude": "Claude",
"Nutze diesen Stil": "Use this style",
"Führe diese Tests aus": "Run these tests",
"Ordner nie ändern": "Never touch this folder",
"Claude hält sich an die Projektregeln": "Claude sticks to the project rules",

# --- Skills ---
"Okay. Und was sind dann Skills?": "Okay. So what are skills, then?",
"Ein Skill bringt Claude bei, <b>wie</b> eine bestimmte Aufgabe richtig läuft.":
    "A skill teaches Claude <b>how</b> a particular job is done properly.",
"Statt jedes Mal deinen ganzen Ablauf zu erklären, machst du daraus einen wieder&shy;verwendbaren Skill.":
    "Instead of explaining your whole procedure every time, you turn it into a reusable skill.",
"Ablauf": "Procedure",
"Notiz": "Note",
"Regel": "Rule",
"Vorlage": "Template",
"SKILL": "SKILL",

"Gib mir mal ein Beispiel.": "Give me an example.",
"Sagen wir, du willst jede Woche denselben Auswertungs&shy;bericht.":
    "Say you want the same analysis report every week.",
"Deine Anweisungen, dein Ablauf, deine Beispiele – daraus wird ein Skill, den du nur noch aufrufst.":
    "Your instructions, your procedure, your examples – that becomes a skill you simply call.",
"Deine Anweisungen": "Your instructions",
"Dein Ablauf": "Your procedure",
"Beispiele": "Examples",
"Skill: Wochen&shy;bericht": "Skill: weekly report",

"Und diese SKILL.md-Dateien, die alle von GitHub laden – das sind einfach&nbsp;Anweisungen?":
    "And those SKILL.md files everyone downloads from GitHub – they&#8217;re just&nbsp;instructions?",
"Ziemlich genau. Ein Skill ist ein Ordner mit einer <code>SKILL.md</code>, dazu Skripte, Vorlagen und Referenz&shy;dateien.":
    "Pretty much. A skill is a folder with a <code>SKILL.md</code> in it, plus scripts, templates and reference files.",
"Claude liest zuerst nur Name und Beschreibung – den Rest erst, wenn er ihn wirklich braucht. Aufrufen kannst du ihn auch selbst mit <code>/skill-name</code>.":
    "Claude first reads only the name and description – the rest only when it really needs it. You can also call it yourself with <code>/skill-name</code>.",
"SKILL.md": "SKILL.md",
"scripts/": "scripts/",
"references/": "references/",
"assets/": "assets/",
"Wieder&shy;verwendbarer Claude-Ablauf": "A reusable Claude procedure",

# --- Plugins ---
"Und Plugins? Sind das nicht auch einfach&nbsp;Skills?":
    "And plugins? Aren&#8217;t those just&nbsp;skills as well?",
"Nicht ganz. Ein Skill ist <b>eine</b> Fähigkeit.":
    "Not quite. A skill is <b>one</b> ability.",
"Ein Plugin ist eher ein <b>Paket</b>: Skills + Hooks + Subagents + MCP-Server + eigene Befehle in einem Rutsch. Installiert wird&#8217;s über einen Marktplatz mit <code>/plugin</code>.":
    "A plugin is more of a <b>bundle</b>: skills + hooks + subagents + MCP servers + custom commands in one go. You install it from a marketplace with <code>/plugin</code>.",
"PLUGIN": "PLUGIN",
"MCP-Server": "MCP servers",
"Skill": "Skill",

# --- MCP ---
"Moment – MCP-Server. Was ist das?": "Hold on – MCP servers. What are those?",
"MCP ist im Grunde die Art, wie Claude sich mit Dingen <b>außerhalb</b> von Claude verbindet.":
    "MCP is basically how Claude connects to things <b>outside</b> of Claude.",
"Ein einheitlicher Stecker für fremde Programme und Dienste.":
    "One standard plug for other people&#8217;s programs and services.",
"GitHub": "GitHub",
"Slack": "Slack",
"Daten&shy;bank": "Database",
"Drive": "Drive",
"Kalender": "Calendar",

"Ich muss also nicht mehr alles von Hand rein&shy;kopieren …":
    "So I don&#8217;t have to paste everything in by hand any more …",
"Claude verbindet sich selbst, holt sich die Information – und darf dort auch handeln, wenn du es erlaubst.":
    "Claude connects on its own, fetches the information – and may act there too, if you allow it.",
"Mit <code>/mcp</code> siehst du, was gerade verbunden ist.":
    "<code>/mcp</code> shows you what is currently connected.",
"Ohne MCP": "Without MCP",
"du kopierst alles von Hand": "you copy everything by hand",
"Mit MCP": "With MCP",
"Claude holt es sich selbst": "Claude fetches it itself",

# --- Hooks ---
"Gut. Und Hooks? Das klingt noch verwirrender.":
    "Right. And hooks? That sounds even more confusing.",
"Hooks sind anders, weil <b>nicht Claude</b> entscheidet, ob sie passieren.":
    "Hooks are different because <b>Claude doesn&#8217;t</b> decide whether they happen.",
"Sie laufen automatisch los, sobald ein bestimmtes Ereignis eintritt. Eingerichtet in <code>settings.json</code> oder über <code>/hooks</code>.":
    "They fire automatically as soon as a certain event occurs. Set up in <code>settings.json</code> or through <code>/hooks</code>.",
"Ereignis passiert": "An event happens",
"löst automatisch den Hook aus": "automatically triggers the hook",
"Hook läuft": "Hook runs",

"Zum Beispiel?": "For example?",
"Ein Hook kann nach jeder Datei&shy;änderung deinen Formatierer starten – oder Claude stoppen, <b>bevor</b> ein gefährlicher Befehl läuft.":
    "A hook can run your formatter after every file change – or stop Claude <b>before</b> a dangerous command runs.",
"Typische Ereignisse: <code>PreToolUse</code>, <code>PostToolUse</code>, <code>UserPromptSubmit</code>, <code>SessionStart</code>, <code>Stop</code>.":
    "Typical events: <code>PreToolUse</code>, <code>PostToolUse</code>, <code>UserPromptSubmit</code>, <code>SessionStart</code>, <code>Stop</code>.",
"Claude ändert eine Datei": "Claude changes a file",
"HOOK läuft automatisch": "HOOK runs automatically",
"Formatieren": "Format",
"Testen": "Test",
"Prüfen": "Check",
"Melden": "Report",
"STOPP": "STOP",
"Stopp vor gefährlichen Befehlen": "Stops before dangerous commands",

# --- Subagents ---
"Was ist mit Subagents? Sind das buchstäblich mehrere&nbsp;Claudes?":
    "What about subagents? Are those literally several&nbsp;Claudes?",
"Das sind eigen&shy;ständige Arbeiter, denen Claude klar umrissene Aufgaben geben kann – jeder mit eigenem Kontext&shy;fenster und eigenem Modell.":
    "They are independent workers Claude can hand clearly defined jobs to – each with its own context window and its own model.",
"Einer recherchiert, einer prüft Code, einer testet. Danach berichten sie zurück an den Haupt-Claude. Verwaltet über <code>/agents</code>.":
    "One researches, one reviews code, one tests. Then they report back to the main Claude. Managed through <code>/agents</code>.",
"HAUPT-CLAUDE": "MAIN CLAUDE",
"Recherche-Agent": "Research agent",
"Code-Agent": "Code agent",
"Test-Agent": "Test agent",
"Ergebnisse zurück an Claude": "Results go back to Claude",

# --- Slash-Befehle ---
"Und was sind diese ganzen /irgendwas-Befehle, die alle benutzen?":
    "And what are all those /something commands everyone uses?",
"Der Schrägstrich ist das Kurzbefehl-Menü von Claude Code.":
    "The slash is Claude Code&#8217;s shortcut menu.",
"Es gibt eingebaute wie <code>/clear</code> und <code>/compact</code> – und Skills bringen eigene Befehle mit, die du selbst aufrufen kannst.":
    "There are built-in ones like <code>/clear</code> and <code>/compact</code> – and skills bring their own commands that you can call yourself.",
"<b>/clear</b><span>neu anfangen</span>": "<b>/clear</b><span>start over</span>",
"<b>/compact</b><span>Kontext eindampfen</span>": "<b>/compact</b><span>boil the context down</span>",
"<b>/context</b><span>Wer frisst den Platz?</span>": "<b>/context</b><span>what eats the space?</span>",
"<b>/rewind</b><span>zurückspulen</span>": "<b>/rewind</b><span>rewind</span>",
"<b>/model</b><span>Modell wechseln</span>": "<b>/model</b><span>switch model</span>",
"<b>/usage</b><span>Verbrauch ansehen</span>": "<b>/usage</b><span>check your usage</span>",

# --- Berechtigungen ---
"Darf Claude einfach alles auf meinem Rechner?":
    "Is Claude allowed to do anything at all on my machine?",
"Nein. Von Haus aus darf es lesen – für alles andere fragt es vorher und zeigt Dir genau, was es vorhat.":
    "No. Out of the box it may read – for anything else it asks first and shows you exactly what it intends to do.",
"Wie streng es zugeht, schaltest Du mit <kbd>Shift</kbd>+<kbd>Tab</kbd> um. Im Plan-Modus schaut Claude sich erst alles an und legt Dir einen Vorschlag hin, bevor irgendetwas passiert.":
    "How strict it is you switch with <kbd>Shift</kbd>+<kbd>Tab</kbd>. In plan mode Claude first looks at everything and puts a proposal in front of you before anything happens.",
"<b>Manuell</b><span>liest von allein, fragt vor jedem Eingriff</span>":
    "<b>Manual</b><span>reads on its own, asks before every change</span>",
"<b>Änderungen ok</b><span>darf Dateien anfassen, der Rest bleibt Rückfrage</span>":
    "<b>Accept edits</b><span>may touch files, everything else still asks</span>",
"<b>Plan</b><span>schaut nur und schlägt vor – ändert nichts</span>":
    "<b>Plan</b><span>only looks and proposes – changes nothing</span>",
"<b>Automatisch</b><span>arbeitet durch, mit Sicherheitsnetz im Hintergrund</span>":
    "<b>Automatic</b><span>works straight through, with a safety net behind it</span>",
"umschalten mit Shift + Tab": "switch with Shift + Tab",

# --- Tastenkuerzel ---
"Gibt es Abkürzungen, die man kennen sollte?":
    "Are there shortcuts worth knowing?",
"Vier Zeichen sparen die meiste Tipparbeit – und zwei Tasten sind der Notausgang.":
    "Four characters save most of the typing – and two keys are the emergency exit.",
"Merk Dir vor allem <kbd>Esc</kbd>: Du musst nicht warten, bis Claude fertig ist. Anhalten, richtigstellen, weitermachen.":
    "Remember <kbd>Esc</kbd> above all: you don&#8217;t have to wait until Claude is done. Stop it, put it right, carry on.",
"<b>@datei</b><span>eine Datei ins Gespräch holen</span>":
    "<b>@file</b><span>pull a file into the conversation</span>",
"<b>!befehl</b><span>selbst etwas ausführen</span>":
    "<b>!command</b><span>run something yourself</span>",
"<b>/</b><span>das Befehlsmenü öffnen</span>":
    "<b>/</b><span>open the command menu</span>",
"<b>Shift+Tab</b><span>Berechtigungen umschalten</span>":
    "<b>Shift+Tab</b><span>switch permission mode</span>",
"<b>Esc</b><span>Claude sofort anhalten</span>":
    "<b>Esc</b><span>stop Claude right now</span>",
"<b>Esc Esc</b><span>zurückspulen</span>":
    "<b>Esc Esc</b><span>rewind</span>",

# --- Kontextfenster ---
"Letzte Frage: Was genau ist dieses Kontext&shy;fenster?":
    "Last question: what exactly is this context window?",
"Das ist Claudes Arbeits&shy;gedächtnis für das laufende Gespräch.":
    "That is Claude&#8217;s working memory for the conversation you are having.",
"Deine Eingaben, Claudes Antworten, gelesene Dateien und Werkzeug-Ergebnisse belegen alle Platz darin.":
    "Your input, Claude&#8217;s answers, files it has read and tool results all take up room in it.",
"Kontextfenster": "Context window",
"Deine Eingaben": "Your input",
"Claudes Antworten": "Claude&#8217;s answers",
"Gelesene Dateien": "Files it has read",
"Werkzeug-Ergebnisse": "Tool results",

"Wenn Leute also sagen &#8222;Claude hat den Faden verloren&#8220; …":
    "So when people say &#8220;Claude lost the plot&#8221; …",
"… dann ist meist so viel zusammen&shy;gekommen, dass nicht mehr alles gleich&shy;zeitig ins Arbeits&shy;gedächtnis passt.":
    "… then usually so much has piled up that it no longer all fits into the working memory at once.",
"Claude Code fasst dann automatisch zusammen. Mit <code>/context</code> siehst du, was den Platz belegt, mit <code>/clear</code> fängst du sauber neu an.":
    "Claude Code then summarises automatically. <code>/context</code> shows you what is taking up the space, <code>/clear</code> gives you a clean start.",
"KONTEXTFENSTER": "CONTEXT WINDOW",
"Was Claude gerade präsent hat": "What Claude currently has in mind",

# --- Checkpoints ---
"Und wenn Claude Mist baut? Alles verloren?":
    "And if Claude messes up? Is everything lost?",
"Nein – Claude Code setzt automatisch Sicherungs&shy;punkte, bevor es Dateien ändert.":
    "No – Claude Code sets checkpoints automatically before it changes files.",
"Zweimal <kbd>Esc</kbd> oder <code>/rewind</code>, und du spulst zurück: nur das Gespräch, nur die Dateien oder beides.":
    "<kbd>Esc</kbd> twice or <code>/rewind</code>, and you roll back: just the conversation, just the files, or both.",
"Stand A": "State A",
"Stand B": "State B",
"Stand C": "State C",
"hier ging&#8217;s schief": "this is where it went wrong",
"/rewind &#8211; zurück auf Stand&nbsp;B": "/rewind &#8211; back to state&nbsp;B",

# --- Memory ---
"Merkt sich Claude auch etwas über eine Sitzung hinaus?":
    "Does Claude remember anything beyond a single session?",
"Ja – dafür gibt es das Gedächtnis: kleine Notiz&shy;dateien, die Claude selbst schreibt und beim nächsten Start wieder liest.":
    "Yes – that is what memory is for: small note files Claude writes itself and reads again the next time it starts.",
"Deine Vorlieben, Projekt&shy;stände, wiederkehrende Entscheidungen. Anders als CLAUDE.md pflegt Claude das selbst.":
    "Your preferences, where a project stands, decisions that keep coming back. Unlike CLAUDE.md, Claude maintains this itself.",
"MEMORY.md": "MEMORY.md",
"notiz.md": "note.md",
"bleibt über Sitzungen hinweg erhalten": "survives from session to session",

# --- Wo Claude Code laeuft ---
"Und das läuft alles nur im Terminal?": "And all of this only runs in the terminal?",
"Längst nicht mehr. Claude Code gibt&#8217;s als Terminal-Befehl, als Desktop-App, im Browser unter <code>claude.ai/code</code> und als Erweiterung für VS&nbsp;Code und JetBrains.":
    "Not for a long time now. Claude Code comes as a terminal command, as a desktop app, in the browser at <code>claude.ai/code</code> and as an extension for VS&nbsp;Code and JetBrains.",
"Dazu Agenten, die im Hintergrund oder in der Cloud weiter&shy;arbeiten, während du etwas anderes machst.":
    "On top of that, agents that keep working in the background or in the cloud while you do something else.",
"Terminal": "Terminal",
"Desktop-App": "Desktop app",
"Browser": "Browser",
"VS&nbsp;Code / JetBrains": "VS&nbsp;Code / JetBrains",
"dieselbe Sitzung, überall": "the same session, everywhere",

# --- Desktop: drei Reiter ---
"Es gibt das alles auch zum Anklicken?": "Is there a version of all this to click on?",
"Ja. Die Claude-App für den Rechner hat drei Reiter: <b>Chat</b> ist das Gespräch, <b>Cowork</b> erledigt Büroarbeit, <b>Code</b> ist Claude Code mit Oberfläche.":
    "Yes. The Claude desktop app has three tabs: <b>Chat</b> is the conversation, <b>Cowork</b> does office work, <b>Code</b> is Claude Code with a user interface.",
"Es gibt sie für Mac und Windows, für Linux als Beta.":
    "It is available for Mac and Windows, and as a beta for Linux.",
"Chat": "Chat",
"Code": "Code",
"Reden<span class=\"chip-sub\">Fragen, Entwürfe, Ideen</span>":
    "Talking<span class=\"chip-sub\">questions, drafts, ideas</span>",
"Arbeiten lassen<span class=\"chip-sub\">Dokumente und Ordner</span>":
    "Delegating<span class=\"chip-sub\">documents and folders</span>",
"Entwickeln<span class=\"chip-sub\">Quelltext und Git</span>":
    "Developing<span class=\"chip-sub\">source code and Git</span>",

# --- Desktop: parallele Sitzungen ---
"Was kann die App, was das Terminal nicht kann?":
    "What can the app do that the terminal can&#8217;t?",
"Mehrere Sitzungen nebeneinander – jede in ihrer eigenen Git-Arbeitskopie. So kommen sie sich nicht in die Quere, auch wenn sie an derselben Stelle werkeln.":
    "Several sessions side by side – each in its own Git worktree. That way they don&#8217;t get in each other&#8217;s way, even when they work on the same spot.",
"Dazu Editor, Terminal, Vorschau und die Durchsicht der Änderungen im selben Fenster. Losschicken kannst Du eine Sitzung sogar vom Handy.":
    "Plus editor, terminal, preview and the review of the changes in the same window. You can even kick off a session from your phone.",
"Sitzung 1<span class=\"chip-sub\">eigene Arbeitskopie</span>":
    "Session 1<span class=\"chip-sub\">its own worktree</span>",
"Sitzung 2<span class=\"chip-sub\">eigene Arbeitskopie</span>":
    "Session 2<span class=\"chip-sub\">its own worktree</span>",
"Sitzung 3<span class=\"chip-sub\">eigene Arbeitskopie</span>":
    "Session 3<span class=\"chip-sub\">its own worktree</span>",
"Editor": "Editor",
"Vorschau": "Preview",
"Änderungen prüfen": "Review changes",
"alles in einem Fenster": "everything in one window",

# --- Cowork ---
"Und was ist dann Cowork?": "So what is Cowork, then?",
"Dieselbe Technik wie Claude Code – nur für Büroarbeit statt Programmieren, ohne Terminal und ohne Einrichten.":
    "The same machinery as Claude Code – only for office work instead of programming, with no terminal and nothing to set up.",
"Du gibst Ordner frei, beschreibst das Ziel, und Claude arbeitet los: Tabellen mit echten Formeln, Präsentationen, fertige Dokumente.":
    "You share folders, describe the goal, and Claude gets going: spreadsheets with real formulas, presentations, finished documents.",
"Deine Ordner": "Your folders",
"Deine Zugänge": "Your accounts",
"COWORK": "COWORK",
"Tabelle": "Spreadsheet",
"Präsentation": "Presentation",
"Bericht": "Report",

"Was macht es denn so?": "So what does it actually do?",
"Einen Ordner voller Belegfotos in eine Abrechnung verwandeln. Aus einem Stapel Notizen einen Bericht schreiben. Eine Ablage aufräumen. Dafür bedient es notfalls auch Chrome – klicken, tippen, Formulare ausfüllen.":
    "Turn a folder full of receipt photos into an expense report. Write a report from a pile of notes. Tidy up a filing system. If need be it will drive Chrome for that – clicking, typing, filling in forms.",
"Wie viel es allein entscheiden darf, legst Du fest.":
    "How much it may decide on its own is up to you.",
"Belege &#8594; Abrechnung": "Receipts &#8594; expense report",
"Notizen &#8594; Bericht": "Notes &#8594; report",
"Ablage aufräumen": "Tidy up the filing",
"und wenn nötig direkt im Browser": "and in the browser if that&#8217;s what it takes",
"Fragt jedes Mal<span class=\"chip-sub\">Du nickst alles ab</span>":
    "Asks every time<span class=\"chip-sub\">you approve everything</span>",
"Entscheidet selbst<span class=\"chip-sub\">mit Sicherheitsnetz</span>":
    "Decides for itself<span class=\"chip-sub\">with a safety net</span>",
"Macht einfach<span class=\"chip-sub\">ohne Rückfrage</span>":
    "Just gets on with it<span class=\"chip-sub\">without asking</span>",

# --- Cowork oder Code ---
"Wann nehme ich denn was?": "When do I use which?",
"Cowork, wenn am Ende Dateien stehen: Berichte, Tabellen, Recherchen. Nichts einzurichten, und es läuft abgeschottet.":
    "Cowork when files come out at the end: reports, spreadsheets, research. Nothing to set up, and it runs sealed off.",
"Claude Code, wenn am Ende Quelltext steht: Tests, Git und volle Sicht auf jeden einzelnen Schritt.":
    "Claude Code when source code comes out at the end: tests, Git and full sight of every single step.",
"Büroarbeit": "Office work",
"nichts einzurichten": "nothing to set up",
"läuft abgeschottet": "runs sealed off",
"für alle": "for everyone",
"Claude Code": "Claude Code",
"Programmieren": "Programming",
"Terminal und Git": "Terminal and Git",
"jeder Schritt sichtbar": "every step visible",
"für Bastler": "for tinkerers",

# --- Routinen ---
"Und wenn etwas regelmäßig von allein laufen soll?":
    "And what if something should run regularly on its own?",
"Dann legst Du eine Routine an: Auftrag, Projekt und Zugänge einmal gespeichert – danach läuft sie ohne Dich.":
    "Then you create a routine: task, project and accounts saved once – after that it runs without you.",
"Und zwar in der Cloud. Dein Rechner darf ausgeschaltet sein. Angelegt wird sie mit <code>/schedule</code>, in der App oder im Browser.":
    "And it does so in the cloud. Your machine may be switched off. You create it with <code>/schedule</code>, in the app or in the browser.",
"/schedule täglich um 9 Uhr die neuen Pull Requests durchsehen":
    "/schedule review the new pull requests daily at 9am",
"Auftrag": "Task",
"Projekt": "Project",
"Zugänge": "Accounts",
"läuft in der Cloud – Rechner aus": "runs in the cloud – machine off",

"Und was bringt so eine Routine ins Rollen?": "And what sets a routine off?",
"Drei Dinge, einzeln oder in Kombination: ein Zeitplan, ein Aufruf von außen, oder ein Ereignis auf GitHub.":
    "Three things, alone or combined: a schedule, a call from outside, or an event on GitHub.",
"Der kürzeste Abstand ist eine Stunde. Einmalige Termine gehen auch – <code>/schedule in zwei Wochen …</code> Das Ganze ist noch im Vorschau-Stadium.":
    "The shortest interval is one hour. One-off appointments work too – <code>/schedule in two weeks …</code> The whole thing is still in preview.",
"Zeitplan<span class=\"chip-sub\">stündlich bis wöchentlich</span>":
    "Schedule<span class=\"chip-sub\">hourly to weekly</span>",
"Aufruf<span class=\"chip-sub\">von Deinen Werkzeugen</span>":
    "A call<span class=\"chip-sub\">from your own tools</span>",
"GitHub<span class=\"chip-sub\">neuer Pull Request</span>":
    "GitHub<span class=\"chip-sub\">new pull request</span>",
"Routine läuft": "Routine runs",
"Ergebnis liegt morgens da": "the result is waiting in the morning",

# --- /loop ---
"Und wenn es nur für die nächste Stunde sein soll?":
    "And if it&#8217;s only meant for the next hour?",
"Dann nimm <code>/loop</code>. Der wiederholt einen Auftrag in der offenen Sitzung – auf Deinem Rechner, mit Deinen Dateien.":
    "Then use <code>/loop</code>. It repeats a task inside the open session – on your machine, with your files.",
"Lässt Du die Zeitangabe weg, sucht sich Claude den Abstand selbst: kurz, solange sich etwas tut, länger, wenn Ruhe ist. <kbd>Esc</kbd> beendet die Schleife.":
    "Leave out the interval and Claude picks it itself: short while something is happening, longer when things are quiet. <kbd>Esc</kbd> ends the loop.",
"/loop 5m schau nach, ob der Bau durch ist":
    "/loop 5m check whether the build has finished",
"mit Zeitangabe<span class=\"chip-sub\">alle 5 Minuten</span>":
    "with an interval<span class=\"chip-sub\">every 5 minutes</span>",
"ohne Zeitangabe<span class=\"chip-sub\">Claude entscheidet</span>":
    "without one<span class=\"chip-sub\">Claude decides</span>",
"ganz ohne Auftrag<span class=\"chip-sub\">räumt selbst auf</span>":
    "with no task at all<span class=\"chip-sub\">it tidies up by itself</span>",
"läuft nur, solange die Sitzung offen ist – und endet nach sieben Tagen":
    "runs only while the session is open – and ends after seven days",

# --- Schleife oder Routine ---
"Das klingt doch fast wie eine Routine.": "That sounds almost like a routine.",
"Der Unterschied ist, wo es läuft. Die Schleife braucht Deine offene Sitzung und Deinen eingeschalteten Rechner – dafür sieht sie Deine Dateien.":
    "The difference is where it runs. The loop needs your session open and your machine switched on – in return it sees your files.",
"Die Routine läuft in der Cloud, ohne Dich. Faustregel: Schleife für heute Nachmittag, Routine für jeden Montag.":
    "The routine runs in the cloud, without you. Rule of thumb: loop for this afternoon, routine for every Monday.",
"auf Deinem Rechner": "on your machine",
"Sitzung muss offen sein": "session has to stay open",
"sieht Deine Dateien": "sees your files",
"für jetzt gerade": "for right now",
"/schedule": "/schedule",
"in der Cloud": "in the cloud",
"Rechner darf aus sein": "machine may be off",
"frische Kopie des Projekts": "a fresh copy of the project",
"für jede Woche": "for every week",

# --- Modelle ---
"Und welches Modell arbeitet da eigentlich?": "And which model is actually doing the work?",
"Stand August 2026: <b>Opus&nbsp;5</b> für die schweren Sachen, <b>Sonnet&nbsp;5</b> für den Alltag, <b>Haiku&nbsp;4.5</b> für schnell und günstig.":
    "As of August 2026: <b>Opus&nbsp;5</b> for the heavy lifting, <b>Sonnet&nbsp;5</b> for everyday work, <b>Haiku&nbsp;4.5</b> for fast and cheap.",
"Umschalten mit <code>/model</code>. Mit <code>/fast</code> antwortet Opus schneller – es wird dabei nicht durch ein kleineres Modell ersetzt.":
    "Switch with <code>/model</code>. With <code>/fast</code> Opus answers more quickly – it is not swapped for a smaller model in the process.",
"<b>Opus 5</b><span>die schweren Aufgaben</span><i>1 Mio. Kontext</i>":
    "<b>Opus 5</b><span>the heavy jobs</span><i>1M context</i>",
"<b>Sonnet 5</b><span>der Alltag</span><i>1 Mio. Kontext</i>":
    "<b>Sonnet 5</b><span>everyday work</span><i>1M context</i>",
"<b>Haiku 4.5</b><span>schnell &amp; günstig</span><i>200 Tsd. Kontext</i>":
    "<b>Haiku 4.5</b><span>fast &amp; cheap</span><i>200K context</i>",
"wechseln mit /model": "switch with /model",

# --- Gut fragen ---
"Und wie sage ich es am besten?": "And how do I best put it?",
"Sag das Ziel, nicht die einzelnen Schritte – den Weg findet Claude selbst. Sag dazu, woran man merkt, dass es fertig ist.":
    "State the goal, not the individual steps – Claude finds the way itself. And say how you can tell when it is done.",
"Und gib den Zusammenhang mit: für wen das gedacht ist, wozu, und was auf keinen Fall passieren darf. Je klarer der Auftrag, desto weniger Runden.":
    "And give the context: who it is for, what for, and what must not happen under any circumstances. The clearer the task, the fewer rounds.",
"eher nicht": "rather not",
"&#8222;Mach die Tabelle mal schöner.&#8220;": "&#8220;Make the table look nicer.&#8221;",
"besser": "better",
"&#8222;Die Tabelle geht an den Vorstand. Zahlen rechtsbündig, Summenzeile fett, keine Farben. Prüf am Ende, dass die Summen stimmen.&#8220;":
    "&#8220;The table goes to the board. Numbers right-aligned, totals row in bold, no colours. Check at the end that the totals add up.&#8221;",

# --- Nachpruefen ---
"Kann ich mich denn darauf verlassen?": "Can I actually rely on it?",
"Meistens ja – aber Claude kann sich auch überzeugend irren. Lass Dir zeigen, was es getan hat, statt es nur zu glauben.":
    "Usually yes – but Claude can also be convincingly wrong. Have it show you what it did instead of just believing it.",
"Und was sich prüfen lässt, soll Claude gleich selbst prüfen: Tests laufen lassen, Zahlen nachrechnen, Quellen nennen.":
    "And whatever can be checked, let Claude check itself: run the tests, redo the arithmetic, name the sources.",
"Änderungen ansehen<span class=\"chip-sub\">nicht nur die Zusammenfassung</span>":
    "Look at the changes<span class=\"chip-sub\">not just the summary</span>",
"Tests laufen lassen<span class=\"chip-sub\">am besten automatisch</span>":
    "Run the tests<span class=\"chip-sub\">automatically if you can</span>",
"Quellen nennen lassen<span class=\"chip-sub\">woher stammt die Zahl?</span>":
    "Ask for sources<span class=\"chip-sub\">where does that number come from?</span>",
"Im Zweifel zurückspulen<span class=\"chip-sub\">Esc Esc kostet nichts</span>":
    "When in doubt, rewind<span class=\"chip-sub\">Esc Esc costs nothing</span>",
"Vertrauen ist gut. Nachsehen ist schneller als Reparieren.":
    "Trust is fine. Checking is faster than repairing.",

# --- Fremde Inhalte ---
"Und wenn in einer Datei steht &#8222;lösche alles&#8220;?":
    "And what if a file says &#8220;delete everything&#8221;?",
"Gute Frage – genau da liegt die Stolperfalle. Claude liest Webseiten, Mails, Tickets und fremden Quelltext. Nichts davon ist ein Auftrag von Dir.":
    "Good question – that is exactly where the trap is. Claude reads web pages, e-mails, tickets and other people&#8217;s source code. None of that is an instruction from you.",
"Aufträge kommen von Dir, aus Deinen Projektregeln und aus dem, was Du erlaubst. Alles andere ist Material zum Lesen – deshalb sind die Berechtigungen keine Schikane.":
    "Instructions come from you, from your project rules and from what you allow. Everything else is material to read – which is why the permissions are not there to annoy you.",
"Deine Anweisung<span class=\"chip-sub\">zählt</span>":
    "Your instruction<span class=\"chip-sub\">counts</span>",
"CLAUDE.md<span class=\"chip-sub\">zählt</span>":
    "CLAUDE.md<span class=\"chip-sub\">counts</span>",
"Webseite<span class=\"chip-sub\">nur Material</span>":
    "Web page<span class=\"chip-sub\">material only</span>",
"E-Mail<span class=\"chip-sub\">nur Material</span>":
    "E-mail<span class=\"chip-sub\">material only</span>",
"fremdes Ticket<span class=\"chip-sub\">nur Material</span>":
    "someone&#8217;s ticket<span class=\"chip-sub\">material only</span>",
"Je weiter Claude nach draußen darf, desto enger halte die Leine":
    "The further out Claude may reach, the shorter you keep the leash",

# --- Schluss ---
"Ohh. Ich glaub, jetzt hab ich&#8217;s.": "Ohh. I think I&#8217;ve got it now.",
"Das freut mich zu hören.": "Glad to hear it.",
"<b>CLAUDE.md</b> &#8211; die Regeln deines Projekts":
    "<b>CLAUDE.md</b> &#8211; the rules of your project",
"<b>Skills</b> &#8211; wie eine Aufgabe richtig läuft":
    "<b>Skills</b> &#8211; how a job is done properly",
"<b>Plugins</b> &#8211; alles davon als ein Paket":
    "<b>Plugins</b> &#8211; all of that as one bundle",
"<b>MCP</b> &#8211; die Verbindung nach draußen":
    "<b>MCP</b> &#8211; the connection to the outside",
"<b>Hooks</b> &#8211; laufen automatisch bei Ereignissen":
    "<b>Hooks</b> &#8211; run automatically on events",
"<b>Subagents</b> &#8211; Helfer mit eigenem Kopf":
    "<b>Subagents</b> &#8211; helpers with a mind of their own",
"<b>Kontextfenster</b> &#8211; das Arbeitsgedächtnis":
    "<b>Context window</b> &#8211; the working memory",
"<b>Checkpoints &amp; Memory</b> &#8211; zurückspulen und behalten":
    "<b>Checkpoints &amp; memory</b> &#8211; rewind and remember",
"<b>Cowork</b> &#8211; dasselbe für Büroarbeit, ohne Terminal":
    "<b>Cowork</b> &#8211; the same for office work, without a terminal",
"<b>Routinen</b> &#8211; laufen nach Plan in der Cloud":
    "<b>Routines</b> &#8211; run to a schedule in the cloud",
"<b>Berechtigungen</b> &#8211; Du bestimmst, wie weit Claude darf":
    "<b>Permissions</b> &#8211; you decide how far Claude may go",
"<b>/loop</b> &#8211; wiederholt etwas, solange Du dabei bist":
    "<b>/loop</b> &#8211; repeats something while you are there",
}

# Seitentitel und Sprachkennung des Dokuments.
TITEL = "Claude Code – the guide"
