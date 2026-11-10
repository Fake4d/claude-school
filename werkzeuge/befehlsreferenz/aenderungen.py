# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <b>ein neuer Unterbefehl, sonst nichts.</b> Die Hilfe von <code>claude</code> ist zeichengleich.
In der Hilfe der Unterbefehle ist unter <code>claude plugin</code> neu: <code>restore-set-aside &lt;plugin&gt;</code>
(gibt einer Plugin-Kennung die Optionen und Geheimnisse zurück, die beiseitegelegt wurden, als ein von Ihrer Organisation
vorgegebener Marktplatz eine andere Quelle ersetzt hat).</p>
<p>Slash-Befehle: keine neuen, keine weggefallenen, und bei keinem hat sich die Beschreibung inhaltlich geändert.</p>
"""

EN = """
<p>Compared with {vorg}: <b>one new subcommand, nothing else.</b> The help of <code>claude</code> is character-for-character identical.
In the help of the subcommands, <code>claude plugin</code> gains <code>restore-set-aside &lt;plugin&gt;</code>
(gives a plugin id back the options and secrets that were set aside when a marketplace your organization declares replaced
another source).</p>
<p>Slash commands: none new, none removed, and no command’s description changed in substance.</p>
"""
