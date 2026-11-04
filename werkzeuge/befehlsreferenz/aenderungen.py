# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <b>Ein neuer Slash-Befehl.</b> Die Hilfe von <code>claude</code> und die
Hilfe der Unterbefehle sind zeichengleich; es gibt keine neuen oder weggefallenen Optionen oder Unterbefehle.</p>
<p><b>Neu:</b> <code>/project</code> – legt das claude.ai-Projekt fest, dem die Nutzungsberichte dieser Sitzung zugeordnet werden.</p>
<p>Weggefallen ist kein Befehl, und bei keinem bestehenden Befehl hat sich die Beschreibung inhaltlich geändert.</p>
"""

EN = """
<p>Compared with {vorg}: <b>one new slash command.</b> The help of <code>claude</code> and the
help of the subcommands are character-for-character identical; there are no new or removed options or subcommands.</p>
<p><b>New:</b> <code>/project</code> – sets the claude.ai Project for this session’s usage reports.</p>
<p>No command was removed, and no existing command’s description changed in substance.</p>
"""
