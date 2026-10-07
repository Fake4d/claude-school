# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: Inhaltlich hat sich nichts geändert. Es gibt keine neuen oder weggefallenen Befehle; die Zahl der
Slash-Befehle bleibt bei 139. Auch <code>claude --help</code> und die Hilfe der Unterbefehle sind zeichengleich
geblieben.</p>
<p>Die einzigen Unterschiede betrafen interne, minifizierte Bezeichner bei 43 Befehlen und sind für den Leser ohne
Bedeutung. Diese Fassung trägt daher nur den neuen Versionsstempel.</p>
"""

EN = """
<p>Compared with {vorg}: nothing has changed in substance. No commands were added or removed; the number of slash
commands stays at 139. <code>claude --help</code> and the help of the subcommands are also character-for-character
identical.</p>
<p>The only differences were internal, minified identifiers for 43 commands and mean nothing to the reader. This
edition therefore only carries the new version stamp.</p>
"""
