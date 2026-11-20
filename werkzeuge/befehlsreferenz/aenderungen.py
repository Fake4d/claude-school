# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <b>ein Befehl ist weggefallen, der ohnehin nie nutzbar war; sonst nur kleine Textänderungen.</b></p>
<ul>
<li><code>/loops</code> ist aus dem Programm entfernt. Der Befehl war schon vorher fest abgeschaltet (er stand hier im Anhang „Angelegt, aber abgeschaltet“), für Nutzer ändert sich also nichts. Wiederkehrende Aufgaben laufen weiter über <code>/loop</code>.</li>
<li><code>/clear</code>: Die Beschreibung sagt jetzt, dass laufende Loops in die neue Sitzung mitgenommen werden; die alte Sitzung bleibt über <code>/resume</code> erreichbar.</li>
<li><code>/teleport</code>: Die Beschreibung lautet nur noch „Resume a cloud session here“ (vorher auch „Send this session to the cloud“).</li>
<li><code>/tasks</code>: zeigt laut Beschreibung jetzt „die Hintergrundarbeit dieser Sitzung“ statt „alles, was im Hintergrund läuft“.</li>
<li><code>/code-review</code>: Neben Fehlern meldet es nun auch verletzte CLAUDE.md-Regeln (statt „Wiederverwendung/Vereinfachung/Effizienz“).</li>
<li><code>claude --help</code>: <code>--name</code> benennt auch eine neue Cloud-Sitzung; <code>--restricted</code> startet zusätzlich keine Plugin-Sprachserver.</li>
</ul>
<p>Slash-Befehle: 134 statt 135 (einer weg, keiner neu); nutzbar sind unverändert 131.</p>
"""

EN = """
<p>Compared with {vorg}: <b>one command was removed that was never usable anyway; otherwise only small text changes.</b></p>
<ul>
<li><code>/loops</code> has been removed from the program. It was already permanently disabled (listed here in the appendix “Present, but switched off”), so nothing changes for users. Recurring tasks still run via <code>/loop</code>.</li>
<li><code>/clear</code>: the description now says that running loops carry over into the new session; the old session stays available via <code>/resume</code>.</li>
<li><code>/teleport</code>: the description now reads only “Resume a cloud session here” (previously also “Send this session to the cloud”).</li>
<li><code>/tasks</code>: now described as showing “this session's background work” instead of “everything running in the background”.</li>
<li><code>/code-review</code>: besides bugs it now also reports broken CLAUDE.md rules (instead of “reuse/simplification/efficiency”).</li>
<li><code>claude --help</code>: <code>--name</code> also names a new cloud session; <code>--restricted</code> additionally starts no plugin language servers.</li>
</ul>
<p>Slash commands: 134 instead of 135 (one removed, none new); still 131 usable.</p>
"""
