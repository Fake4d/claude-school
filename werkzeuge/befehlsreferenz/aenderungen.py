# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <b>ein neuer Slash-Befehl, keiner weggefallen; sonst vor allem umformulierte Beschreibungen.</b></p>
<ul>
<li>Neu: <code>/send-to-project</code> – schickt eine Nachricht aus dieser Sitzung an ein Claude Project („Send a message from this session to a Claude Project“).</li>
<li><code>/help</code> hat jetzt einen Argument-Hinweis: <code>[command]</code>.</li>
<li>Beschreibung im Wortlaut geändert (Bedeutung im Kern gleich, meist kürzer gefasst): <code>/add-dir</code>, <code>/btw</code>, <code>/bug</code>, <code>/context</code> („Show what fills the context“), <code>/copy</code>, <code>/effort</code>, <code>/export</code>, <code>/fork</code>, <code>/plan</code>, <code>/powerup</code>, <code>/resume</code>, <code>/rewind</code>, <code>/setup-bedrock</code>, <code>/setup-vertex</code>, <code>/status</code>, <code>/terminal-setup</code>.</li>
<li><code>claude --help</code> und die Hilfe der Unterbefehle: Es sind keine Optionen oder Unterbefehle dazugekommen oder weggefallen, nur Beschreibungstexte sind umformuliert. Einzige inhaltliche Ergänzung: Bei <code>--bare</code> und <code>--safe-mode</code> wird nun erwähnt, dass die Hooks von Managed-Plugins der Organisation weiterhin gelten.</li>
</ul>
<p>Slash-Befehle: 135 statt 134, keine weggefallen.</p>
"""

EN = """
<p>Compared with {vorg}: <b>one new slash command, none removed; otherwise mostly reworded descriptions.</b></p>
<ul>
<li>New: <code>/send-to-project</code> – sends a message from this session to a Claude Project (“Send a message from this session to a Claude Project”).</li>
<li><code>/help</code> now has an argument hint: <code>[command]</code>.</li>
<li>Description wording changed (same meaning at heart, mostly shorter): <code>/add-dir</code>, <code>/btw</code>, <code>/bug</code>, <code>/context</code> (“Show what fills the context”), <code>/copy</code>, <code>/effort</code>, <code>/export</code>, <code>/fork</code>, <code>/plan</code>, <code>/powerup</code>, <code>/resume</code>, <code>/rewind</code>, <code>/setup-bedrock</code>, <code>/setup-vertex</code>, <code>/status</code>, <code>/terminal-setup</code>.</li>
<li><code>claude --help</code> and the subcommand help: no options or subcommands were added or removed, only description texts were reworded. The one substantive addition: for <code>--bare</code> and <code>--safe-mode</code> it now says the hooks of your organization's managed plugins still apply.</li>
</ul>
<p>Slash commands: 135 instead of 134, none removed.</p>
"""
