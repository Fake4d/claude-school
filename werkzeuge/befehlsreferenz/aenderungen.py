# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <b>eine geänderte Beschreibung bei <code>/schedule</code>; sonst nichts Inhaltliches.</b></p>
<ul>
<li><code>/schedule</code>: Die Beschreibung lautet jetzt „Create and manage scheduled tasks that run in the cloud“ (vorher: „Create and manage scheduled remote Claude Code agents“). Gemeint ist weiterhin das Anlegen und Verwalten geplanter Aufgaben, die in der Cloud laufen.</li>
</ul>
<p><code>claude --help</code> und die Hilfe der Unterbefehle sind zeichengleich. Slash-Befehle: weiterhin 136 (keiner neu, keiner weg).</p>
"""

EN = """
<p>Compared with {vorg}: <b>one changed description for <code>/schedule</code>; nothing else of substance.</b></p>
<ul>
<li><code>/schedule</code>: the description now reads “Create and manage scheduled tasks that run in the cloud” (before: “Create and manage scheduled remote Claude Code agents”). It still means creating and managing scheduled tasks that run in the cloud.</li>
</ul>
<p><code>claude --help</code> and the subcommand help are character-for-character identical. Slash commands: still 136 (none new, none removed).</p>
"""
