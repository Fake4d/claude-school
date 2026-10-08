# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: Es gibt keine neuen oder weggefallenen Befehle; die Zahl der Slash-Befehle bleibt bei 139.
Auch <code>claude --help</code> und die Hilfe der Unterbefehle sind zeichengleich geblieben.</p>
<p>Geändert hat sich nur die Beschreibung von <code>/plugin-authoring</code>: Sie spricht jetzt allgemeiner von einer
Änderung an Claudes eigener Oberfläche oder seinem Verhalten (etwa Fenster oder Leiste, Statuszeile, Hinweis,
Slash-Befehl oder ein Hook auf Werkzeug- und Prompt-Aufrufe) und nennt als Einsatz das Erstellen, Ändern und
Fehlersuchen eines Mods oder seines Hook-Moduls. Zuvor ging es enger um Live-Fenster, Leiste, Statuszeile, Toast und
Hooks im Terminal oder in der Desktop-Code-Ansicht. Sonst gab es nur interne, minifizierte Bezeichner bei 40 Befehlen,
die für den Leser ohne Bedeutung sind.</p>
"""

EN = """
<p>Compared with {vorg}: no commands were added or removed; the number of slash commands stays at 139.
<code>claude --help</code> and the help of the subcommands are also character-for-character identical.</p>
<p>Only the description of <code>/plugin-authoring</code> changed: it now speaks more broadly of a change to Claude's
own interface or behaviour (such as a pane or panel, a band above the prompt, a status line, a toast, a slash command
or a hook on tool calls or prompts) and names making, changing and debugging a mod or its hooks module as the use.
Before, it was narrower, about a live pane, band, status line, toast and hooks in the terminal or the desktop Code
tab. Otherwise there were only internal, minified identifiers for 40 commands, which mean nothing to the reader.</p>
"""
