# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: Inhaltlich hat sich nichts geändert. Es gibt keine neuen oder weggefallenen Befehle; die Zahl der
Slash-Befehle bleibt bei 139, und keine Beschreibung eines Slash-Befehls wurde geändert. Die Hilfe der Unterbefehle ist
zeichengleich geblieben.</p>
<p>Einzige Abweichung in <code>claude --help</code>: Im Hilfetext zu <code>--restricted</code> wird bei den entfernten,
Code ausführenden Werkzeugen „REPL“ nicht mehr namentlich genannt; der übrige Wortlaut ist gleich. Ein neuer oder
geänderter Schalter ist das nicht.</p>
<p>Geändert haben sich außerdem nur interne, minifizierte Bezeichner bei 44 Befehlen, die für den Leser ohne Bedeutung
sind.</p>
<p>Hinweis zum Auslesen: Der Befehl <code>/unmarked</code> existiert, ließ sich aber nicht auslesen und fehlt deshalb in
dieser Referenz. Das ist ein Ausleseproblem, kein Wegfall und keine inhaltliche Änderung.</p>
"""

EN = """
<p>Compared with {vorg}: nothing changed in substance. No commands were added or removed; the number of slash commands
stays at 139, and no slash command description changed. The help of the subcommands is character-for-character
identical.</p>
<p>The only difference in <code>claude --help</code>: the help text for <code>--restricted</code> no longer names “REPL”
among the code-running tools it removes; the rest of the wording is the same. This is not a new or changed option.</p>
<p>Otherwise only internal, minified identifiers changed for 44 commands, which mean nothing to the reader.</p>
<p>Note on extraction: the command <code>/unmarked</code> exists but could not be read out, so it is missing from this
reference. This is an extraction problem, not a removal and not a change in substance.</p>
"""
