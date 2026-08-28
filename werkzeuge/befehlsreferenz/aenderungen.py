# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg} kommt ein neuer Slash-Befehl hinzu: <code>/limit-reset</code>. Kein Befehl
fällt weg, die Liste wächst auf {n_slash} Einträge. Die Kurzbeschreibung von <code>/loop</code>
wurde präzisiert: der selbstgetaktete Modus ohne festes Intervall wird jetzt genannt ("Omit the
interval to let the model self-pace" statt der festen 10-Minuten-Vorgabe). Bei 44 weiteren
Slash-Befehlen haben sich lediglich rein interne Bezeichner geändert, ohne jede Bedeutung für
diese Liste.</p>
<p>Bei den Terminal-Optionen (Teil A) kommt die neue Option <code>--restricted</code> hinzu:
sie entfernt die eingebauten Werkzeuge, die Befehle oder Code ausführen (Bash, PowerShell, REPL
und die anderen codeausführenden Werkzeuge) sowie WebFetch, sofern <code>--tools</code> sie
nicht ausdrücklich benennt, ignoriert Benutzer-, Projekt- und lokale Einstellungsdateien
(verwaltete Einstellungen und <code>--settings</code> gelten weiter), beschränkt die
Dateiwerkzeuge auf die Arbeitsverzeichnisse, verweigert <code>bypassPermissions</code> und lässt
Schreibzugriffe auf Einstellungs-, Git- und Werkzeugkonfigurationsdateien nur durch eine Person
oder den eingerichteten Freigabe-Handler zu. Dieselbe Option erscheint auch in der Hilfe der
Unterbefehle (Teil B) beim Starten ausgelagerter Sitzungen. Alles Weitere in Teil A und B ist
zeichengleich zu {vorg}.</p>
"""

EN = """
<p>Compared with {vorg} one new slash command is added: <code>/limit-reset</code>. None is
dropped, and the list grows to {n_slash} entries. The short description of <code>/loop</code>
was refined: the self-paced mode without a fixed interval is now called out explicitly ("Omit
the interval to let the model self-pace" instead of the fixed 10-minute default). For 44 further
slash commands only purely internal identifiers changed, of no consequence for this list.</p>
<p>Among the terminal options (part A), the new option <code>--restricted</code> is added:
restricted mode removes the built-in tools that run commands or code (Bash, PowerShell, REPL and
the other code-running tools) and WebFetch unless <code>--tools</code> names them, and ignores
user, project and local settings files (managed settings and <code>--settings</code> still
apply). It also confines the file tools to the working directories, refuses
<code>bypassPermissions</code>, and lets only a person or the configured permission handler
approve writes to settings, git and tool-configuration files. The same option also appears in
the subcommand help (part B) for starting dispatched sessions. Everything else in parts A and B
is character-for-character identical to {vorg}.</p>
"""
