# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg} gibt es zwei inhaltliche Ergänzungen bei <code>claude --help</code>: Die
Beschreibung von <code>--bg</code>/<code>--background</code> erklärt jetzt zusätzlich das
Zusammenspiel mit <code>--resume</code> — eine bereits laufende Hintergrundsitzung wird unter
derselben Kennung fortgesetzt, oder es startet eine Kopie mit entsprechendem Hinweis, falls die
Sitzung noch läuft. Neu hinzugekommen ist die Option <code>--system-prompt-snapshot &lt;on|off&gt;</code>,
die die Systemanweisung einmal je Unterhaltung festhält und danach unverändert wiederverwendet. Die
Hilfe der Unterbefehle blieb zeichengleich. Bei den Slash-Befehlen bleibt die Liste unverändert bei
{n_slash} Einträgen — kein Befehl kam hinzu, keiner fiel weg, und inhaltlich hat sich an keinem
etwas geändert; bei 34 Befehlen änderten sich lediglich rein interne Bezeichner, ohne Bedeutung für
diese Liste.</p>
"""

EN = """
<p>Compared with {vorg} there are two substantive additions to <code>claude --help</code>: the
description of <code>--bg</code>/<code>--background</code> now also covers how it interacts with
<code>--resume</code> — an already-running background session continues under the same ID, or a
copy starts with a note to that effect if the session is already running. New is the option
<code>--system-prompt-snapshot &lt;on|off&gt;</code>, which records the system prompt once per
conversation and reuses it verbatim from then on. The subcommand help remains
character-for-character identical. The slash command list stays unchanged at {n_slash} entries —
none added, none dropped, and nothing changed in substance for any of them; for 34 commands only
purely internal identifiers changed, of no consequence for this list.</p>
"""
