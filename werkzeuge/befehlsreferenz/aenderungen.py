# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <code>/update</code> heißt jetzt <code>/restart</code> („Claude Code neu starten
und diese Sitzung behalten“). <code>update</code> funktioniert weiter als zweiter Name. Der Befehl
war bisher abgeschaltet und ist jetzt verfügbar. <code>/plugin-types</code> ist ersatzlos
weggefallen; der Changelog erwähnt das nicht. Damit sinkt die Zahl der Slash-Befehle von 140 auf
139, davon 4 statt 5 abgeschaltet. <code>/code-review</code> kennt die neue Option
<code>--max-findings &lt;n&gt;|all</code> (wie viele Funde gemeldet werden; die Wahl bleibt, bis
man <code>--max-findings default</code> übergibt). <code>/pause-memory</code> hält jetzt das
Konto-Gedächtnis und das lokale Auto-Gedächtnis an; ein erneuter Aufruf schaltet beide wieder
ein.</p>
<p>Bei <code>claude --help</code> ist die Option <code>--client-data-url</code> weggefallen. Neu ist
der Unterbefehl <code>claude purge</code>. Er löscht allen gespeicherten Zustand eines Projekts und
ersetzt das bisherige <code>claude project purge</code>. Bei <code>claude plugin</code> ist
<code>test [dir]</code> hinzugekommen: Es führt die Tests eines Mods aus.</p>
<p>Korrektur in eigener Sache: Die automatische Rückfrage zu dieser Fassung hielt beide
weggefallenen Befehle fälschlich für einen Auslesefehler. Die Selbstprüfung sucht deshalb jetzt
nach dem alten Beschreibungstext statt nach dem Namen und erkennt Umbenennungen. Außerdem
standen die Tabellen der Optionen und Unterbefehle seit etwa 2.1.250 auf einem festen Stand; neue
Einträge wurden zwar im Änderungskasten angekündigt, fehlten aber in der Tabelle. Sie werden jetzt
bei jeder Fassung direkt aus der Programmhilfe gelesen. Nachgetragen sind dadurch
<code>--desktop</code>, <code>--restricted</code>, die neue Form <code>--agents
&lt;json-oder-datei&gt;</code> (mit <code>--print</code> auch ein Dateipfad), <code>claude plugin
configure</code> und <code>claude update</code>. Die Beschreibung von <code>claude plugin tag</code>
war falsch übersetzt: Der Befehl legt einen Git-Tag für eine Plugin-Veröffentlichung an.</p>
"""

EN = """
<p>Compared with {vorg}: <code>/update</code> is now called <code>/restart</code> ("Restart Claude
Code and keep this session"). <code>update</code> still works as a second name. The command was
previously turned off and is now available. <code>/plugin-types</code> was removed without
replacement; the changelog does not mention it. The slash command count therefore drops from 140
to 139, with 4 instead of 5 turned off. <code>/code-review</code> has the new option
<code>--max-findings &lt;n&gt;|all</code> (how many findings to report; the choice stays until you
pass <code>--max-findings default</code>). <code>/pause-memory</code> now pauses both account
memory and local auto-memory; running it again turns both back on.</p>
<p><code>claude --help</code> lost the option <code>--client-data-url</code>. New is the sub-command
<code>claude purge</code>. It deletes all stored state of a project and replaces the former
<code>claude project purge</code>. <code>claude plugin</code> gained <code>test [dir]</code>, which
runs a mod's tests.</p>
<p>A correction on our side: the automatic query for this version wrongly took both removed
commands for a parsing error. The self-check now searches for the old description text instead of
the name and recognises renames. In addition, the option and sub-command tables had been frozen at
roughly 2.1.250; new entries were announced in this box but missing from the tables. They are now
read straight from the program's help for every version. This adds <code>--desktop</code>,
<code>--restricted</code>, the new form <code>--agents &lt;json-or-file&gt;</code> (with
<code>--print</code> also a file path), <code>claude plugin configure</code> and <code>claude
update</code>. The description of <code>claude plugin tag</code> was wrong: it creates a git tag
for a plugin release.</p>
"""
