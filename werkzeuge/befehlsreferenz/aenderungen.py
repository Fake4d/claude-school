# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <b>Ein neuer Slash-Befehl, eine geänderte Beschreibung.</b> Die Hilfe von <code>claude</code> und die
Hilfe der Unterbefehle sind zeichengleich; es gibt keine neuen oder weggefallenen Optionen oder Unterbefehle.</p>
<p><b>Neu:</b> <code>/use-case</code> – wählt den Life-Sciences-Anwendungsfall, der zu den eigenen Anfragen passt.</p>
<p><b>Beschreibung geändert:</b> <code>/upgrade</code> – bisher „Auf Max wechseln für höhere Grenzen und mehr Opus“,
jetzt „Den Tarif wechseln für höhere Grenzen und mehr Opus“. Weggefallen ist kein Befehl.</p>
"""

EN = """
<p>Compared with {vorg}: <b>one new slash command, one changed description.</b> The help of <code>claude</code> and the
help of the subcommands are character-for-character identical; there are no new or removed options or subcommands.</p>
<p><b>New:</b> <code>/use-case</code> – choose the Life Sciences use case that applies to your requests.</p>
<p><b>Description changed:</b> <code>/upgrade</code> – previously “Move to Max for higher limits and more Opus”, now
“Change your plan for higher limits and more Opus”. No command was removed.</p>
"""
