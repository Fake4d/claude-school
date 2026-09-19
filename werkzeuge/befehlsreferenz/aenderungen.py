# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <code>claude --help</code> und die Hilfe der Unterbefehle sind zeichengleich
geblieben. Bei den Slash-Befehlen ist keiner hinzugekommen, keiner weggefallen, und bei keinem
Befehl hat sich die Beschreibung inhaltlich geändert. Bei 21 Befehlen haben sich nur interne,
minifizierte Bezeichner geändert; das betrifft niemanden, der die Referenz liest. Diese Fassung
dokumentiert also lediglich den Versionssprung von {vorg} auf {v} – inhaltlich hat sich nichts
geändert.</p>
"""

EN = """
<p>Compared with {vorg}: <code>claude --help</code> and the sub-command help came out
byte-for-byte identical. No slash command was added, none was removed, and no command changed its
description in substance. 21 commands had only internal, minified identifiers renamed, which has
no effect on anyone reading the reference. This edition therefore merely documents the version
bump from {vorg} to {v} – nothing has changed in substance.</p>
"""
