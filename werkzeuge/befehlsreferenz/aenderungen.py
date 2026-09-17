# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <code>claude --help</code> und die Hilfe der Unterbefehle sind zeichengleich
geblieben. Bei den Slash-Befehlen ist die Zahl mit 139 gleich geblieben — kein Befehl kam hinzu,
keiner ist weggefallen. Bei vier Befehlen hat sich die Beschreibung inhaltlich geändert: Bei
<code>/code-review</code> heißt es jetzt genauer, dass die Suche nach Wiederverwendungs-,
Vereinfachungs- und Effizienz-Verbesserungen nur dort greift, wo das Prüfrezept des Modells sie
abdeckt. <code>/heapdump</code> beschreibt jetzt auch das Verhalten unter Linux, wenn kein
Desktop-Ordner existiert: Dann landet der Speicherauszug im Home-Verzeichnis. Bei
<code>/ultraplan</code> und <code>/ultrareview</code> heißt es statt „Claude Code on the web" jetzt
„cloud session" — eine Umbenennung ohne inhaltliche Änderung der Funktion. Aus demselben Grund
heißt <code>/web-setup</code> jetzt „Set up cloud sessions with your GitHub account" statt „Set up
Claude Code on the web with your GitHub account". Bei 34 weiteren Befehlen haben sich nur interne,
nicht sichtbare Bezeichner geändert; das betrifft niemanden, der die Referenz liest. Diese Fassung
dokumentiert also den Versionssprung von {vorg} auf {v} mit vier Beschreibungs-Anpassungen, die
größtenteils die Umbenennung von „Claude Code on the web" zu „cloud session" nachvollziehen.</p>
"""

EN = """
<p>Compared with {vorg}: <code>claude --help</code> and the sub-command help came out
byte-for-byte identical. The slash command count stayed at 139 — no command was added, none was
removed. Four commands changed their description in substance: <code>/code-review</code> now
states more precisely that the search for reuse/simplification/efficiency cleanups only applies
where the model's review recipe covers them. <code>/heapdump</code> now also describes the
behaviour on Linux when there is no Desktop folder: the heap dump then goes to the home directory
instead. <code>/ultraplan</code> and <code>/ultrareview</code> now say "cloud session" instead of
"Claude Code on the web" — a renaming with no change in function. For the same reason,
<code>/web-setup</code> now reads "Set up cloud sessions with your GitHub account" instead of "Set
up Claude Code on the web with your GitHub account". 34 further commands had only internal,
non-visible identifiers renamed, which has no effect on anyone reading the reference. This edition
therefore documents the version bump from {vorg} to {v} together with four description updates,
most of which reflect the "Claude Code on the web" → "cloud session" renaming.</p>
"""
