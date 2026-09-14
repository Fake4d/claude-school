# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: fast eine Nullrunde. <code>claude --help</code> und die Hilfe der Unterbefehle
sind zeichengleich geblieben. Bei den Slash-Befehlen ist die Zahl mit 139 gleich geblieben — kein
Befehl kam hinzu, keiner ist weggefallen. Eine Beschreibung hat sich inhaltlich geändert:
<code>/plugin-types</code> schreibt jetzt zusätzlich <code>claude-code-plugins.d.ts</code> — die
Typverträge der aktivierten Plugins — neben den bisherigen Dateien. Bei 35 weiteren Befehlen haben
sich nur interne, nicht sichtbare Bezeichner geändert; das betrifft niemanden, der die Referenz
liest. Diese Fassung dokumentiert also im Wesentlichen den Versionssprung von {vorg} auf {v}, mit
einer einzigen sichtbaren Änderung.</p>
"""

EN = """
<p>Compared with {vorg}: almost a no-op release. <code>claude --help</code> and the sub-command
help came out byte-for-byte identical. The slash command count stayed at 139 — no command was
added, none was removed. One description changed in substance:
<code>/plugin-types</code> now also writes <code>claude-code-plugins.d.ts</code> — the enabled
plugins' type contracts — alongside the existing files. 35 further commands had only internal,
non-visible identifiers renamed, which has no effect on anyone reading the reference. This edition
therefore documents essentially the version bump from {vorg} to {v}, with a single visible
change.</p>
"""
