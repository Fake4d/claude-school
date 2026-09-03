# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg} gibt es eine inhaltliche Ergänzung bei <code>claude --help</code>: die neue
Option <code>--permission-prompts &lt;target&gt;</code> legt fest, wer bei <code>--print</code> auf
Berechtigungsabfragen antwortet — <code>host</code> (der SDK-Host bzw. <code>--permission-prompt-tool</code>)
oder <code>none</code> (automatische Ablehnung; der Berechtigungsmodus entscheidet weiterhin über
alles andere), Standard ist <code>host</code>. In der Hilfe der Unterbefehle hat sich eine Zahl
geändert: Bei <code>claude ultrareview --timeout</code> stieg der Standardwert von 30 auf 45 Minuten,
sonst blieb dieser Teil unverändert. Bei den Slash-Befehlen bleibt die Liste unverändert bei
{n_slash} Einträgen — kein Befehl kam hinzu, keiner fiel weg. Inhaltlich geändert hat sich die
Beschreibung von <code>/plugin-types</code>: der Befehl schreibt jetzt zusätzlich zur bisherigen
Typdatei für die MCP-Werkzeuge auch die TypeScript-Deklarationen der Plugin-Schnittstelle selbst.
Bei 34 weiteren Befehlen änderten sich lediglich rein interne Bezeichner, ohne Bedeutung für diese
Liste.</p>
"""

EN = """
<p>Compared with {vorg} there is one substantive addition to <code>claude --help</code>: the new
option <code>--permission-prompts &lt;target&gt;</code> sets who answers permission prompts with
<code>--print</code> — <code>host</code> (the SDK host or <code>--permission-prompt-tool</code>) or
<code>none</code> (auto-deny; the permission mode still decides everything else), default is
<code>host</code>. In the subcommand help, one number changed: for
<code>claude ultrareview --timeout</code> the default rose from 30 to 45 minutes; the rest of that
section is unchanged. The slash command list stays unchanged at {n_slash} entries — none added,
none dropped. One description changed in substance: <code>/plugin-types</code> now also writes the
plugin API's own TypeScript declarations, in addition to the existing type file for the MCP tools.
For 34 further commands only purely internal identifiers changed, of no consequence for this
list.</p>
"""
