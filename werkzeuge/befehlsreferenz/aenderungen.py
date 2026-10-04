# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: Inhaltlich hat sich nichts geändert. <code>claude --help</code> und die Hilfe
aller Unterbefehle sind zeichengleich, bei den 139 Slash-Befehlen gibt es keine neuen, keine
weggefallenen und keine inhaltlich geänderten. Geändert haben sich nur interne, minifizierte
Bezeichner bei 34 Befehlen; für den Leser ist das ohne Bedeutung. Diese Fassung hebt nur den
Versionsstempel an.</p>
"""

EN = """
<p>Compared with {vorg}: nothing has changed in substance. <code>claude --help</code> and the help
of all sub-commands are character-identical, and of the 139 slash commands none is new, none was
removed and none changed in content. Only internal, minified identifiers changed for 34 commands;
this means nothing to the reader. This edition only bumps the version stamp.</p>
"""
