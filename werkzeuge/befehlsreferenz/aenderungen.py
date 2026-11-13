# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <b>keine neuen und keine weggefallenen Befehle, nur Feinheiten bei Beschreibungen.</b></p>
<ul>
<li><code>claude agents rm &lt;id&gt;</code> (Hilfe von <code>claude</code> und der Unterbefehle): Der Text ist neu gefasst. Der Befehl entfernt eine Hintergrund-Sitzung nur, wenn das sicher ist, aus der Liste und löscht ihren Worktree. Die Unterhaltung bleibt erhalten; <code>claude --resume</code> listet sie.</li>
<li><code>claude mcp add</code>: Die Hilfe ist gekürzt, die Beispielliste in der Hilfe ist entfallen. Die Option selbst ist unverändert.</li>
<li>Slash-Befehl <code>/stickers</code>: Die Beschreibung lautet jetzt „Verfügbarkeit von Claude-Code-Stickern prüfen“ statt „Claude-Code-Sticker bestellen“.</li>
<li>Slash-Befehl <code>/plugin-authoring</code>: Die Beschreibung ist im Wortlaut geändert (nennt jetzt u. a. Themes und Panels).</li>
</ul>
<p>Slash-Befehle: weiterhin 134, keine neuen, keine weggefallenen.</p>
"""

EN = """
<p>Compared with {vorg}: <b>no new and no removed commands, only small changes to descriptions.</b></p>
<ul>
<li><code>claude agents rm &lt;id&gt;</code> (help of <code>claude</code> and of the subcommands): the text was reworded. If it is safe, the command removes a background session from the list and deletes its worktree. The conversation is kept; <code>claude --resume</code> lists it.</li>
<li><code>claude mcp add</code>: the help is shortened, the list of examples in the help is gone. The command itself is unchanged.</li>
<li>Slash command <code>/stickers</code>: the description now reads “Check Claude Code sticker availability” instead of “Order Claude Code stickers”.</li>
<li>Slash command <code>/plugin-authoring</code>: the description wording changed (it now mentions themes and panels, among other things).</li>
</ul>
<p>Slash commands: still 134, none new, none removed.</p>
"""
