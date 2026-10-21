# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: Nullrunde. Inhaltlich hat sich nichts geändert. Die Hilfe von <code>claude --help</code> und die
Hilfe der Unterbefehle sind zeichengleich. Die Zahl der Slash-Befehle bleibt bei 138, es gibt keine neuen, keine
weggefallenen und keine, deren Beschreibung sich geändert hat. Bei 42 Befehlen wurden lediglich interne,
minifizierte Bezeichner getauscht – für den Leser ohne Bedeutung.</p>
<p>Hinweis zum Auslesen: Der Befehl <code>/shell_expansion</code> existiert, ließ sich aber nicht auslesen und fehlt
deshalb in dieser Referenz. Das ist ein Ausleseproblem, kein Wegfall.</p>
"""

EN = """
<p>Compared with {vorg}: nothing changed. <code>claude --help</code> and the help of the subcommands are
character-for-character identical. The number of slash commands stays at 138; there are no new ones, none removed,
and none whose description changed. Only internal, minified identifiers were swapped for 42 commands, which means
nothing to the reader.</p>
<p>Note on extraction: the command <code>/shell_expansion</code> exists but could not be read out, so it is missing from
this reference. This is an extraction problem, not a removal.</p>
"""
