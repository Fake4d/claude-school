# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg} kommt ein neuer Slash-Befehl hinzu: <code>/whiteboard-mp</code>, ein
Mehrspieler-Whiteboard, bei dem alle mit geöffneter Ansicht Striche und Mauszeiger der anderen
live mitverfolgen. Kein Befehl fällt weg, die Liste wächst auf {n_slash} Einträge. Bei
<code>/dataviz</code> und <code>/schedule</code> hat sich nur der interne Auslösetext geändert
(<code>/dataviz</code> nennt jetzt zusätzlich, Diagrammdaten an einen dokumentenfähigen
Erstanbieter-Connector als Zeilen statt als Bild zu übergeben; <code>/schedule</code> ist knapper
gefasst) — für diese Liste ohne Bedeutung. Bei 37 weiteren Slash-Befehlen haben sich lediglich
rein interne Bezeichner geändert, ebenfalls ohne jede Bedeutung für diese Liste.</p>
<p>Bei den Terminal-Optionen (Teil A) wurde die Beschreibung von <code>--bg, --background</code>
präzisiert: sie nennt jetzt namentlich die Befehle, mit denen eine Hintergrundsitzung verwaltet
wird. Genau diese Befehle sind neu in der Hilfe der Unterbefehle (Teil B) hinzugekommen:
<code>claude attach &lt;id&gt;</code> öffnet eine Hintergrundsitzung in diesem Terminal,
<code>claude logs &lt;id&gt;</code> zeigt ihre letzte Ausgabe, <code>claude respawn</code> startet
sie (oder mit <code>--all</code> alle zugleich) mit der aktuellen Fassung neu,
<code>claude rm &lt;id&gt;</code> löscht sie samt Arbeitsbaum, wenn das gefahrlos möglich ist, und
<code>claude stop|kill &lt;id&gt;</code> hält sie an, ohne die Unterhaltung zu löschen — sie lässt
sich mit <code>claude attach</code> wieder öffnen oder mit <code>--resume</code> fortsetzen. Bei
<code>mcp add-json</code> steht jetzt, dass neben stdio und SSE auch HTTP und WebSocket
unterstützt werden. Alles Weitere in Teil A und B ist zeichengleich zu {vorg}.</p>
"""

EN = """
<p>Compared with {vorg} one new slash command is added: <code>/whiteboard-mp</code>, a
multiplayer whiteboard where everyone with the view open sees each other's strokes and cursors
live. None is dropped, and the list grows to {n_slash} entries. For <code>/dataviz</code> and
<code>/schedule</code> only the internal trigger text changed (<code>/dataviz</code> now also
says to hand chart data to a document-capable first-party connector as rows rather than as an
image; <code>/schedule</code> is worded more tersely) — of no consequence for this list. For 37
further slash commands only purely internal identifiers changed, likewise of no consequence for
this list.</p>
<p>Among the terminal options (part A), the description of <code>--bg, --background</code> was
refined: it now names the commands used to manage a background session. Those very commands are
new in the subcommand help (part B): <code>claude attach &lt;id&gt;</code> opens a background
session in this terminal, <code>claude logs &lt;id&gt;</code> shows its recent output,
<code>claude respawn</code> restarts it (or all of them at once with <code>--all</code>) to run
the current version, <code>claude rm &lt;id&gt;</code> deletes it and its worktree when that is
safe, and <code>claude stop|kill &lt;id&gt;</code> stops it without discarding the conversation —
it reopens with <code>claude attach</code> or resumes with <code>--resume</code>. <code>mcp
add-json</code> now states that HTTP and WebSocket are supported alongside stdio and SSE.
Everything else in parts A and B is character-for-character identical to {vorg}.</p>
"""
