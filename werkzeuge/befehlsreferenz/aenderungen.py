# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg} eine Nullrunde: Die Hilfe zu <code>claude --help</code> und die Hilfe der
Unterbefehle sind zeichengleich geblieben. Bei den Slash-Befehlen bleibt die Liste unverändert bei
{n_slash} Einträgen — kein Befehl kam hinzu, keiner fiel weg, und inhaltlich hat sich an keinem
etwas geändert. Bei 12 Befehlen haben sich lediglich rein interne Bezeichner geändert, ohne jede
Bedeutung für diese Liste. Diese Fassung unterscheidet sich von {vorg} damit nur im
Versionsstempel.</p>
"""

EN = """
<p>Compared with {vorg} this is a no-op release: the help for <code>claude --help</code> and the
subcommand help remain character-for-character identical. The slash command list stays unchanged
at {n_slash} entries — none added, none dropped, and nothing changed in substance for any of them.
For 12 commands only purely internal identifiers changed, of no consequence for this list. This
release differs from {vorg} only in its version stamp.</p>
"""
