# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <b>Weggefallen sind <code>/artifact-components</code>, <code>/prototype</code> und
<code>/workshop</code></b>, drei eingebaute Hilfen zum Bauen von Artifact-Seiten (Bausteinkasten, Prototyp aus einer Idee,
gemeinsamer Entwurf Schritt für Schritt). Sie fehlen seit 2.1.312 ersatzlos und stehen auch nicht mehr im Programm. Der
Changelog erwähnt das nicht. Die übrigen Artifact-Befehle bleiben.</p>
<p><b>Genauer beschrieben:</b> <code>claude purge</code> löscht laut Hilfe die Daten eines Projekts nur auf diesem
Rechner, samt Eintrag in <code>~/.claude.json</code>. <code>/limit-reset</code> und <code>/low-priority</code> sprechen jetzt
vom 5-Stunden-Limit statt vom Sitzungslimit. Gemeint ist dasselbe. Sonst gibt es keine neuen Befehle oder Optionen.</p>
"""

EN = """
<p>Compared with {vorg}: <b><code>/artifact-components</code>, <code>/prototype</code> and <code>/workshop</code> have
been removed</b>, three built-in helpers for building artifact pages (component kit, prototype from an idea, step-by-step
joint design). They have been gone since 2.1.312 without replacement and are no longer in the program. The changelog does
not mention it. The other artifact commands remain.</p>
<p><b>Clarified:</b> according to its help, <code>claude purge</code> deletes a project's data on this computer only,
including its entry in <code>~/.claude.json</code>. <code>/limit-reset</code> and <code>/low-priority</code> now speak of the
5-hour limit instead of the session limit; it is the same limit. Otherwise there are no new commands or options.</p>
"""
