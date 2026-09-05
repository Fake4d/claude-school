# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg} eine Nullrunde: <code>claude --help</code> ist zeichengleich geblieben, ebenso
die Hilfe der Unterbefehle. Auch die Liste der Slash-Befehle ist unverändert, weiterhin
{n_slash} Einträge, keine neuen, keine weggefallenen, keine inhaltlich geänderten Beschreibungen.
Bei 32 Befehlen änderten sich lediglich rein interne Bezeichner, ohne Bedeutung für diese Liste.</p>
"""

EN = """
<p>Compared with {vorg}, a quiet release: <code>claude --help</code> is unchanged down to the
character, and so is the subcommand help. The slash command list is unchanged as well, still
{n_slash} entries, none added, none removed, no descriptions changed in substance. For 32 commands
only purely internal identifiers changed, of no consequence for this list.</p>
"""
