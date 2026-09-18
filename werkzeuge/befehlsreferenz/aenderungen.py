# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <code>claude --help</code> und die Hilfe der Unterbefehle sind zeichengleich
geblieben. Bei den Slash-Befehlen ist ein Befehl hinzugekommen, keiner ist weggefallen, und bei
keinem bestehenden Befehl hat sich die Beschreibung inhaltlich geändert. Neu ist
<code>/claim-credit</code>: Er öffnet die Seite des Angebots, das beim Start angezeigt wird, und
ist nur unter bestimmten Bedingungen verfügbar. Bei 37 Befehlen haben sich nur interne,
minifizierte Bezeichner geändert; das betrifft niemanden, der die Referenz liest. Diese Fassung
dokumentiert also den Versionssprung von {vorg} auf {v} mit genau einem neuen Befehl und sonst
keiner inhaltlichen Änderung.</p>
"""

EN = """
<p>Compared with {vorg}: <code>claude --help</code> and the sub-command help came out
byte-for-byte identical. One slash command was added, none was removed, and no existing command
changed its description in substance. The new one is <code>/claim-credit</code>: it opens the page
of the offer shown at start-up, and it is only available under certain conditions. 37 commands had
only internal, minified identifiers renamed, which has no effect on anyone reading the reference.
This edition therefore documents the version bump from {vorg} to {v} with exactly one new command
and no other change in substance.</p>
"""
