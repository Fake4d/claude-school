# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: Es gibt keine neuen oder weggefallenen Befehle; die Zahl der Slash-Befehle bleibt bei 139. Die
Ausgabe von <code>claude --help</code> und die Hilfe der Unterbefehle sind zeichengleich geblieben.</p>
<p>Einzige inhaltliche Änderung: Bei <code>/resume</code> wird kein Argument-Hinweis mehr angezeigt; zuvor lautete er
„[conversation id or search term]“.</p>
<p>Geändert haben sich außerdem nur interne, minifizierte Bezeichner bei 40 Befehlen, die für den Leser ohne Bedeutung
sind.</p>
<p>Hinweis zum Auslesen: Der Befehl <code>/shell_expansion</code> existiert, ließ sich aber nicht auslesen und fehlt
deshalb in dieser Referenz. Das ist ein Ausleseproblem, kein Wegfall und keine inhaltliche Änderung.</p>
"""

EN = """
<p>Compared with {vorg}: no commands were added or removed; the number of slash commands stays at 139. The output of
<code>claude --help</code> and the help of the subcommands are character-for-character identical.</p>
<p>The only change in substance: <code>/resume</code> no longer shows an argument hint; it used to read
“[conversation id or search term]”.</p>
<p>Otherwise only internal, minified identifiers changed for 40 commands, which mean nothing to the reader.</p>
<p>Note on extraction: the command <code>/shell_expansion</code> exists but could not be read out, so it is missing from
this reference. This is an extraction problem, not a removal and not a change in substance.</p>
"""
