# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <b>keine neuen und keine weggefallenen Befehle; nur kleine Änderungen an Beschreibungen und einem Argument-Wert.</b></p>
<ul>
<li><code>/tui</code>: Die Werte heißen jetzt <code>classic</code> | <code>fullscreen</code> (vorher <code>default</code> | <code>fullscreen</code>); der Argument-Hinweis lautet <code>[classic|fullscreen]</code>.</li>
<li><code>/model</code>: Der Argument-Hinweis ist jetzt <code>&lt;model&gt;</code> statt <code>[model]</code>; die Beschreibung nennt nicht mehr das aktuelle Modell.</li>
<li>Beschreibung nur umformuliert: <code>/status</code> (Komma-Setzung) und <code>/statusline</code> („Set up the status line“).</li>
<li><code>claude --help</code>: <code>--autocompact</code> – das Fenster beträgt „mindestens 100k Token“ statt „100k–1M Token“.</li>
<li>Hilfe der Unterbefehle: Eine Option, die einen JSON-String erwartet, akzeptiert nun auch <code>-</code>, um ihn von stdin zu lesen.</li>
</ul>
<p>Slash-Befehle: weiterhin 135, keine neu, keine weggefallen.</p>
"""

EN = """
<p>Compared with {vorg}: <b>no new and no removed commands; only small changes to descriptions and one argument value.</b></p>
<ul>
<li><code>/tui</code>: the values are now <code>classic</code> | <code>fullscreen</code> (previously <code>default</code> | <code>fullscreen</code>); the argument hint is <code>[classic|fullscreen]</code>.</li>
<li><code>/model</code>: the argument hint is now <code>&lt;model&gt;</code> instead of <code>[model]</code>; the description no longer mentions the current model.</li>
<li>Description merely reworded: <code>/status</code> (comma placement) and <code>/statusline</code> (“Set up the status line”).</li>
<li><code>claude --help</code>: <code>--autocompact</code> – the window is “at least 100k tokens” instead of “100k–1M tokens”.</li>
<li>Subcommand help: an option that takes a JSON string now also accepts <code>-</code> to read it from stdin.</li>
</ul>
<p>Slash commands: still 135, none new, none removed.</p>
"""
