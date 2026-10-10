# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: Inhaltlich hat sich nichts geändert. Es gibt keine neuen oder weggefallenen Befehle; die Zahl der
Slash-Befehle bleibt bei 139, und keine Beschreibung wurde geändert. Auch <code>claude --help</code> und die Hilfe der
Unterbefehle sind zeichengleich geblieben.</p>
<p>Geändert haben sich nur interne, minifizierte Bezeichner bei 43 Befehlen, die für den Leser ohne Bedeutung sind.
Diese Fassung hebt lediglich den Versionsstempel an.</p>
"""

EN = """
<p>Compared with {vorg}: nothing changed in substance. No commands were added or removed; the number of slash commands
stays at 139, and no description changed. <code>claude --help</code> and the help of the subcommands are also
character-for-character identical.</p>
<p>Only internal, minified identifiers changed for 43 commands, which mean nothing to the reader. This release merely
raises the version stamp.</p>
"""
