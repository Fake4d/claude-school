# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg} gibt es eine inhaltliche Änderung: Die Hilfe des Unterbefehls
<code>eval</code> beschreibt jetzt genauer, woher die Eval-Fälle kommen. Bisher hieß es, sie
lägen fest unter <code>evals/**/case.yaml</code> bzw. <code>evals/**/prompt.md</code> +
<code>graders/*.md</code>. Neu: Das Verzeichnis lässt sich per <code>--eval-dir</code> oder
über die Manifest-Datei umstellen, <code>evals/</code> ist nur noch der Normalfall.</p>
<p>Bei den Terminal-Optionen (Teil A) ist <code>claude --help</code> zeichengleich zu {vorg}.
Die übrige Hilfe der Unterbefehle (Teil B) ist bis auf die eval-Beschreibung ebenfalls
zeichengleich.</p>
<p>Bei den Slash-Befehlen (Teil C) hat sich die Zahl nicht geändert: {n_slash} Einträge wie
zuvor, keiner ist dazugekommen oder weggefallen, keine Kurzbeschreibung wurde inhaltlich
geändert. Bei 41 Befehlen haben sich rein interne Bezeichner geändert — ohne Bedeutung für
diese Liste.</p>
"""

EN = """
<p>Compared with {vorg} there is one substantive change: the help for the <code>eval</code>
subcommand now describes more precisely where eval cases come from. Previously it said they
live fixed under <code>evals/**/case.yaml</code> or <code>evals/**/prompt.md</code> +
<code>graders/*.md</code>. New: the directory can be overridden via <code>--eval-dir</code> or
the manifest file, with <code>evals/</code> now just the default.</p>
<p>Among the terminal options (part A), <code>claude --help</code> is character-for-character
identical to {vorg}. The rest of the subcommand help (part B) is likewise identical apart from
the eval description.</p>
<p>Among the slash commands (part C) the count is unchanged: {n_slash} entries as before,
none added, none dropped, no short description changed in substance. For 41 commands purely
internal identifiers changed — of no consequence for this list.</p>
"""
