# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg} gibt es einen neuen Slash-Befehl: <code>/low-priority</code> — setzt eine
laufende Sitzung nach Erreichen des Sitzungslimits mit niedrigerer Priorität fort; erneuter
Aufruf stoppt das wieder.</p>
<p>Zwei Kurzbeschreibungen wurden präzisiert, ohne dass sich die Funktion ändert:
<code>/auto-mode-setup</code> ("richtet den Auto-Modus ein und passt ihn an — Umgebungskontext,
plus optionale Regelanpassungen" wurde zu "bringt dem Auto-Modus die eigene Umgebung bei, plus
optionale Regelanpassungen") und <code>/list-agents</code> (listet jetzt ausdrücklich auch
"Teammitglieder" neben Subagenten und anderen Claude-Sitzungen).</p>
<p>Bei den Terminal-Optionen (Teil A) ist <code>claude --help</code> zeichengleich zu {vorg}.
Die Hilfe der Unterbefehle (Teil B) hat eine kleine Ergänzung beim Unterbefehl <code>mcp</code>:
der Hinweis zum Health-Check freigegebener Server nennt jetzt zusätzlich, dass sich das je
Projekt abschalten lässt.</p>
<p>Bei den Slash-Befehlen (Teil C) steigt die Zahl von 129 auf {n_slash}. Bei 42 Befehlen haben
sich rein interne Bezeichner geändert — ohne Bedeutung für diese Liste.</p>
"""

EN = """
<p>Compared with {vorg} there is one new slash command: <code>/low-priority</code> — continues
a running session at lower priority after it hits the session limit; running it again stops
that again.</p>
<p>Two short descriptions were sharpened without any change in function:
<code>/auto-mode-setup</code> ("Set up and customise auto mode — environment context, plus
optional rule tweaks" became "Teach auto mode about your environment, plus optional rule
tweaks") and <code>/list-agents</code> (now explicitly mentions "teammates" alongside subagents
and other Claude sessions).</p>
<p>Among the terminal options (part A), <code>claude --help</code> is character-for-character
identical to {vorg}. The subcommand help (part B) gained one small addition under the
<code>mcp</code> subcommand: the note about health-checking approved servers now also mentions
that this can be disabled per project.</p>
<p>Among the slash commands (part C) the count rises from 129 to {n_slash}. For 42 commands
purely internal identifiers changed — of no consequence for this list.</p>
"""
