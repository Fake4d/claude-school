# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <b>Zwei Slash-Befehle sind weggefallen.</b> Die Hilfe von <code>claude</code> und die
Hilfe der Unterbefehle sind zeichengleich; es gibt keine neuen oder weggefallenen Optionen oder Unterbefehle.</p>
<p><b>Weg:</b> <code>/claim-credit</code> (öffnete die Seite des beim Start angezeigten Angebots) und
<code>/memory-types</code> (Nachschlagewerk zu den Gedächtnisarten). Beide sind ersatzlos entfallen, nicht umbenannt;
der offizielle Changelog erwähnt das nicht.</p>
<p>Neue Befehle gibt es keine, und bei keinem bestehenden Befehl hat sich die Beschreibung inhaltlich geändert.</p>
"""

EN = """
<p>Compared with {vorg}: <b>two slash commands were removed.</b> The help of <code>claude</code> and the
help of the subcommands are character-for-character identical; there are no new or removed options or subcommands.</p>
<p><b>Removed:</b> <code>/claim-credit</code> (opened the page of the offer shown at start-up) and
<code>/memory-types</code> (reference on the kinds of memory). Both are gone without replacement, not renamed;
the official changelog does not mention it.</p>
<p>There are no new commands, and no existing command’s description changed in substance.</p>
"""
