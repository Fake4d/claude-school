# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg} eine Nullrunde: Kein Slash-Befehl kommt hinzu, keiner fällt weg — es bleibt
bei {n_slash} Befehlen — und keine Kurzbeschreibung hat sich inhaltlich geändert. Bei 37
Slash-Befehlen haben sich lediglich rein interne Bezeichner geändert, ohne jede Bedeutung für
diese Liste.</p>
<p>Auch bei den Terminal-Optionen (Teil A) ist <code>claude --help</code> zeichengleich zu
{vorg}, und die Hilfe der Unterbefehle (Teil B) ist ebenfalls unverändert. Diese Fassung
dokumentiert damit ausschließlich den Versionssprung von {vorg} auf {v}.</p>
"""

EN = """
<p>Compared with {vorg} this is a null round: no slash command is added, none is dropped — the
count stays at {n_slash} — and no short description changed in substance. For 37 slash commands
only purely internal identifiers changed, of no consequence for this list.</p>
<p>Among the terminal options (part A), <code>claude --help</code> is character-for-character
identical to {vorg}, and the subcommand help (part B) is unchanged as well. This edition
therefore documents nothing but the version bump from {vorg} to {v}.</p>
"""
