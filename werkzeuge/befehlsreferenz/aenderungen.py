# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: Bei den Slash-Befehlen ist kein Befehl hinzugekommen oder weggefallen. Bei
<code>/doctor</code> gibt es jetzt einen Argument-Hinweis <code>[prompt-audit [&lt;path&gt;]]</code>, den
es vorher nicht gab. Bei <code>/plugin-authoring</code> wurde die Beschreibung umgeschrieben: Der
Befehl wird jetzt als Weg beschrieben, einen „Mod" zu bauen – ein Live-Fenster, ein Band, eine
Statuszeile, einen Toast oder einen Hook in Claude Code (Terminal oder Desktop-Code-Tab), geschrieben
als Plugin aus Funktions-Hooks, das sich in dieser Sitzung im laufenden Betrieb neu lädt; vor dem
Schreiben oder Debuggen eines Hooks-Moduls zu laden. Bei 32 weiteren Befehlen wurden nur interne,
minifizierte Bezeichner ausgetauscht; das betrifft niemanden, der die Referenz liest. Bei
<code>claude --help</code> ist die Option <code>--client-data-url &lt;url&gt;</code> hinzugekommen: die URL
eines signierten Konfigurationsdokuments. Claude Code beendet sich, wenn es sich nicht laden lässt
oder das gewählte Modell nicht abdeckt; setzt man stattdessen <code>CLAUDE_CODE_CLIENT_DATA_URL</code>,
bleibt die URL aus der Prozessliste heraus. Die Hilfe der Unterbefehle ist zeichengleich geblieben.</p>
"""

EN = """
<p>Compared with {vorg}: no slash command was added or removed. <code>/doctor</code> now has an
argument hint <code>[prompt-audit [&lt;path&gt;]]</code> that did not exist before. The description of
<code>/plugin-authoring</code> was rewritten: the command is now presented as the way to make a "mod" –
a live pane, band, status line, toast or hook inside Claude Code (terminal or desktop Code tab),
written as a plugin of function hooks that hot-reloads in the current session; to be loaded before
writing or debugging a hooks module. 32 further commands had only internal, minified identifiers
renamed, which has no effect on anyone reading the reference. <code>claude --help</code> gained the
option <code>--client-data-url &lt;url&gt;</code>: the URL of a signed configuration document. Claude Code
exits if it cannot load it or it does not cover the selected model; setting
<code>CLAUDE_CODE_CLIENT_DATA_URL</code> instead keeps the URL out of the process list. The sub-command
help came out byte-for-byte identical.</p>
"""
