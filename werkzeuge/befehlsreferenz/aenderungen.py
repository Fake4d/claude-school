# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <b>keine neuen und keine weggefallenen Befehle, nur eine Beschreibung im Wortlaut geändert.</b></p>
<ul>
<li>Slash-Befehl <code>/plugin-authoring</code>: Die Beschreibung ist im Wortlaut geändert. Sie beginnt jetzt mit „Make a mod“ und nennt als Beispiele Themes, Panels, Bänder, Statuszeilen, Toasts, Slash-Befehle und Hooks auf Tool-Aufrufe.</li>
</ul>
<p><code>claude --help</code> und die Hilfe der Unterbefehle sind unverändert. Slash-Befehle: weiterhin 134, keine neuen, keine weggefallenen.</p>
"""

EN = """
<p>Compared with {vorg}: <b>no new and no removed commands, only one description reworded.</b></p>
<ul>
<li>Slash command <code>/plugin-authoring</code>: the description wording changed. It now starts with “Make a mod” and gives themes, panels, bands, status lines, toasts, slash commands and hooks on tool calls as examples.</li>
</ul>
<p><code>claude --help</code> and the help of the subcommands are unchanged. Slash commands: still 134, none new, none removed.</p>
"""
