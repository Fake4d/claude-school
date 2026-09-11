# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: ein neuer Slash-Befehl, <code>/output-style</code> (Ausgabestile auflisten
oder zu einem wechseln) — damit stehen jetzt 139 Slash-Befehle in der Referenz. Kein Befehl ist
weggefallen, und bei keinem bestehenden Befehl hat sich die Beschreibung geändert. Bei 37 Befehlen
haben sich nur interne, nicht sichtbare Bezeichner geändert; das betrifft niemanden, der die
Referenz liest.</p>
<p><code>claude --help</code> ist zeichengleich geblieben. Bei der Hilfe der Unterbefehle gibt es
eine inhaltliche Änderung: <code>claude plugin eval</code> beschreibt jetzt ausführlicher, was der
Befehl tut und worauf zu achten ist — er lädt das Plugin und lässt seine Eval-Suite (Prompts,
Grader; Gerüstskripte und echte MCP-Server nur nach Zustimmung) auf der eigenen Maschine laufen,
weshalb nur Plugins ausgewertet werden sollten, denen man vertraut. Der erste Lauf in einem nicht
vertrauten Plugin-Ordner fragt nach Bestätigung (<code>--trust-plugin</code> beantwortet das für
CI).</p>
"""

EN = """
<p>Compared with {vorg}: one new slash command, <code>/output-style</code> (list output styles or
switch to one) — the reference now lists 139 slash commands. No command was removed, and no
existing command's description changed. 37 commands had only internal, non-visible identifiers
renamed, which has no effect on anyone reading the reference.</p>
<p><code>claude --help</code> came out byte-for-byte identical. The sub-command help has one
substantive change: <code>claude plugin eval</code> now describes in more detail what the command
does and what to watch for — it loads the plugin and runs its eval suite (prompts, graders;
scaffold scripts and real MCP servers only when you opt in) on your own machine, so only plugins
you trust should be evaluated. The first run in an untrusted plugin directory asks for
confirmation (<code>--trust-plugin</code> answers that for CI).</p>
"""
