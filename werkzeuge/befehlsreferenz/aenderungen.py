# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Bei den Terminal-Optionen (Teil A) hat sich nichts geändert: <code>claude --help</code>
ist zeichengleich zu {vorg}.</p>
<p>Bei den Unterbefehlen (Teil B) gibt es eine inhaltliche Änderung: <code>claude plugin
validate</code> prüft jetzt auch einen bloßen <code>.claude/skills</code>-Ordner und meldet
<code>SKILL.md</code>-Dateien, deren Vorspann (Frontmatter) sich nicht einlesen lässt. Die
Kurzbeschreibung in dieser Liste („Plugin auf Fehler prüfen.") bleibt zutreffend, wurde aber
nicht um dieses Detail erweitert.</p>
<p>Bei den Slash-Befehlen (Teil C) hat sich die Zahl nicht geändert: {n_slash} Einträge wie
zuvor, keiner ist dazugekommen oder weggefallen.</p>
<p class="unter" style="margin-top:2mm">Beim automatischen Abgleich sah es kurzzeitig so aus,
als sei <code>/claude-api</code> entfallen. Grund war diesmal keine falsche Namensauflösung wie
beim <code>/loop</code>-Fall, sondern eine leere Kurzbeschreibung: sie liegt in dieser Fassung
als Array mehrerer Textbausteine vor statt als einzelner Text, und das Ausleseverfahren kannte
dieses Muster noch nicht. Der Befehl selbst war nie betroffen. Das Verfahren wurde entsprechend
erweitert.</p>
"""

EN = """
<p>Nothing changed among the terminal options (part A): <code>claude --help</code> is
character-for-character identical to {vorg}.</p>
<p>Among the subcommands (part B) there is one real change: <code>claude plugin validate</code>
now also checks a bare <code>.claude/skills</code> folder and reports <code>SKILL.md</code>
files whose frontmatter cannot be parsed. The short description in this list ("Check a plugin
for errors.") remains accurate and was not extended with that detail.</p>
<p>Among the slash commands (part C) the count is unchanged: {n_slash} entries as before,
none added, none dropped.</p>
<p class="unter" style="margin-top:2mm">During the automatic comparison it briefly looked as
if <code>/claude-api</code> had disappeared. This time the cause was not a failed name lookup
as in the <code>/loop</code> case, but an empty short description: in this version it is an
array of several text fragments rather than a single string, and the extraction did not yet
know that shape. The command itself was never affected. The extraction has been extended
accordingly.</p>
"""
