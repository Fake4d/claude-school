# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: Der Befehl <code>/plan-artifact</code> ist weggefallen — sein Name steht in
keiner der beiden Fassungen mehr im Programm, und der offizielle Changelog erwähnt ihn nicht,
also kein Auslesefehler, sondern ein echter Wegfall. Bei den Optionen hat <code>--plugin-dir</code>
dazugelernt: es lädt jetzt auch einen ganzen Ordner voller Plugins statt nur eines einzelnen.
<code>--fallback-model</code> greift nicht mehr nur im Kopfzeilenmodus (<code>--print</code>),
sondern auch in interaktiven Sitzungen. Bei den Slash-Befehlen selbst kam bei <code>/import</code>
mit "cursor" eine dritte unterstützte Quelle hinzu, und bei <code>/plan</code> ist die Unteroption
"share" aus dem Hinweistext verschwunden.</p>
"""

EN = """
<p>Compared with {vorg}: the <code>/plan-artifact</code> command is gone — its name no longer
appears in either build, and the official changelog doesn't mention it either, so this is a real
removal, not a misread. Among the options, <code>--plugin-dir</code> now also accepts a whole
folder of plugins instead of just one, and <code>--fallback-model</code> no longer only works in
headless mode (<code>--print</code>) but in interactive sessions too. Among the slash commands
themselves, <code>/import</code> gained "cursor" as a third supported source, and <code>/plan</code>
lost the "share" sub-option from its argument hint.</p>
"""
