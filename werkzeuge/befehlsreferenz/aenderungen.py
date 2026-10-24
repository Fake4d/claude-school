# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <b>Weggefallen ist <code>/artifact-pr-review</code></b>, der Befehl, der ein Pull-Request-Review als
teilbare Artifact-Seite angelegt hat. Er fehlt seit 2.1.309 ersatzlos und steht auch nicht mehr im Programm. Der Changelog
erwähnt das nicht.</p>
<p><b>Neu ist die Option <code>--trust-workspace</code> für <code>claude ultrareview</code>.</b> Sie vertraut dem aktuellen
Ordner für diesen einen Lauf, ohne nachzufragen (für Skripte und CI). Nur in Ordnern verwenden, denen man traut. Sonst gibt es
keine neuen Befehle und keine geänderten Beschreibungen, <code>claude --help</code> ist zeichengleich.</p>
<p>Korrektur in eigener Sache: Die Fassungen 2.1.307 und 2.1.308 nannten <code>/shell_expansion</code> als Befehl, der
sich nicht auslesen ließ. Das war falsch. Es ist kein Slash-Befehl, sondern ein interner Prüftyp der Sicherheitsprüfung
für Shell-Befehle, und wird nicht mehr gemeldet.</p>
"""

EN = """
<p>Compared with {vorg}: <b><code>/artifact-pr-review</code> has been removed</b>, the command that created a pull
request review as a shareable artifact page. It has been gone since 2.1.309 without replacement and is no longer in the
program. The changelog does not mention it.</p>
<p><b>New: the <code>--trust-workspace</code> option for <code>claude ultrareview</code>.</b> It trusts the current
folder for this one run without asking (for scripts and CI). Use it only in folders you trust. Otherwise there are no new
commands and no changed descriptions; <code>claude --help</code> is character-for-character identical.</p>
<p>Correction: versions 2.1.307 and 2.1.308 listed <code>/shell_expansion</code> as a command that could not be read
out. That was wrong. It is not a slash command but an internal check type of the shell command safety check, and is no
longer reported.</p>
"""
