# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Eine Nullrunde: Gegenüber {vorg} hat sich inhaltlich nichts geändert.</p>
<p>Bei den Terminal-Optionen (Teil A) ist <code>claude --help</code> zeichengleich zu {vorg}.
Auch die Hilfe der Unterbefehle (Teil B) ist zeichengleich.</p>
<p>Bei den Slash-Befehlen (Teil C) hat sich die Zahl nicht geändert: {n_slash} Einträge wie
zuvor, keiner ist dazugekommen oder weggefallen, keine Kurzbeschreibung wurde inhaltlich
geändert. Bei 35 Befehlen haben sich rein interne Bezeichner geändert — ohne Bedeutung für
diese Liste.</p>
"""

EN = """
<p>A no-op release: nothing changed in substance compared with {vorg}.</p>
<p>Among the terminal options (part A), <code>claude --help</code> is character-for-character
identical to {vorg}. The subcommand help (part B) is likewise identical.</p>
<p>Among the slash commands (part C) the count is unchanged: {n_slash} entries as before,
none added, none dropped, no short description changed in substance. For 35 commands purely
internal identifiers changed — of no consequence for this list.</p>
"""
