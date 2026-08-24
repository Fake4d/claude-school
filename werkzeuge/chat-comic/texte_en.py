# -*- coding: utf-8 -*-
"""English wording for the comic „Claude im Gespräch“.

Key = the German text exactly as it ends up in the built page, value = its
English counterpart. The keys are produced by i18n.einheiten(); if the German
side changes, the build stops and prints the new key, so nothing can silently
stay German.

Keep the inline markup (<b>, <i>, <span class="chip-sub">) identical on both
sides — it carries the layout.
"""

TEXTE = {

# --- Titelseite ---
"Alle reden davon, was Claude alles&nbsp;kann.":
    "Everyone keeps talking about what Claude&nbsp;can do.",
"Ich seh nur ein leeres&nbsp;Textfeld.":
    "All I see is an empty&nbsp;text box.",
"Artifacts": "Artifacts",
"Projekte": "Projects",
"Gedächtnis": "Memory",
"Research": "Research",
"Verbindungen": "Connectors",
"Stile": "Styles",
"Dateien": "Files",
"Sprachmodus": "Voice mode",
"Modelle": "Models",
"Incognito": "Incognito",
"Websuche": "Web search",
"Deine Daten": "Your data",
"Fang einfach an.": "Just start.",

# --- 1 Was das ist ---
"Was ist Claude denn nun – eine Suchmaschine?":
    "So what is Claude, then – a search engine?",
"Nein. Eine Suchmaschine gibt Dir Fundstellen. Claude gibt Dir ein <b>Ergebnis</b>.":
    "No. A search engine gives you places to look. Claude gives you a <b>result</b>.",
"Du beschreibst, was Du brauchst – Claude denkt nach, sucht bei Bedarf nach, rechnet, schreibt und baut Dir das Fertige hin.":
    "You describe what you need – Claude thinks, looks things up if it has to, calculates, writes, and puts the finished thing in front of you.",
"Suchmaschine": "Search engine",
"Deine Frage": "Your question",
"10 blaue Links": "10 blue links",
"Du liest und baust selbst": "You read and build it yourself",
"Claude": "Claude",
"Dein Ziel": "Your goal",
"Das fertige Ergebnis": "The finished result",
"Text, Tabelle, Auswertung, Entwurf": "Text, spreadsheet, analysis, draft",

# --- 2 Anfangen ---
"Und was muss ich dafür installieren?":
    "And what do I have to install for that?",
"Gar nichts. Browser auf, anmelden, lostippen. Es gibt Claude auch als App für den Rechner und fürs Handy – aber nötig ist keine davon.":
    "Nothing at all. Open a browser, sign in, start typing. There are apps for your computer and your phone too – but you need neither.",
"Und Du musst nicht lernen, wie man <i>richtig</i> fragt. Schreib es so hin, wie Du es einem Kollegen sagen würdest.":
    "And you don&#8217;t have to learn how to ask <i>properly</i>. Put it the way you would say it to a colleague.",
"Browser": "Browser",
"Desktop-App": "Desktop app",
"Handy": "Phone",
"Reicht als erste Nachricht:": "Good enough as a first message:",
"„Ich hab hier drei Angebote für eine neue Heizung. Sag mir, worin sie sich unterscheiden und worauf ich achten muss.“":
    "&#8220;I&#8217;ve got three quotes here for a new boiler. Tell me how they differ and what I should watch out for.&#8221;",
"nichts einzurichten, nichts zu lernen": "nothing to set up, nothing to learn",

# --- 3 Dateien hineingeben ---
"Kann ich ihm auch meine eigenen Unterlagen&nbsp;geben?":
    "Can I give it my own documents&nbsp;as well?",
"Ja – zieh sie einfach ins Gespräch. PDFs, Fotos, Tabellen, Textdateien.":
    "Yes – just drag them into the conversation. PDFs, photos, spreadsheets, text files.",
"Claude liest sie und arbeitet damit weiter: zusammenfassen, vergleichen, Zahlen herausziehen, Fragen dazu beantworten.":
    "Claude reads them and works on from there: summarising, comparing, pulling out numbers, answering questions about them.",
"Angebot.pdf": "Quote.pdf",
"Foto.jpg": "Photo.jpg",
"Liste.xlsx": "List.xlsx",
"Notizen.txt": "Notes.txt",
"Zusammenfassung": "Summary",
"Vergleich": "Comparison",
"die Zahlen daraus": "the numbers from it",

# --- 4 Artifacts ---
"Manchmal klappt rechts so ein Fenster auf. Was ist&nbsp;das?":
    "Sometimes a window opens up on the right. What is&nbsp;that?",
"Das ist ein <b>Artifact</b>. Wenn das Ergebnis kein Satz mehr ist, sondern ein Ding, legt Claude es daneben statt mitten ins Gespräch.":
    "That is an <b>artifact</b>. When the result is no longer a sentence but a thing, Claude puts it beside the conversation instead of into it.",
"Ein Dokument, eine Übersicht, ein Schaubild – oder eine kleine Anwendung, die wirklich läuft.":
    "A document, an overview, a diagram – or a small application that actually runs.",
"Im Gespräch": "In the conversation",
"Antwort": "Answer",
"Erklärung": "Explanation",
"Rückfrage": "Follow-up question",
"zum Lesen": "to read",
"Als Artifact": "As an artifact",
"Dokument": "Document",
"Schaubild": "Diagram",
"Kleine Anwendung": "Small application",
"zum Benutzen und Behalten": "to use and to keep",

# --- 5 Artifacts aendern ---
"Und wenn mir etwas daran nicht passt?":
    "And what if I don&#8217;t like something about it?",
"Sagen, was anders soll – Claude baut es um. Text kannst Du auch direkt anfassen: markieren und ändern lassen.":
    "Say what should be different – Claude rebuilds it. You can also touch the text directly: highlight it and have it changed.",
"Jede Fassung bleibt erhalten, Du kannst zurückblättern. Herunterladen geht, und veröffentlichen auch: dann bekommst Du einen Link zum Weitergeben.":
    "Every version is kept, so you can page back. You can download it, and publish it too: then you get a link to pass on.",
"Fassung 1": "Version 1",
"Fassung 2": "Version 2",
"Fassung 3": "Version 3",
"Herunterladen<span class=\"chip-sub\">liegt bei Dir</span>":
    "Download<span class=\"chip-sub\">yours to keep</span>",
"Veröffentlichen<span class=\"chip-sub\">Link zum Teilen</span>":
    "Publish<span class=\"chip-sub\">a link to share</span>",
"nichts geht verloren – Du kannst jederzeit zurück":
    "nothing is lost – you can always go back",

# --- 6 Echte Dateien ---
"Bekomme ich auch eine richtige Excel-Datei?":
    "Do I get a real Excel file too?",
"Ja. Claude kann echte Dateien bauen – Tabellen mit funktionierenden Formeln, Präsentationen, Dokumente, PDFs.":
    "Yes. Claude can build real files – spreadsheets with working formulas, presentations, documents, PDFs.",
"Gebaut wird das in einem abgeschotteten Bereich bei Anthropic, nicht auf Deinem Rechner. Du lädst die fertige Datei herunter.":
    "It is built in a sealed-off area at Anthropic, not on your computer. You download the finished file.",
"Abgeschotteter Bereich": "Sealed-off area",
"Tabelle.xlsx": "Spreadsheet.xlsx",
"Folien.pptx": "Slides.pptx",
"Bericht.docx": "Report.docx",
"Du lädst sie herunter": "You download it",
"an Deine eigenen Ordner kommt Claude hier noch nicht":
    "at this stage Claude cannot reach your own folders yet",

# --- 7 Unterhaltungen ---
"Soll ich alles in ein Gespräch schreiben?":
    "Should I put everything into one conversation?",
"Lieber nicht. Ein Gespräch hat ein Arbeitsgedächtnis, und irgendwann ist es voll – dann wird es zäh und ungenau.":
    "Better not. A conversation has a working memory, and it fills up – then things get sluggish and vague.",
"Faustregel: neues Thema, neues Gespräch. Beim Thema bleiben kostet nichts und macht die Antworten besser.":
    "Rule of thumb: new topic, new conversation. It costs nothing and makes the answers better.",
"Ein Gespräch für alles": "All in one conversation",
"Urlaub": "Holiday",
"Steuer": "Taxes",
"Bewerbung": "Application",
"Rezept": "Recipe",
"verliert den Faden": "loses the thread",
"Ein Thema, ein Gespräch": "One topic each",
"bleibt scharf": "stays sharp",

# --- 8 Gedaechtnis ---
"Fange ich dann jedes Mal wieder bei null&nbsp;an?":
    "So do I start from scratch&nbsp;every time?",
"Nein. Claude merkt sich Dinge über Gespräche hinweg und kann in früheren nachsehen. Du kannst ihm auch sagen „merk Dir das“.":
    "No. Claude remembers things across conversations and can look back at earlier ones. You can also just tell it &#8220;remember that&#8221;.",
"Was gemerkt wurde, kannst Du ansehen, ändern und löschen – oder das Gedächtnis ganz abschalten. Für einmalige Sachen gibt es Incognito: taucht nirgends auf.":
    "What it remembered you can look at, change and delete – or switch memory off entirely. For one-off things there is incognito: it shows up nowhere.",
"Was Du magst": "What you like",
"Woran Du arbeitest": "What you work on",
"Wie Du schreibst": "How you write",
"Ansehen": "Look at it",
"Ändern": "Change it",
"Löschen": "Delete it",
"Ganz aus": "Switch it off",
"Incognito: kein Verlauf, kein Gedächtnis, nichts bleibt":
    "Incognito: no history, no memory, nothing stays",

# --- 9 Projekte ---
"Kann ich das irgendwie ordnen?": "Can I bring some order to this?",
"Dafür gibt es Projekte. Jedes ist ein eigener Arbeitsbereich: eigene Gespräche, eigene Unterlagen, eigene Anweisungen – und ein eigenes Gedächtnis.":
    "That is what projects are for. Each one is its own workspace: its own conversations, its own documents, its own instructions – and its own memory.",
"Einmal hinterlegt, gilt es für alles darin. Du musst nicht in jedem Gespräch neu erklären, worum es geht.":
    "Set it up once and it applies to everything inside. You don&#8217;t have to explain the background again in every conversation.",
"Steuer 2026": "Taxes 2026",
"Deine Belege": "Your receipts",
"„Antworte knapp“": "&#8220;Answer briefly&#8221;",
"eigenes Gedächtnis": "its own memory",
"Verein": "Club",
"Satzung": "Statutes",
"„Immer förmlich“": "&#8220;Always formal&#8221;",
"getrennte Arbeitsbereiche – nichts vermischt sich":
    "separate workspaces – nothing gets mixed up",

# --- 10 Suchen und Nachdenken ---
"Weiß Claude, was gestern passiert&nbsp;ist?":
    "Does Claude know what happened&nbsp;yesterday?",
"Von sich aus nicht – sein Wissen hat einen Stichtag. Aber es kann nachschlagen, und dann nennt es Dir die Quellen.":
    "Not by itself – its knowledge has a cut-off date. But it can look things up, and then it names its sources.",
"Zwei verschiedene Knöpfe: <b>Suchen</b> holt kurz etwas von draußen. <b>Länger nachdenken</b> holt gar nichts, sondern denkt gründlicher – gut für Knobelaufgaben.":
    "Two different buttons: <b>search</b> briefly fetches something from outside. <b>Extended thinking</b> fetches nothing at all but thinks harder – good for puzzles.",
"Suchen": "Search",
"kurz nach draußen": "a quick look outside",
"mit Quellenangabe": "with sources named",
"„Was kostet das gerade?“": "&#8220;What does that cost right now?&#8221;",
"Länger nachdenken": "Extended thinking",
"bleibt drinnen": "stays inside",
"dafür gründlicher": "but goes deeper",
"„Wo ist der Fehler in meiner Rechnung?“":
    "&#8220;Where is the mistake in my calculation?&#8221;",

# --- 11 Research ---
"Und wenn ich es richtig genau wissen&nbsp;will?":
    "And if I want to know it&nbsp;properly?",
"Dann nimm <b>Research</b>. Claude sucht dann selbstständig weiter, folgt Spuren, prüft mehrere Quellen gegeneinander – ein bis drei Minuten lang.":
    "Then use <b>research</b>. Claude keeps searching on its own, follows leads and checks several sources against each other – for one to three minutes.",
"Am Ende steht ein Bericht mit Belegen, keine schnelle Antwort. Für Vergleiche, Marktüberblicke, Entscheidungsvorlagen.":
    "What comes out is a report with evidence, not a quick answer. For comparisons, market overviews, decision papers.",
"sucht": "searches",
"liest": "reads",
"prüft nach": "checks",
"Bericht": "Report",
"dauert 1–3 Minuten": "takes 1–3 minutes",
"mit Quellen zum Nachschlagen": "with sources you can look up",
"für die Fragen, bei denen eine schnelle Antwort nichts taugt":
    "for the questions where a quick answer is no use",

# --- 12 Verbindungen ---
"Kommt es auch an meinen Kalender und meine&nbsp;Mails?":
    "Can it get at my calendar and my&nbsp;mail?",
"Wenn Du es verbindest, ja. Drive, Kalender, Mail und einiges mehr hängst Du unter <b>Customize</b> an.":
    "If you connect it, yes. You attach Drive, calendar, mail and a good deal more under <b>Customize</b>.",
"Danach holt Claude sich die Sachen selbst. Verbinde aber nur, was Du wirklich brauchst – und was Du kennst.":
    "After that Claude fetches things itself. But only connect what you really need – and what you know.",
"Drive": "Drive",
"Kalender": "Calendar",
"Mail": "Mail",
"Slack": "Slack",
"nur anschließen, was Du brauchst – Claude sieht dann, was Du siehst":
    "connect only what you need – Claude then sees what you see",

# --- 13 Antwortstil ---
"Mir ist das immer zu&nbsp;lang.": "It&#8217;s always too&nbsp;long for me.",
"Dann stell den Stil um. Es gibt fertige – knapp, förmlich, erklärend – und Du kannst einen eigenen bauen.":
    "Then change the style. There are ready-made ones – concise, formal, explanatory – and you can build your own.",
"Für einen eigenen gibst Du Claude einfach ein paar Zeilen, die klingen wie Du. Ab dann schreibt es so.":
    "For your own you simply give Claude a few lines that sound like you. From then on it writes that way.",
"<b>Knapp</b><span>kommt sofort zum Punkt</span>":
    "<b>Concise</b><span>gets to the point straight away</span>",
"<b>Erklärend</b><span>nimmt Dich mit, wenn Du es lernen willst</span>":
    "<b>Explanatory</b><span>takes you along when you want to learn</span>",
"<b>Förmlich</b><span>für alles, was nach draußen geht</span>":
    "<b>Formal</b><span>for anything that goes outside the house</span>",
"<b>Dein eigener</b><span>klingt wie Du – aus Deinen Beispielen gebaut</span>":
    "<b>Your own</b><span>sounds like you – built from your examples</span>",

# --- 14 Handy und Sprache ---
"Und unterwegs?": "And when I&#8217;m out?",
"Dasselbe Gespräch, überall: Browser, Rechner-App, Handy. Du machst es auf, wo Du gerade bist.":
    "The same conversation, everywhere: browser, desktop app, phone. You open it wherever you happen to be.",
"Am Handy kannst Du auch einfach reden statt tippen. Praktisch beim Gehen – und beim Sortieren von Gedanken.":
    "On the phone you can simply talk instead of typing. Handy while walking – and for sorting out your thoughts.",
"Tippen": "Typing",
"oder einfach reden": "or simply talking",
"ein Gespräch, egal wo Du es aufmachst":
    "one conversation, wherever you open it",

# --- 15 Modelle ---
"Da steht oben ein Name. Muss ich den&nbsp;ändern?":
    "There&#8217;s a name at the top. Do I have to&nbsp;change it?",
"Meistens nicht. Die Voreinstellung passt für fast alles.":
    "Usually not. The default fits almost everything.",
"Wenn eine Aufgabe wirklich schwer ist, nimm ein stärkeres Modell. Wenn es nur schnell gehen soll, das kleine. Stand August 2026 heißen sie so:":
    "If a job is genuinely hard, take a stronger model. If it just has to be quick, take the small one. As of August 2026 they are called:",
"<b>Fable 5</b><span>das stärkste</span><i>nicht überall enthalten</i>":
    "<b>Fable 5</b><span>the strongest</span><i>not on every plan</i>",
"<b>Opus 5</b><span>die schweren Sachen</span><i>denkt gründlich</i>":
    "<b>Opus 5</b><span>the heavy jobs</span><i>thinks thoroughly</i>",
"<b>Sonnet 5</b><span>der Alltag</span><i>die Voreinstellung</i>":
    "<b>Sonnet 5</b><span>everyday work</span><i>the default</i>",
"<b>Haiku 4.5</b><span>schnell &amp; günstig</span><i>für Kurzes</i>":
    "<b>Haiku 4.5</b><span>fast &amp; cheap</span><i>for short things</i>",
"im Zweifel: einfach lassen": "when in doubt: leave it alone",

# --- 16 Gut fragen ---
"Wie sage ich es denn am&nbsp;besten?": "How do I best&nbsp;put it?",
"Sag das Ziel, nicht die Schritte – den Weg findet Claude selbst. Und sag dazu, woran man merkt, dass es fertig ist.":
    "State the goal, not the steps – Claude finds the way itself. And say how you can tell when it is done.",
"Gib den Zusammenhang mit: für wen, wofür, und was auf keinen Fall passieren darf. Je klarer der Auftrag, desto weniger Runden.":
    "Give the context: who it is for, what for, and what must not happen. The clearer the task, the fewer rounds.",
"eher nicht": "rather not",
"„Schreib was zu unserem Sommerfest.“":
    "&#8220;Write something about our summer party.&#8221;",
"besser": "better",
"„Eine Einladung zum Sommerfest für die Nachbarschaft, höchstens eine halbe Seite, freundlich aber nicht albern. Termin und Anmeldung müssen drinstehen.“":
    "&#8220;An invitation to the summer party for the neighbours, half a page at most, friendly but not silly. Date and how to sign up must be in there.&#8221;",

# --- 17 Nachpruefen ---
"Kann ich mich denn darauf&nbsp;verlassen?": "Can I actually&nbsp;rely on it?",
"Meistens ja – aber Claude kann sich auch überzeugend irren, und es klingt dabei genauso sicher wie sonst.":
    "Usually yes – but Claude can also be convincingly wrong, and it sounds just as certain as ever while doing it.",
"Deshalb: Bei allem, was zählt, nach der Quelle fragen. Und Zahlen lieber nachrechnen lassen, als sie zu glauben.":
    "So: for anything that matters, ask where it came from. And have numbers worked out again rather than believing them.",
"Quelle nennen lassen<span class=\"chip-sub\">woher stammt das?</span>":
    "Ask for the source<span class=\"chip-sub\">where is that from?</span>",
"Zahlen nachrechnen<span class=\"chip-sub\">Schritt für Schritt</span>":
    "Redo the arithmetic<span class=\"chip-sub\">step by step</span>",
"Bei Wichtigem: gegenlesen<span class=\"chip-sub\">Vertrag, Bewerbung, Arzt</span>":
    "When it matters: read it over<span class=\"chip-sub\">contracts, applications, health</span>",
"je wichtiger die Sache, desto kürzer die Leine":
    "the more it matters, the shorter the leash",

# --- 18 Fremde Inhalte ---
"Und wenn in einem PDF steht „lösche&nbsp;alles“?":
    "And if a PDF says &#8220;delete&nbsp;everything&#8221;?",
"Gute Frage – da liegt die Stolperfalle. Claude liest Webseiten, Mails und fremde Dokumente. <b>Nichts davon ist ein Auftrag von Dir.</b>":
    "Good question – that is where the trap is. Claude reads web pages, e-mails and other people&#8217;s documents. <b>None of that is an instruction from you.</b>",
"Aufträge kommen von Dir. Alles andere ist Material zum Lesen. Deshalb: bei Fremdem genauer hinsehen, was am Ende herauskommt.":
    "Instructions come from you. Everything else is material to read. So with anything from outside, look more closely at what comes out.",
"Deine Anweisung<span class=\"chip-sub\">zählt</span>":
    "Your instruction<span class=\"chip-sub\">counts</span>",
"Dein Projekt<span class=\"chip-sub\">zählt</span>":
    "Your project<span class=\"chip-sub\">counts</span>",
"Webseite<span class=\"chip-sub\">nur Material</span>":
    "Web page<span class=\"chip-sub\">material only</span>",
"E-Mail<span class=\"chip-sub\">nur Material</span>":
    "E-mail<span class=\"chip-sub\">material only</span>",
"fremdes PDF<span class=\"chip-sub\">nur Material</span>":
    "someone&#8217;s PDF<span class=\"chip-sub\">material only</span>",
"was drinsteht, wird gelesen – nicht befolgt":
    "what it says gets read – not obeyed",

# --- 19 Deine Daten ---
"Was passiert eigentlich mit dem, was ich&nbsp;schreibe?":
    "What actually happens to what I&nbsp;write?",
"Das steht in den Einstellungen, und Du entscheidest es. Dort legst Du fest, ob Deine Gespräche zur Verbesserung von Claude verwendet werden dürfen.":
    "That is in the settings, and you decide it. There you set whether your conversations may be used to improve Claude.",
"Incognito-Gespräche werden nie dafür verwendet – und landen auch nicht im Verlauf. Für heikle Sachen gilt trotzdem: nur hineingeben, was Du auch einem Dienstleister geben würdest.":
    "Incognito conversations are never used for it – and never appear in your history either. For delicate matters the rule still holds: only put in what you would also hand to a service provider.",
"<b>Einstellungen</b><span>Du bestimmst, ob Gespräche zur Verbesserung genutzt werden</span>":
    "<b>Settings</b><span>you decide whether conversations are used for improvement</span>",
"<b>Incognito</b><span>kein Verlauf, kein Gedächtnis, nie fürs Training</span>":
    "<b>Incognito</b><span>no history, no memory, never for training</span>",
"<b>Trotzdem gilt</b><span>Zugangsdaten und fremde Geheimnisse gehören nirgends hinein</span>":
    "<b>Still true</b><span>credentials and other people&#8217;s secrets belong nowhere near it</span>",

# --- 20 Die drei Stufen ---
"Und wenn ich mehr&nbsp;will?": "And if I want&nbsp;more?",
"Dann geht es in Stufen weiter – die Frage ist immer, wie weit Du Claude an Deine Sachen lässt.":
    "Then it goes on in stages – the question is always how far you let Claude at your things.",
"Hier, im Gespräch, geht alles durch Dich hindurch: Du gibst hinein, Du nimmst heraus. Das reicht für erstaunlich viel.":
    "Here, in the conversation, everything passes through you: you put in, you take out. That covers an astonishing amount.",
"<b>1 · Im Gespräch</b><span>nichts einzurichten – Du lädst hoch, Du lädst herunter</span>":
    "<b>1 · In the conversation</b><span>nothing to set up – you upload, you download</span>",
"<b>2 · Cowork</b><span>Claude arbeitet direkt in Deinen Ordnern</span>":
    "<b>2 · Cowork</b><span>Claude works directly in your folders</span>",
"<b>3 · Claude Code</b><span>Terminal: Claude arbeitet auf dem ganzen Rechner – und läuft ohne Dich weiter</span>":
    "<b>3 · Claude Code</b><span>terminal: Claude works on the whole machine – and keeps running without you</span>",
"für Stufe 2 und 3 gibt es je ein eigenes Heft":
    "stages 2 and 3 each have a booklet of their own",

# --- 21 Fazit ---
"Ohh. Das ist ja gar nicht so&nbsp;wild.": "Oh. That&#8217;s not so&nbsp;bad after all.",
"Eben. Fang mit einer echten Aufgabe an, nicht mit einem Test.":
    "Exactly. Start with a real job, not with a test.",
"""
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
<b>Weiterlernen</b> &#8211; kostenlose Kurse auf academy.claude.com<br>
<b>Weiter geht&#8217;s</b> &#8211; Cowork für Deine Ordner, Code für den ganzen Rechner
""":
"""
<b>Artifacts</b> &#8211; when Claude builds something instead of describing it<br>
<b>Files</b> &#8211; drag them in, get real files back<br>
<b>Conversations</b> &#8211; new topic, new conversation<br>
<b>Memory</b> &#8211; it remembers things, and you can switch it off<br>
<b>Projects</b> &#8211; separate workspaces with their own rules<br>
<b>Search &amp; research</b> &#8211; the quick grab and the long report<br>
<b>Connectors</b> &#8211; Drive, calendar, mail under &#8220;Customize&#8221;<br>
<b>Style</b> &#8211; concise, formal, explanatory or your own<br>
<b>Asking well</b> &#8211; state the goal, not the steps<br>
<b>Checking</b> &#8211; sounding certain is not the same as being right<br>
<b>Outside content</b> &#8211; it gets read, not obeyed<br>
<b>Keep learning</b> &#8211; free courses at academy.claude.com<br>
<b>What&#8217;s next</b> &#8211; Cowork for your folders, Code for the whole machine
""",
}

TITEL = "Claude in conversation – the guide"
