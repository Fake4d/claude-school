# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg} kommt kein Slash-Befehl hinzu und keiner fällt weg; es bleibt bei
{n_slash} Befehlen. Inhaltlich geändert hat sich genau eine Kurzbeschreibung:
<code>/whiteboard</code> hieß bisher „eine freihändige Fläche zum Skizzieren von
Architekturdiagrammen in Drahtmodell-Güte" und heißt jetzt „eine <i>gemeinsame</i>
Skizzenfläche für Diagramme in Drahtmodell-Güte" — der Zeichenbereich wird also
ausdrücklich als geteilt beschrieben.</p>
<p>Bei den Terminal-Optionen (Teil A) ist <code>claude --help</code> zeichengleich zu {vorg},
und auch die Hilfe der Unterbefehle (Teil B) ist unverändert. Bei 43 Slash-Befehlen haben sich
rein interne Bezeichner geändert — ohne Bedeutung für diese Liste.</p>
<p><b>In eigener Sache:</b> Fünf Beschreibungen und drei Argument-Hinweise weichen von der
gedruckten Fassung {vorg} ab, ohne dass sich das Programm geändert hätte — betroffen sind
<code>/design</code>, <code>/mcp</code>, <code>/model</code>, <code>/usage</code> und
<code>/version</code>. Grund ist eine Korrektur am Ausleseverfahren: Einige Befehle sind im
Programm mehrfach angelegt, etwa <code>/design</code> als Sammelbefehl <i>und</i> als enge
Variante für <code>consent|revoke</code>. Bisher gewann schlicht der Eintrag, der zufällig
früher in der Datei stand; jetzt wird deterministisch der aussagekräftigste gewählt. Bei
<code>/design</code> steht deshalb erstmals der vollständige Argument-Hinweis
<code>[sync|login|consent|revoke|import|export|status|&lt;prompt&gt;]</code> statt nur
<code>consent | revoke</code>.</p>
<p>Unter der Haube hat Anthropic das Programm neu geschnitten: Die ausgelieferte Datei ist von
392 auf 246 Megabyte geschrumpft und ihre Module tragen andere Namen. Für die Benutzung ändert
das nichts, für diese Referenz schon — das Ausleseverfahren musste daran angepasst werden.</p>
"""

EN = """
<p>Compared with {vorg} no slash command is added and none is dropped; the count stays at
{n_slash}. Exactly one short description changed in substance: <code>/whiteboard</code> used to
read "a freehand canvas for sketching architecture diagrams at wireframe fidelity" and now reads
"a <i>shared</i> sketch canvas for wireframe-fidelity diagrams" — the drawing surface is now
explicitly described as shared.</p>
<p>Among the terminal options (part A), <code>claude --help</code> is character-for-character
identical to {vorg}, and the subcommand help (part B) is unchanged as well. For 43 slash commands
purely internal identifiers changed — of no consequence for this list.</p>
<p><b>A note on this edition:</b> Five descriptions and three argument hints differ from the
printed {vorg} edition without the program having changed — <code>/design</code>,
<code>/mcp</code>, <code>/model</code>, <code>/usage</code> and <code>/version</code>. The reason
is a correction to how this reference is extracted: some commands are defined more than once in
the program, for instance <code>/design</code> both as an umbrella command <i>and</i> as a narrow
<code>consent|revoke</code> variant. Previously whichever entry happened to sit earlier in the
file won; the most informative one is now chosen deterministically. That is why
<code>/design</code> shows its full argument hint
<code>[sync|login|consent|revoke|import|export|status|&lt;prompt&gt;]</code> for the first time,
instead of just <code>consent | revoke</code>.</p>
<p>Under the hood Anthropic re-cut the program: the shipped file shrank from 392 to 246 megabytes
and its modules carry different names. This changes nothing about using Claude Code, but it does
affect this reference — the extraction had to be adapted to it.</p>
"""
