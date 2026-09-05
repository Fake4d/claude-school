# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg} ist <code>claude --help</code> zeichengleich geblieben, ebenso die Hilfe der
Unterbefehle. Geändert hat sich allein die Liste der Slash-Befehle, von 134 auf {n_slash} Einträge.
Neu ist <code>/plugin-authoring</code>: Hilfe beim Schreiben und Prüfen eines Plugins, das aus
Funktions-Hooks besteht. <code>/setup-cowork</code> heißt jetzt <code>/setup-claude</code> und führt
nicht mehr nur durch die Cowork-Einrichtung, sondern durch die Einrichtung allgemein — der alte Name
funktioniert als Alias weiter. Weggefallen ist <code>/whiteboard-mp</code>: Die
Mehrspieler-Zeichenfläche ist in <code>/whiteboard</code> aufgegangen, das nun je nach Umgebung die
Einzel- oder die Live-Fassung öffnet. Dazu eine Korrektur in eigener Sache:
<code>/artifact-pr-review</code> steht ab dieser Fassung in der Liste. Den Befehl gibt es seit
Langem — er fehlte hier, weil unser Ausleseverfahren seine Beschreibung nicht lesen konnte und ihn
wortlos übersprang. Das ist ein Fehler auf unserer Seite gewesen, kein Zuwachs bei Claude Code. Bei
38 weiteren Befehlen änderten sich lediglich rein interne Bezeichner, ohne Bedeutung für diese
Liste.</p>
"""

EN = """
<p>Compared with {vorg}, <code>claude --help</code> is unchanged down to the character, and so is
the subcommand help. The only change is in the slash command list, which grew from 134 to
{n_slash} entries. <code>/plugin-authoring</code> is new: help with writing and debugging a plugin
made of function hooks. <code>/setup-cowork</code> is now called <code>/setup-claude</code> and no
longer walks you through Cowork setup alone but through setup in general — the old name still works
as an alias. <code>/whiteboard-mp</code> is gone: the multiplayer drawing surface has been folded
into <code>/whiteboard</code>, which now opens either the solo or the live version depending on the
environment. One correction on our own account: <code>/artifact-pr-review</code> appears in the list
from this version on. The command has existed for a long time — it was missing here because our
extraction could not read its description and skipped it without a word. That was a fault on our
side, not an addition to Claude Code. For 38 further commands only purely internal identifiers
changed, of no consequence for this list.</p>
"""
