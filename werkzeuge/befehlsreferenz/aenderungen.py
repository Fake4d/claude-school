# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: Bei den Slash-Befehlen ist kein Befehl hinzugekommen oder weggefallen; die
Anzahl blieb bei 140. Einzige inhaltliche Änderung: <code>/loop</code> hat jetzt den Argument-Hinweis
<code>[interval] [prompt]</code> (vorher keinen). Bei 36 weiteren Befehlen wurden nur interne,
minifizierte Bezeichner ausgetauscht; das betrifft niemanden, der die Referenz liest. Bei
<code>claude --help</code> ist die Option <code>--desktop</code> hinzugekommen: Sie öffnet die
Sitzung in der Claude-Desktop-App statt im Terminal (zusammen mit <code>--continue</code> oder
<code>--resume &lt;id&gt;</code>, um die Sitzung auszuwählen). In der Hilfe der Unterbefehle ist
<code>configure [options] &lt;plugin&gt;</code> hinzugekommen: Es zeigt die Optionen eines Plugins und
welche davon noch nicht gesetzt sind, oder speichert Werte von stdin mit
<code>--values-stdin</code>.</p>
"""

EN = """
<p>Compared with {vorg}: no slash command was added or removed; the count stays at 140. The only
change in content: <code>/loop</code> now has the argument hint <code>[interval] [prompt]</code>
(previously none). 36 further commands had only internal, minified identifiers renamed, which has no
effect on anyone reading the reference. <code>claude --help</code> gained the option
<code>--desktop</code>: it opens the session in the Claude Desktop app instead of the terminal (with
<code>--continue</code> or <code>--resume &lt;id&gt;</code> to pick the session). The sub-command help
gained <code>configure [options] &lt;plugin&gt;</code>: it shows a plugin's options and which are
unset, or saves values from stdin with <code>--values-stdin</code>.</p>
"""
