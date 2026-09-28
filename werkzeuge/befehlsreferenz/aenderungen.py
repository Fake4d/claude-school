# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: Bei den Slash-Befehlen ist kein Befehl hinzugekommen oder weggefallen. Bei
<code>/desktop</code> lautet die Beschreibung jetzt „Continue the current session in Claude Desktop"
(vorher nur „- …"), der Alias <code>app</code> ist hinzugekommen und der bisherige Argument-Hinweis
ist entfallen. Bei <code>/mcp</code> hat sich der Argument-Hinweis geändert: statt
<code>reconnect &lt;server&gt;</code> steht dort jetzt <code>reconnect (&lt;server&gt;|all)</code>. Bei
<code>/rate-limit-options</code> wurde die Beschreibung von „Show options when rate limit is reached"
zu „Manage usage limits and upgrade options" geändert. Bei 34 weiteren Befehlen wurden nur interne,
minifizierte Bezeichner ausgetauscht; das betrifft niemanden, der die Referenz liest. Bei
<code>claude --help</code> ist in der Beschreibung der Modelloption der Beispielverweis auf
<code>'claude-fable-5'</code> entfallen; sonst blieb die Hilfe gleich. Die Hilfe der Unterbefehle ist
zeichengleich geblieben.</p>
"""

EN = """
<p>Compared with {vorg}: no slash command was added or removed. The description of
<code>/desktop</code> is now "Continue the current session in Claude Desktop" (previously just
"- …"), it gained the alias <code>app</code>, and its former argument hint is gone. The argument hint
of <code>/mcp</code> changed: <code>reconnect &lt;server&gt;</code> is now
<code>reconnect (&lt;server&gt;|all)</code>. The description of <code>/rate-limit-options</code> changed
from "Show options when rate limit is reached" to "Manage usage limits and upgrade options". 34 further
commands had only internal, minified identifiers renamed, which has no effect on anyone reading the
reference. In <code>claude --help</code>, the model option's description no longer gives the example
<code>'claude-fable-5'</code>; otherwise the help is unchanged. The sub-command help came out
byte-for-byte identical.</p>
"""
