# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: Bei den Slash-Befehlen hat sich nichts geändert – keiner ist hinzugekommen
oder weggefallen, und bei keinem hat sich die Beschreibung inhaltlich geändert. Bei 36 Befehlen
wurden nur interne, minifizierte Bezeichner ausgetauscht; das betrifft niemanden, der die Referenz
liest. Bei <code>claude --help</code> gibt es zwei Präzisierungen: Bei <code>--bare</code> steht
jetzt dabei, dass mit „Hooks" die in Einstellungen und von installierten Plugins definierten Hooks
gemeint sind – in Claude Code eingebaute Funktionen sind davon nicht betroffen. Bei
<code>--safe-mode</code> heißt es nun ausdrücklich „installierte Plugins" statt nur „Plugins", und
in der Zusicherung, was trotzdem normal funktioniert, ist jetzt auch von Plugins die Rede
(„eingebaute Tools und Plugins" statt nur „eingebaute Tools"). Die Hilfe der Unterbefehle ist
zeichengleich geblieben.</p>
"""

EN = """
<p>Compared with {vorg}: nothing changed among the slash commands – none was added, none was
removed, and no command's description changed in substance. 36 commands had only internal,
minified identifiers renamed, which has no effect on anyone reading the reference.
<code>claude --help</code> gained two clarifications: <code>--bare</code> now spells out that
"hooks" means those defined in settings and by installed plugins – features built into Claude Code
itself are unaffected. <code>--safe-mode</code> now says "installed plugins" explicitly instead of
just "plugins", and the note about what still works normally now also mentions plugins ("built-in
tools and plugins" instead of just "built-in tools"). The sub-command help came out byte-for-byte
identical.</p>
"""
