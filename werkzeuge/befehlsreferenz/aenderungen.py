# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: Neue oder weggefallene Befehle gibt es nicht; die Zahl der Slash-Befehle bleibt bei 139.
Geändert hat sich Folgendes:</p>
<ul>
<li><code>claude attach</code> und <code>claude logs</code> akzeptieren jetzt statt der ID auch den Namen der
Hintergrundsitzung (<code>&lt;id|name&gt;</code>); ein Teil des Namens genügt. Namen mit Leerzeichen gehören in
Anführungszeichen.</li>
<li>Die Beschreibung von <code>/code-review</code> fasst die Stufen der Prüftiefe knapper (von wenigen, sicheren
Befunden bis zu vielen, teils unsicheren). Die Funktion selbst bleibt gleich.</li>
</ul>
<p>Sonst nichts: Die übrigen Änderungen betrafen nur interne, minifizierte Bezeichner bei 42 Befehlen und sind für den
Leser ohne Bedeutung.</p>
"""

EN = """
<p>Compared with {vorg}: no commands were added or removed; the number of slash commands stays at 139.
What changed:</p>
<ul>
<li><code>claude attach</code> and <code>claude logs</code> now accept the name of the background session
instead of the ID (<code>&lt;id|name&gt;</code>); part of the name is enough. Names with spaces must be quoted.</li>
<li>The description of <code>/code-review</code> words the effort levels more briefly (from few high-confidence
findings up to many, some uncertain). The feature itself is unchanged.</li>
</ul>
<p>Nothing else: the remaining differences were only internal, minified identifiers for 42 commands and mean nothing
to the reader.</p>
"""
