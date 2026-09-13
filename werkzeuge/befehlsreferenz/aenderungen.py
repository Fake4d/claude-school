# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: eine Nullrunde. <code>claude --help</code> und die Hilfe der Unterbefehle sind
zeichengleich geblieben. Bei den Slash-Befehlen ist die Zahl mit 139 gleich geblieben — kein
Befehl kam hinzu, keiner ist weggefallen, und bei keinem hat sich die Beschreibung geändert. Bei 6
Befehlen haben sich nur interne, nicht sichtbare Bezeichner geändert; das betrifft niemanden, der
die Referenz liest. Diese Fassung dokumentiert also ausschließlich den Versionssprung von
{vorg} auf {v}.</p>
"""

EN = """
<p>Compared with {vorg}: a no-op release. <code>claude --help</code> and the sub-command help came
out byte-for-byte identical. The slash command count stayed at 139 — no command was added, none
was removed, and no existing command's description changed. 6 commands had only internal,
non-visible identifiers renamed, which has no effect on anyone reading the reference. This
edition therefore documents nothing but the version bump from {vorg} to {v}.</p>
"""
