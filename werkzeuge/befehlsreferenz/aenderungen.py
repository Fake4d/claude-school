# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg} gibt es zwei neue Slash-Befehle: <code>/cloud-plugins</code> — legt fest, ob
Sitzungen in der Cloud die auf diesem Rechner eingeschalteten Erweiterungen mitbenutzen — und
<code>/plugin-types</code>, das eine Typdatei <code>claude-code-mcp.d.ts</code> mit den Eingaben
der verbundenen MCP-Werkzeuge schreibt, um eine Erweiterung gegen diese Sitzung zu typisieren.
Weggefallen ist kein Befehl.</p>
<p>Eine Kurzbeschreibung hat sich inhaltlich geändert: <code>/schedule</code> hieß bisher
„erstellt und verwaltet geplante entfernte Claude-Code-Agenten" und heißt jetzt „erstellt,
ändert, listet oder startet geplante Cloud-Agenten (Routinen), die nach Zeitplan laufen" — der
Befehl kann also ausdrücklich auch auflisten und sofort starten, nicht nur anlegen und
verwalten.</p>
<p>Bei sechs weiteren Befehlen — <code>/artifact-components</code>,
<code>/artifact-diagramming</code>, <code>/prototype</code>, <code>/run-skill-generator</code>,
<code>/whiteboard</code> und <code>/workshop</code> — wurde im Beschreibungstext lediglich der
Gedankenstrich durch einen einfachen Bindestrich ersetzt. Am Sinn ändert das nichts.</p>
<p>Bei den Terminal-Optionen (Teil A) ist <code>claude --help</code> zeichengleich zu {vorg},
und auch die Hilfe der Unterbefehle (Teil B) ist unverändert.</p>
<p>Bei den Slash-Befehlen (Teil C) steigt die Zahl von 130 auf {n_slash}. Bei 44 Befehlen haben
sich rein interne Bezeichner geändert — ohne Bedeutung für diese Liste.</p>
"""

EN = """
<p>Compared with {vorg} there are two new slash commands: <code>/cloud-plugins</code> — decides
whether cloud sessions use the plugins enabled on this machine — and <code>/plugin-types</code>,
which writes a <code>claude-code-mcp.d.ts</code> type file describing the inputs of the connected
MCP tools, so a plugin can be typed against this session. No command was dropped.</p>
<p>One short description changed in substance: <code>/schedule</code> used to read "create and
manage scheduled remote Claude Code agents" and now reads "create, update, list, or run scheduled
cloud agents (routines) that execute on a cron schedule" — so the command explicitly also lists
and runs them on the spot, not just creates and manages them.</p>
<p>For six further commands — <code>/artifact-components</code>,
<code>/artifact-diagramming</code>, <code>/prototype</code>, <code>/run-skill-generator</code>,
<code>/whiteboard</code> and <code>/workshop</code> — the only change in the description text is
an em dash replaced by a plain hyphen. Nothing about the meaning changed.</p>
<p>Among the terminal options (part A), <code>claude --help</code> is character-for-character
identical to {vorg}, and the subcommand help (part B) is unchanged as well.</p>
<p>Among the slash commands (part C) the count rises from 130 to {n_slash}. For 44 commands
purely internal identifiers changed — of no consequence for this list.</p>
"""
