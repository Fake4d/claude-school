# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <b>Inhaltlich hat sich nichts geändert.</b> Es gibt keine neuen und keine weggefallenen
Befehle, Optionen oder Unterbefehle; auch die Beschreibungen der Slash-Befehle sind unverändert.</p>
<p><b>Einzige Abweichung:</b> In der Hilfe heißt <code>claude auto-mode</code> jetzt „Inspect or reset auto mode
configuration“ statt „… auto mode classifier configuration“. Gemeint ist dasselbe, nur das Wort „classifier“ ist aus dem
Hilfetext verschwunden.</p>
"""

EN = """
<p>Compared with {vorg}: <b>nothing has changed in substance.</b> There are no new and no removed commands, options or
subcommands; the descriptions of the slash commands are unchanged as well.</p>
<p><b>The only difference:</b> in the help, <code>claude auto-mode</code> is now described as "Inspect or reset auto mode
configuration" instead of "… auto mode classifier configuration". It is the same thing; only the word "classifier" has
disappeared from the help text.</p>
"""
