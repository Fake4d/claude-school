# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: eine Nullrunde. <code>claude --help</code> und die Hilfe der Unterbefehle sind
zeichengleich geblieben, und bei den 138 Slash-Befehlen hat sich inhaltlich nichts getan — weder
neue noch weggefallene Befehle, keine geänderten Beschreibungen. Bei 37 Befehlen haben sich nur
interne, nicht sichtbare Bezeichner geändert; das betrifft niemanden, der die Referenz liest.</p>
"""

EN = """
<p>Compared with {vorg}: a no-op release. <code>claude --help</code> and the sub-command help
came out byte-for-byte identical, and among the 138 slash commands nothing changed in substance —
no additions, no removals, no description changes. 37 commands had only internal, non-visible
identifiers renamed, which has no effect on anyone reading the reference.</p>
"""
