# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: Bei den Slash-Befehlen ist kein Befehl hinzugekommen oder weggefallen. Bei
<code>/focus</code> zeigt der Vergleich einen Argument-Hinweis <code>[on|off]</code>, den es vorher
nicht gab. Bei <code>/desktop</code> weichen die ausgelesenen Angaben ab (Beschreibung nur noch
„- …", Alias <code>app</code> fehlt, Argument-Hinweis „whole"); das sieht nach einem Ausleseproblem
aus und ist nicht als Änderung übernommen – die Beschreibung bleibt wie bisher. Bei 36 weiteren
Befehlen wurden nur interne, minifizierte Bezeichner ausgetauscht; das betrifft niemanden, der die
Referenz liest. Bei <code>claude --help</code> gibt es eine Präzisierung: <code>--agents</code>
nimmt jetzt neben einem JSON-Objekt auch – zusammen mit <code>--print</code> – den Pfad zu einer
Datei entgegen, die dieses JSON enthält. Die Hilfe der Unterbefehle ist zeichengleich geblieben.</p>
"""

EN = """
<p>Compared with {vorg}: no slash command was added or removed. For <code>/focus</code> the
comparison shows an argument hint <code>[on|off]</code> that did not exist before. For
<code>/desktop</code> the extracted values differ (description reduced to "- …", the
<code>app</code> alias missing, argument hint "whole"); this looks like an extraction problem and
has not been taken over as a change – the description stays as before. 36 further commands had only
internal, minified identifiers renamed, which has no effect on anyone reading the reference.
<code>claude --help</code> gained one clarification: <code>--agents</code> now accepts, besides a
JSON object, also – together with <code>--print</code> – the path to a file that holds such JSON.
The sub-command help came out byte-for-byte identical.</p>
"""
