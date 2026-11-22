# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <b>ein neuer Befehl, <code>/access</code>, und eine geänderte Beschreibung; sonst nichts.</b></p>
<ul>
<li><code>/access</code> ist neu: zeigt die Verifizierungsprogramme, an denen das Konto teilnimmt.</li>
<li><code>/design-sync</code>: Die Beschreibung lautet jetzt „Sync a React design system to Claude Design“ (vorher „Push … to claude.ai/design“). Der Befehl bündelt weiterhin den echten Komponentencode (aus Storybook oder einem Paket) und lädt ihn hoch.</li>
</ul>
<p><code>claude --help</code> und die Hilfe der Unterbefehle sind zeichengleich. Slash-Befehle: 135 statt 134 (einer neu, keiner weg).</p>
"""

EN = """
<p>Compared with {vorg}: <b>one new command, <code>/access</code>, and one changed description; nothing else.</b></p>
<ul>
<li><code>/access</code> is new: it shows the verification programs your account is in.</li>
<li><code>/design-sync</code>: the description now reads “Sync a React design system to Claude Design” (previously “Push … to claude.ai/design”). The command still bundles the real component code (from Storybook or a package) and uploads it.</li>
</ul>
<p><code>claude --help</code> and the subcommand help are character-for-character identical. Slash commands: 135 instead of 134 (one new, none removed).</p>
"""
