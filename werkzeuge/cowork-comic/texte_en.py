# -*- coding: utf-8 -*-
"""English wording for the Claude Cowork comic.

Key = the German text exactly as it ends up in the built page, value = its
English counterpart. The keys are produced by i18n.einheiten(); if the German
side changes, the build stops and prints the new key, so nothing can silently
stay German.

Keep the inline markup (<b>, <i>, <code>, <span class="chip-sub">) identical on
both sides — it carries the layout.
"""

TEXTE = {

# --- Titelseite ---
"Claude soll jetzt richtig <i>arbeiten</i>? Ich&nbsp;kann&nbsp;aber nicht programmieren.":
    "Claude is supposed to actually <i>work</i> now? But&nbsp;I&nbsp;can&#8217;t program.",
"Und ein Terminal hab ich noch nie&nbsp;aufgemacht.":
    "And I have never once&nbsp;opened a terminal.",
"Ordner": "Folders",
"Der Plan": "The plan",
"Tabellen": "Spreadsheets",
"Folien": "Slides",
"Verbindungen": "Connections",
"Projekte": "Projects",
"Rechte": "Permissions",
"Zeitplan": "Schedule",
"Sicherheit": "Safety",
"Helfer": "Helpers",
"Chrome": "Chrome",
"Skills": "Skills",
"Brauchst Du&nbsp;nicht.": "You don&#8217;t&nbsp;need to.",

# --- Was ist Cowork ---
"Also – was ist Cowork überhaupt?": "So – what is Cowork, actually?",
"Dieselbe Technik, die hinter Claude Code steckt – aber Du bedienst sie in der ganz normalen Claude-App. Kein Terminal, nichts einzurichten.":
    "The same machinery that sits behind Claude Code – but you use it in the ordinary Claude app. No terminal, nothing to set up.",
"Sie ist für Büroarbeit gedacht: recherchieren, auswerten, Dokumente erstellen. Alles, was aus mehreren Schritten besteht.":
    "It is meant for office work: research, analysis, producing documents. Anything that takes several steps.",
"Recherche": "Research",
"Auswertung": "Analysis",
"Dokumente": "Documents",
"Aufräumen": "Tidying up",
"COWORK": "COWORK",
"dieselbe Technik wie Claude Code – nur ohne Terminal":
    "the same machinery as Claude Code – just without a terminal",

# --- Chat vs. Cowork ---
"Aber ich kann Claude doch jetzt schon Fragen&nbsp;stellen?":
    "But I can already ask&nbsp;Claude questions?",
"Im Chat bekommst Du eine <b>Antwort</b> – und baust daraus selbst die Datei.":
    "In chat you get an <b>answer</b> – and you build the file from it yourself.",
"In Cowork bekommst Du die <b>fertige Datei</b>. Claude liest Deine Unterlagen, schreibt das Ergebnis und sagt Dir, woher jede Angabe stammt.":
    "In Cowork you get the <b>finished file</b>. Claude reads your documents, writes the result and tells you where every figure came from.",
"Chat": "Chat",
"Du fragst": "You ask",
"Claude antwortet": "Claude answers",
"Du baust die Datei selbst": "You build the file yourself",
"Cowork": "Cowork",
"Du beschreibst das Ziel": "You describe the goal",
"Claude arbeitet": "Claude works",
"Fertige Datei": "Finished file",
"Du bekommst das Ergebnis": "You get the result",

# --- Erste Schritte ---
"Wie fange ich an?": "How do I get started?",
"Vier Schritte. Im Eingabefeld schaltest Du von <b>Chat</b> auf <b>Cowork</b> um – das ist schon der schwierigste Teil.":
    "Four steps. In the input box you switch from <b>Chat</b> to <b>Cowork</b> – and that is already the hardest part.",
"Dann beschreibst Du, was herauskommen soll. Claude zeigt Dir seinen Plan. Du schaust drüber, und dann läuft es los.":
    "Then you describe what should come out. Claude shows you its plan. You look it over, and off it goes.",
"<b>1 · Umschalten</b><span>von Chat auf Cowork</span>":
    "<b>1 · Switch</b><span>from Chat to Cowork</span>",
"<b>2 · Beschreiben</b><span>„Sortiere meinen Download-Ordner“</span>":
    "<b>2 · Describe</b><span>&#8220;Sort out my downloads folder&#8221;</span>",
"<b>3 · Plan ansehen</b><span>Claude zeigt, was es vorhat</span>":
    "<b>3 · Read the plan</b><span>Claude shows what it intends</span>",
"<b>4 · Laufen lassen</b><span>zuschauen – oder später wiederkommen</span>":
    "<b>4 · Let it run</b><span>watch – or come back later</span>",

# --- Der Plan ---
"Legt es dann einfach los?": "Does it just get going, then?",
"Nein. Claude überlegt sich erst einen Plan und zeigt ihn Dir – bevor irgendetwas passiert.":
    "No. Claude works out a plan first and shows it to you – before anything happens.",
"Und während es arbeitet, siehst Du bei jedem Schritt, was es gerade tut. Kein schwarzer Kasten.":
    "And while it works you see at every step what it is doing. No black box.",
"Deine Aufgabe": "Your task",
"Claude zeigt Dir zuerst:": "Claude shows you first:",
"„Ich sehe mir die 34 Belege an, ordne sie nach Datum, ziehe die Beträge heraus und baue daraus eine Tabelle mit Summenformel.“":
    "&#8220;I&#8217;ll look at the 34 receipts, sort them by date, pull out the amounts and build a spreadsheet with a totals formula.&#8221;",
"Du nickst": "You approve",
"oder Du korrigierst": "or you correct it",

# --- Ordnerfreigabe ---
"Woher weiß es, wo meine Sachen liegen?": "How does it know where my things are?",
"Du gibst ihm einen Ordner frei. Claude liest und schreibt dann direkt darin – Du musst nichts hochladen und nichts herunterladen.":
    "You share a folder with it. Claude then reads and writes directly inside it – you don&#8217;t have to upload or download anything.",
"Das geht über die Desktop-App, nur für die Ordner, die Du ausgewählt hast, und nur solange die App läuft.":
    "That works through the desktop app, only for the folders you picked, and only while the app is running.",
"Nur dieser Ordner<span class=\"chip-sub\">von Dir ausgewählt</span>":
    "This folder only<span class=\"chip-sub\">chosen by you</span>",
"Alles andere<span class=\"chip-sub\">bleibt zu</span>":
    "Everything else<span class=\"chip-sub\">stays shut</span>",
"Beleg.pdf": "Receipt.pdf",
"Notizen.txt": "Notes.txt",
"Liste.xlsx": "List.xlsx",
"kein Hochladen, kein Herunterladen – Claude arbeitet direkt darin":
    "no uploading, no downloading – Claude works right inside it",

# --- Ergebnisse ---
"Und was bekomme ich am Ende?": "And what do I get at the end?",
"Richtige Dateien, keine Textwüste zum Abtippen.":
    "Real files, not a wall of text for you to retype.",
"Tabellen mit <b>funktionierenden Formeln</b>, Präsentationen, sauber formatierte Dokumente. Zum Öffnen und Weiterschicken.":
    "Spreadsheets with <b>working formulas</b>, presentations, neatly formatted documents. Ready to open and pass on.",
"Tabelle": "Spreadsheet",
"Präsentation": "Presentation",
"Bericht": "Report",
"mit echten Formeln": "with real formulas",
"fertig formatiert": "fully formatted",
"mit Quellenangabe": "with its sources named",

# --- Beispiele ---
"Gib mir mal ganz konkrete Beispiele.": "Give me some really concrete examples.",
"Den Download-Ordner nach Art und Datum sortieren. Einen Stapel Belegfotos in eine fertige Abrechnung verwandeln.":
    "Sort the downloads folder by type and date. Turn a pile of receipt photos into a finished expense report.",
"Dateien einheitlich umbenennen. Aus Notizen einen Bericht bauen. Vor einem Termin alles Wichtige zusammentragen.":
    "Rename files to one scheme. Build a report out of notes. Pull together everything that matters before a meeting.",
"Download-Ordner sortieren": "Sort the downloads folder",
"Belege &#8594; Abrechnung": "Receipts &#8594; expense report",
"Dateien umbenennen<span class=\"chip-sub\">2026-08-13-Rechnung.pdf</span>":
    "Rename files<span class=\"chip-sub\">2026-08-13-invoice.pdf</span>",
"Notizen &#8594; Bericht": "Notes &#8594; report",
"Termin vorbereiten": "Prepare for a meeting",
"Recherche zusammenfassen": "Summarise research",
"Bericht jede Woche": "A report every week",

# --- Parallele Helfer ---
"Große Aufgaben dauern dann ewig, oder?": "Big jobs must take forever, then?",
"Nicht unbedingt. Claude teilt große Arbeit in kleinere Stücke auf und lässt mehrere Helfer gleichzeitig laufen.":
    "Not necessarily. Claude splits big work into smaller pieces and runs several helpers at the same time.",
"Jeder erledigt seinen Teil, am Ende wird alles zusammengeführt.":
    "Each does its part, and at the end everything is brought together.",
"Deine große Aufgabe": "Your big task",
"Helfer 1<span class=\"chip-sub\">liest die Unterlagen</span>":
    "Helper 1<span class=\"chip-sub\">reads the documents</span>",
"Helfer 2<span class=\"chip-sub\">sucht die Zahlen</span>":
    "Helper 2<span class=\"chip-sub\">finds the numbers</span>",
"Helfer 3<span class=\"chip-sub\">prüft nach</span>":
    "Helper 3<span class=\"chip-sub\">checks the work</span>",
"ein fertiges Ergebnis": "one finished result",

# --- Weiterlaufen ---
"Muss ich dabei sitzen bleiben?": "Do I have to sit and watch?",
"Nein. Du kannst den Laptop zuklappen – die Aufgabe läuft weiter.":
    "No. You can close the laptop – the job keeps running.",
"Und Du kannst dieselbe Sitzung später woanders wieder aufmachen: am Rechner, im Browser oder am Handy.":
    "And you can reopen the same session somewhere else later: on your computer, in the browser or on your phone.",
"Du startest": "You start it",
"Laptop zu": "Laptop closed",
"Claude arbeitet weiter": "Claude keeps working",
"Du kommst zurück": "You come back",
"Desktop-App": "Desktop app",
"Browser": "Browser",
"Handy": "Phone",
"dieselbe Sitzung, egal wo Du sie aufmachst":
    "the same session, wherever you open it",

# --- Dispatch ---
"Du sagst Handy – kann ich auch von unterwegs etwas&nbsp;anstoßen?":
    "You say phone – can I kick something off&nbsp;while I&#8217;m out?",
"Dafür gibt es <b>Dispatch</b>. Dein Handy wird zur Fernbedienung für den Claude, der zu Hause auf Deinem Rechner sitzt.":
    "That is what <b>Dispatch</b> is for. Your phone becomes the remote control for the Claude sitting on your computer at home.",
"In der Handy-App auf Cowork gehen, in der Seitenleiste <b>Dispatch</b> antippen, Aufgabe hinschreiben. Du bekommst eine Mitteilung, wenn es fertig ist – oder wenn Claude etwas von Dir wissen will.":
    "In the phone app go to Cowork, tap <b>Dispatch</b> in the sidebar, write down the task. You get a notification when it is done – or when Claude needs something from you.",
"Unterwegs": "On the go",
"Auftrag tippen": "Type the task",
"Rechner arbeitet": "Computer works",
"Mitteilung zurück": "Notified back",
"Zum Beispiel unterwegs getippt:": "Typed on the go, for example:",
"„Zieh die Zahlen aus der Quartalstabelle und leg mir eine Zusammenfassung auf den Schreibtisch.“":
    "&#8220;Pull the numbers out of the quarterly spreadsheet and put a summary on my desktop.&#8221;",
"Rechner muss wach sein<span class=\"chip-sub\">und die Claude-App offen</span>":
    "Computer must be awake<span class=\"chip-sub\">and the Claude app open</span>",
"Ein Gespräch<span class=\"chip-sub\">Handy und Rechner, ohne Bruch</span>":
    "One conversation<span class=\"chip-sub\">phone and computer, no break</span>",

# --- Projekte ---
"Kann ich das irgendwie ordnen?": "Can I bring some order to this?",
"Ja, mit Projekten. Jedes Projekt ist ein eigener Arbeitsbereich mit eigenen Dateien und eigenen Anweisungen.":
    "Yes, with projects. Every project is its own workspace with its own files and its own instructions.",
"Claude merkt sich darin auch, was es beim letzten Mal gelernt hat – Du fängst nicht jedes Mal von vorn an.":
    "Inside one, Claude also remembers what it learned last time – you don&#8217;t start from scratch every time.",
"Steuer 2026": "Taxes 2026",
"eigene Dateien": "its own files",
"eigene Anweisungen": "its own instructions",
"eigenes Gedächtnis": "its own memory",
"Verein": "Club",
"getrennte Arbeitsbereiche – nichts vermischt sich":
    "separate workspaces – nothing gets mixed up",

# --- Verbindungen ---
"Kommt es auch an meine anderen Programme?": "Can it reach my other programs too?",
"Wenn Du es verbindest, ja. Google Drive, Slack und andere Dienste hängst Du unter <b>Customize</b> in der Seitenleiste an.":
    "If you connect it, yes. You attach Google Drive, Slack and other services under <b>Customize</b> in the sidebar.",
"Danach holt Claude sich die Sachen selbst – Du kopierst nichts mehr hin und her.":
    "After that Claude fetches things itself – no more copying back and forth.",
"Google Drive": "Google Drive",
"Slack": "Slack",
"weitere Dienste": "other services",
"Dein fertiges Ergebnis": "Your finished result",

# --- Skills ---
"Ich hab von „Skills“ gehört. Brauch ich die?":
    "I&#8217;ve heard about &#8220;skills&#8221;. Do I need them?",
"Erst mal nicht. Ein Skill ist ein gespeicherter Ablauf für etwas, das Du immer wieder gleich brauchst.":
    "Not to begin with. A skill is a saved procedure for something you need the same way over and over.",
"Fertige Pakete gibt es für ganze Berufsfelder. Auch die schaltest Du unter <b>Customize</b> dazu.":
    "There are ready-made bundles for whole professions. You switch those on under <b>Customize</b> as well.",
"Deine Anweisung": "Your instruction",
"Dein Ablauf": "Your procedure",
"Dein Beispiel": "Your example",
"SKILL": "SKILL",
"einmal einrichten": "set it up once",
"immer wieder aufrufen": "call it again and again",

# --- Chrome ---
"Und was ist, wenn etwas nur auf einer Webseite geht?":
    "And what if something only works on a website?",
"Dann kann Claude den Browser mitbenutzen: klicken, tippen, Formulare ausfüllen.":
    "Then Claude can use the browser too: clicking, typing, filling in forms.",
"Das ist praktisch – aber genau da wäre ich vorsichtig. Für Bank, Arzt und alles Persönliche lieber nicht.":
    "That is handy – but that is exactly where I would be careful. Better not for banking, health and anything personal.",
"Seite öffnen": "Open the page",
"klicken": "click",
"ausfüllen": "fill in",
"Ergebnis holen": "collect the result",
"Gut geeignet<span class=\"chip-sub\">öffentliche Seiten, Recherche</span>":
    "Well suited<span class=\"chip-sub\">public pages, research</span>",
"Lieber nicht<span class=\"chip-sub\">Bank, Gesundheit, Privates</span>":
    "Better not<span class=\"chip-sub\">banking, health, private matters</span>",

# --- Berechtigungen ---
"Darf es dann einfach alles machen?": "So may it simply do anything?",
"Du entscheidest, wie weit die Leine ist. Es gibt drei Stufen.":
    "You decide how long the leash is. There are three levels.",
"Für heikle Sachen nimmst Du <b>Manuell</b>. Die unterste Stufe schaltet <i>alle</i> Kontrollen ab – die würde ich nur nehmen, wenn Du genau weißt, warum.":
    "For delicate things you use <b>Manual</b>. The bottom level switches <i>all</i> the checks off – I would only use that one if you know exactly why.",
"<b>Manuell</b><span>fragt vor jedem Schritt – für alles Heikle</span>":
    "<b>Manual</b><span>asks before every step – for anything delicate</span>",
"<b>Automatisch</b><span>arbeitet durch, prüft sich dabei selbst auf Sicherheit</span>":
    "<b>Automatic</b><span>works straight through, checking itself for safety</span>",
"<b>Ohne Rückfrage</b><span>fragt nie, nichts prüft mit – nur mit gutem Grund</span>":
    "<b>No questions</b><span>never asks, nothing checks along – only with good reason</span>",
"Endgültig löschen darf Claude nie ohne Dein ausdrückliches Ja – in jeder Stufe":
    "Claude may never delete for good without your explicit yes – at every level",

# --- Zeitplan ---
"Kann es auch regelmäßig von allein laufen?": "Can it run regularly on its own, too?",
"Ja. Unter <b>Scheduled</b> in der Seitenleiste legst Du wiederkehrende Aufgaben an – jeden Montag der Bericht, jeden Morgen die Zusammenfassung.":
    "Yes. Under <b>Scheduled</b> in the sidebar you set up recurring jobs – the report every Monday, the summary every morning.",
"Fang mit etwas Harmlosem an. Und schau ab und zu nach, was dabei herauskommt.":
    "Start with something harmless. And look in now and then to see what comes out.",
"Jeden Montag: Wochenbericht aus dem Projektordner":
    "Every Monday: weekly report from the project folder",
"läuft von allein": "runs by itself",
"Ergebnis liegt da": "the result is waiting",
"Du schaust drüber": "you look it over",
"mit kleinen, ungefährlichen Aufgaben anfangen":
    "start with small, harmless jobs",

# --- Wo es laeuft ---
"Läuft das alles auf meinem Rechner?": "Does all of this run on my computer?",
"Nein – die eigentliche Arbeit passiert abgeschottet auf den Servern von Anthropic. An Dein Heimnetz kommt sie nicht heran.":
    "No – the actual work happens sealed off on Anthropic&#8217;s servers. It cannot reach your home network.",
"Aber Vorsicht bei der Denkweise: Das schützt Deinen Rechner. Es begrenzt <b>nicht</b>, was Claude mit dem anfangen kann, was Du ihm freigegeben hast.":
    "But careful with that line of thought: it protects your computer. It does <b>not</b> limit what Claude can do with whatever you shared with it.",
"Geschützt": "Protected",
"Dein Rechner": "Your computer",
"Dein Heimnetz": "Your home network",
"da kommt sie nicht heran": "it cannot reach these",
"Trotzdem offen": "Open all the same",
"freigegebene Ordner": "shared folders",
"verbundene Dienste": "connected services",
"was Du freigibst, ist freigegeben": "what you share is shared",

# --- Fremde Inhalte ---
"Gibt es etwas, das wirklich schiefgehen kann?":
    "Is there anything that can really go wrong?",
"Der wichtigste Fall: In einer Webseite, einer Mail oder einem Dokument stecken versteckte Anweisungen – und Claude liest sie mit, während es Deine Aufgabe erledigt.":
    "The one that matters most: a web page, an e-mail or a document contains hidden instructions – and Claude reads them along the way while doing your job.",
"Deshalb: nur Quellen einbeziehen, denen Du traust. Und bei Fremdem lieber die Stufe <b>Manuell</b>.":
    "So: only pull in sources you trust. And with anything from outside, better use the <b>Manual</b> level.",
"fremde Webseite": "someone else&#8217;s web page",
"versteckte Anweisung": "hidden instruction",
"Claude liest mit": "Claude reads it too",
"Quellen prüfen<span class=\"chip-sub\">nur was Du kennst</span>":
    "Check your sources<span class=\"chip-sub\">only what you know</span>",
"Manuell schalten<span class=\"chip-sub\">bei allem Fremden</span>":
    "Switch to manual<span class=\"chip-sub\">for anything from outside</span>",
"Ergebnis ansehen<span class=\"chip-sub\">nicht blind vertrauen</span>":
    "Look at the result<span class=\"chip-sub\">don&#8217;t trust it blindly</span>",

# --- Merkregeln ---
"Was soll ich mir merken, damit nichts passiert?":
    "What should I remember so nothing goes wrong?",
"Einen eigenen Arbeitsordner anlegen statt alles freizugeben. Sicherungskopien behalten. Und Finanzunterlagen, Zugangsdaten und Persönliches draußen lassen.":
    "Set up a working folder of its own instead of sharing everything. Keep backups. And leave financial papers, credentials and personal matters out of it.",
"Du musst nicht jeden Schritt prüfen – aber schau, ob das Ganze plausibel aussieht.":
    "You don&#8217;t have to check every step – but do look at whether the whole thing seems plausible.",
"<b>Eigener Ordner</b><span>nur das freigeben, was für die Aufgabe nötig ist</span>":
    "<b>A folder of its own</b><span>share only what the job needs</span>",
"<b>Sicherungskopie</b><span>von allem, was wehtut, wenn es weg ist</span>":
    "<b>Backups</b><span>of anything that hurts if it is gone</span>",
"<b>Klein anfangen</b><span>erst harmlose Aufgaben, dann die wichtigen</span>":
    "<b>Start small</b><span>harmless jobs first, then the important ones</span>",
"<b>Draußen lassen</b><span>Finanzen, Zugangsdaten, Gesundheit, Privates</span>":
    "<b>Leave out</b><span>finances, credentials, health, private matters</span>",

# --- Cowork oder Code ---
"Und wann nehme ich das andere – Claude Code?":
    "And when do I use the other one – Claude Code?",
"Cowork, wenn am Ende <b>Dateien</b> stehen: Berichte, Tabellen, Recherchen, aufgeräumte Ordner.":
    "Cowork when <b>files</b> come out at the end: reports, spreadsheets, research, tidied-up folders.",
"Claude Code, wenn am Ende <b>Quelltext</b> steht. Das ist die Werkzeugkiste für Leute, die programmieren.":
    "Claude Code when <b>source code</b> comes out at the end. That is the toolbox for people who program.",
"Büroarbeit": "Office work",
"nichts einzurichten": "nothing to set up",
"in der normalen App": "in the ordinary app",
"für alle": "for everyone",
"Claude Code": "Claude Code",
"Programmieren": "Programming",
"Terminal und Git": "Terminal and Git",
"jeder Schritt sichtbar": "every step visible",
"für Bastler": "for tinkerers",

# --- Wo finde ich es ---
"Und wo finde ich das jetzt?": "And where do I find it?",
"In der Claude-App – als Umschalter direkt neben dem Chat. Am Rechner für Windows und Mac, dazu im Browser und am Handy.":
    "In the Claude app – as a switch right next to the chat. On the computer for Windows and Mac, plus in the browser and on your phone.",
"Es gehört zu den bezahlten Zugängen. Wenn Du schon einen hast, ist es einfach da.":
    "It is part of the paid plans. If you already have one, it is simply there.",
"Windows": "Windows",
"Mac": "Mac",
"in den bezahlten Zugängen enthalten – Stand August 2026":
    "included in the paid plans – as of August 2026",

# --- Schluss ---
"Das klingt machbar. Ich probier&#8217;s aus.":
    "That sounds doable. I&#8217;ll give it a try.",
"Genau richtig. Fang mit dem Download-Ordner an.":
    "Just right. Start with the downloads folder.",
"<b>Umschalten</b> &#8211; im Eingabefeld von Chat auf Cowork":
    "<b>Switch</b> &#8211; from Chat to Cowork in the input box",
"<b>Beschreiben</b> &#8211; sag, was herauskommen soll, nicht wie":
    "<b>Describe</b> &#8211; say what should come out, not how",
"<b>Plan ansehen</b> &#8211; Claude zeigt erst, was es vorhat":
    "<b>Read the plan</b> &#8211; Claude shows its intent first",
"<b>Ordner freigeben</b> &#8211; nur den, um den es geht":
    "<b>Share a folder</b> &#8211; only the one it is about",
"<b>Ergebnis</b> &#8211; fertige Tabellen, Folien, Dokumente":
    "<b>Result</b> &#8211; finished spreadsheets, slides, documents",
"<b>Dispatch</b> &#8211; vom Handy aus anstoßen, Rechner muss wach sein":
    "<b>Dispatch</b> &#8211; start it from your phone, computer must be awake",
"<b>Projekte</b> &#8211; getrennte Arbeitsbereiche mit Gedächtnis":
    "<b>Projects</b> &#8211; separate workspaces with a memory",
"<b>Verbindungen</b> &#8211; Drive, Slack und mehr unter „Customize“":
    "<b>Connections</b> &#8211; Drive, Slack and more under &#8220;Customize&#8221;",
"<b>Berechtigungen</b> &#8211; drei Stufen, Du bestimmst":
    "<b>Permissions</b> &#8211; three levels, you decide",
"<b>Nach Zeitplan</b> &#8211; wiederkehrende Aufgaben unter „Scheduled“":
    "<b>On a schedule</b> &#8211; recurring jobs under &#8220;Scheduled&#8221;",
"<b>Vorsicht</b> &#8211; fremde Inhalte, Finanzen, Zugangsdaten":
    "<b>Careful</b> &#8211; outside content, finances, credentials",
"<b>Cowork oder Code</b> &#8211; Dateien oder Quelltext":
    "<b>Cowork or Code</b> &#8211; files or source code",
}

TITEL = "Claude Cowork – the guide"
