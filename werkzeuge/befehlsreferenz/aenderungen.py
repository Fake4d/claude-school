# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: Ein Slash-Befehl ist weggefallen, die Zahl sinkt von 139 auf 138. <code>/whiteboard</code>
(gemeinsame Zeichenfläche als Artifact) ist nicht mehr als Befehl angemeldet. Anthropic hat ihn still entfernt, der
offizielle Changelog erwähnt es nicht. Neue Befehle gibt es keine. Die interne Beschreibung von
<code>/plugin-authoring</code> wurde umformuliert, ohne dass sich der Zweck ändert.</p>
<p>In <code>claude --help</code> sind mehrere Optionstexte präziser geworden: <code>--resume</code> findet eine
Unterhaltung jetzt auch über ihren Namen. <code>--json-schema</code> wirkt nur zusammen mit <code>--print</code>.
<code>--disable-slash-commands</code> schaltet Skills und Befehle ab. <code>--debug</code> zeigt neue Filterbeispiele
(<code>--debug=hooks,mcp</code>, <code>--debug='!hooks,!mcp'</code>). <code>--system-prompt-snapshot</code> ist
unter <code>--bare</code> außerhalb von Cloud- und Hintergrundsitzungen standardmäßig aus. Bei
<code>claude update</code> steht jetzt, dass Installationen per Paketmanager über diesen aktualisiert werden.</p>
<p>Korrektur in eigener Sache: Der Kurztext zu <code>--system-prompt-snapshot</code> behauptete bisher, ein eigener
<code>--system-prompt</code> schalte die Aufzeichnung ab. Laut Hilfe wird er mit aufgezeichnet. Das ist jetzt
richtiggestellt.</p>
<p>Hinweis zum Auslesen: Der Befehl <code>/shell_expansion</code> existiert, ließ sich aber nicht auslesen und fehlt
deshalb in dieser Referenz. Das ist ein Ausleseproblem, kein Wegfall.</p>
"""

EN = """
<p>Compared with {vorg}: one slash command was removed, so the count drops from 139 to 138. <code>/whiteboard</code>
(a shared sketch canvas as an artifact) is no longer registered as a command. Anthropic removed it silently; the
official changelog does not mention it. There are no new commands. The internal description of
<code>/plugin-authoring</code> was reworded without changing its purpose.</p>
<p>Several option texts in <code>claude --help</code> became more precise: <code>--resume</code> now also finds a
conversation by its name. <code>--json-schema</code> only works together with <code>--print</code>.
<code>--disable-slash-commands</code> turns off skills and commands. <code>--debug</code> shows new filter examples
(<code>--debug=hooks,mcp</code>, <code>--debug='!hooks,!mcp'</code>). <code>--system-prompt-snapshot</code> is off
by default under <code>--bare</code> outside cloud and background sessions. <code>claude update</code> now says that
package-manager installs update through the package manager.</p>
<p>Correction on our part: the short text for <code>--system-prompt-snapshot</code> used to claim that a custom
<code>--system-prompt</code> turns recording off. According to the help, it is recorded as well. This is now
corrected.</p>
<p>Note on extraction: the command <code>/shell_expansion</code> exists but could not be read out, so it is missing from
this reference. This is an extraction problem, not a removal.</p>
"""
