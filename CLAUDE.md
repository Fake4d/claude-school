# Hinweise für Claude

Notizen an mein künftiges Ich. Hier steht, was beim Arbeiten an diesem Repo
wirklich weh tut — nicht, was man sich aus den Dateien selbst zusammenlesen kann.

## Bauweg

Alle Anleitungen entstehen gleich: ein Python-Skript schreibt **eine einzige
HTML-Datei je Sprache**, daraus wird das PDF gedruckt. Kein Framework, keine Abhängigkeiten
außer dem Drucker.

- Comics (vier Stück, eines davon ein Special): `build.py` → HTML → **Chromium headless** → PDF
- Befehlsreferenz: `build_ref.py` → HTML → **WeasyPrint** → PDF
- Server-Anleitung: **handgeschriebenes HTML** → WeasyPrint → PDF
- Englische Fassungen: aus der deutschen abgeleitet, siehe „Zweisprachig“ weiter unten

Die Comics brauchen Chromium, weil WeasyPrint das Flexbox-Layout der Panels nicht
sauber umbricht. Umgekehrt reicht der Referenz WeasyPrint völlig.

Die Server-Anleitung ist die Ausnahme: Sie hat **kein** Bauskript, die HTML-Datei
selbst ist die Quelle und wird direkt bearbeitet. Sie liegt unter
`~/claude/server-setup-quelle/anleitung-v3.html` (bis 28.08.2026 `~/claude/florian/` —
die erste Ausgabe war für einen Bekannten geschrieben, der Ordner trug lange dessen
Namen; beim Aufräumen umbenannt). Beim Veröffentlichen wird sie in
`KI-Server-Assistent-Ausgabe-3.*` umbenannt; die Umbenennung erledigt
`zielname_von()` im Veröffentlichungsskript.

**Bei einer neuen Ausgabe** sind es fünf Stellen: `<title>`, die Fußzeile in `@page`,
der Titelkasten, der Kasten „Was in dieser Ausgabe neu ist" — und `zielname_von()`
im Veröffentlichungsskript, sonst landet die neue Ausgabe unter dem alten Dateinamen.

## Chromium auf diesem Server (Snap)

Ein direkter Aufruf scheitert am Cgroup-Check. Der Weg, der ohne `sudo` funktioniert:

```bash
SNAP=/snap/chromium/current
export LD_LIBRARY_PATH=$SNAP/usr/lib/chromium-browser:$SNAP/usr/lib/x86_64-linux-gnu:$SNAP/lib/x86_64-linux-gnu:$SNAP/usr/lib
$SNAP/usr/lib/chromium-browser/chrome --headless --disable-gpu --no-sandbox \
  --no-pdf-header-footer --print-to-pdf=AUSGABE.pdf "file:///…/datei.html"
```

**Fallstrick:** Über den `systemd-run`-Weg darf die Ausgabe nicht nach `/tmp` gehen —
die Snap-Sandbox schreibt dann wortlos keine Datei. Beim Direktaufruf oben gilt das
nicht.

## Überlauf-QA — bitte nicht überspringen

Die Comicseiten haben feste Höhe (`210×262 mm`) und `overflow:hidden`. Zu viel Inhalt
wird also **stillschweigend abgeschnitten**, ohne Fehlermeldung. Beim Durchblättern
übersieht man das zuverlässig.

Dafür gibt es `werkzeuge/qa-ueberlauf.py` — nicht von Hand nachbauen:

```bash
python3 werkzeuge/qa-ueberlauf.py pfad/zur.pdf     # Rückgabewert 1 bei Verdacht
python3 werkzeuge/qa-ueberlauf.py --alle pfad.pdf  # auch die sauberen Seiten zeigen
```

Es wandelt das PDF mit `pdftoppm -jpeg -r 50` in Bilder und misst je Seite den
Abstand der äußersten nicht-weißen Pixel zu allen **vier** Rändern; unter ~10 px gilt
als verdächtig. Das Veröffentlichungsskript ruft **genau diese Datei** auf — es gibt
also keine zweite Fassung, die altern könnte. Wer hier etwas ändert, ändert damit
auch die Sperre vor dem Veröffentlichen.

Zwei Dinge, die ich auf die harte Tour gelernt habe:

1. **Alle vier Ränder prüfen, nicht nur unten.** Eine frühere Fassung prüfte nur
   nach unten — dabei war eine Seite rechts abgeschnitten (ein Kasten halb weg) und
   fiel wochenlang nicht auf.
2. **Oben ist immer ~8 px.** Das ist der Seitenzahl-Aufkleber, der absichtlich weit
   oben sitzt. Diesen Rand von der Prüfung ausnehmen, sonst meldet jede Seite Alarm.

Typische Ursachen für Überlauf: zu lange Beschriftungen in `.chain` (steht auf
`nowrap` und wächst seitlich raus) und `.window` mit `min-width`, das eine
zweispaltige Anordnung breiter macht als die Seite.

## Deutsche Anführungszeichen brechen Python

Im Fließtext gehören `„…“` — also unten-öffnend, **oben**-schließend. Schreibt man
aus Versehen `„…"` mit geradem ASCII-Zeichen am Ende, beendet das den Python-String
und `build.py` stirbt mit `unterminated string literal`. Ist mir passiert; wenn der
Fehler auftaucht, zuerst danach greppen.

## Schriften

Liegen gemeinsam in `werkzeuge/schriften/`. Alle `build.py` suchen sie **erst neben
sich, dann in `../schriften`** — damit dasselbe Skript sowohl im Repo als auch in
einem flachen Arbeitsordner läuft. Diese Doppelsuche bitte erhalten, sonst bricht
einer der beiden Wege.

Sie werden als base64 direkt ins HTML eingebettet. Deshalb sind die HTML-Dateien
je rund ein Megabyte groß — das ist Absicht, nicht Versehen: die Dateien sollen ohne
Internet und ohne Nebendateien überall gleich aussehen.

## Befehlsreferenz auf eine neue Version heben

1. `python3 extract_slash.py <version>` — liest die Slash-Befehle direkt aus der
   installierten Binärdatei unter `~/.local/share/claude/versions/<version>`.
2. `claude --help` und die Hilfe jedes Unterbefehls neu abziehen und **gegen die
   Vorfassung diffen**. Ist beides zeichengleich, dann auch genau das schreiben,
   statt Änderungen zu behaupten.
3. In `build_ref.py` `VERSION` und `VORGAENGER` setzen.
4. Bauen. Fehlen Übersetzungen, bricht das Skript ab und nennt sie — nachtragen in
   `texte_de.py`.

Beim Sprung 2.1.228 → 2.1.229 war inhaltlich **nichts** anders; verändert hatten sich
nur interne, minifizierte Bezeichner. Solche Nullrunden ehrlich als Nullrunde
benennen — das war dem Auftraggeber ausdrücklich mehr wert als eine schöngeredete
Änderungsliste.

## Die Server-Anleitung beschreibt diesen Server

Sie ist keine ausgedachte Anleitung, sondern die Bauanleitung für genau das Setup, auf
dem sie entsteht. Daraus folgt zweierlei.

**Was hier gelernt wird, gehört hinein.** Beispiel: Dass dem Systemdienst
`--continue` fehlte und er nach jedem Neustart bei null anfing, fiel im Alltag auf —
in Ausgabe 3 steht es. Wer am Setup etwas verbessert, sollte prüfen, ob die Anleitung
nachzuziehen ist.

**Nichts Persönliches darf hinein.** Vor jeder Veröffentlichung prüfen: echte
IP-Adressen, Mailadressen, Domains, den ntfy-Kanalnamen, Namen Dritter. Der Kanalname
ist besonders heikel, weil ntfy-Kanäle öffentlich lesbar sind — im Text steht deshalb
ein erfundener Beispielname, nie der echte. Platzhalter sind `meinname` (Benutzer),
`203.0.113.10` (Dokumentations-IP nach RFC 5737) und `ich@meinprovider.de`.

## Inhaltliche Genauigkeit

Produktfragen rund um Anthropic **nachschlagen, nicht aus dem Gedächtnis schreiben.**
Cowork lag hinter meinem Wissensstand, und eine frühere Auskunft aus
Drittanbieter-Artikeln war schlicht falsch („nur macOS“ — tatsächlich gibt es das
für Windows und Mac, im Browser und am Handy). Der Cowork-Comic ist deshalb
durchgehend gegen die offizielle Dokumentation geprüft.

## Veröffentlichen

Nicht von Hand kopieren. Ein Skript **außerhalb** dieses Repos erledigt beide Ziele
zugleich — Git und Webseite:

```
~/claude/bin/anleitungen-veroeffentlichen.sh        # bauen, prüfen, Git + Web
~/claude/bin/anleitungen-veroeffentlichen.sh -n     # Probelauf
```

Es liegt bewusst **nicht** in diesem Repo, und das aus zwei Gründen: Es braucht die
FTP-Zugangsdaten (`~/claude/state/ftp.conf`), und es enthält Domain, Mailadressen und
absolute Pfade eines bestimmten Servers — nichts davon gehört in ein öffentliches
Repo. Was daran allgemein brauchbar ist, ist stattdessen als eigenes Werkzeug
herausgelöst und hier veröffentlicht: `werkzeuge/qa-ueberlauf.py`.

Quelle sind immer die Arbeitsordner
`~/claude/{befehlsreferenz,claude-anleitung,cowork-anleitung,loop-anleitung}` — die
Dateien in diesem Repo sind Kopien daraus und sollten nicht direkt bearbeitet werden.

Ein zweites Skript außerhalb, `~/claude/bin/refcheck.sh`, läuft täglich per cron und
vergleicht die installierte Claude-Fassung mit der zuletzt veröffentlichten. Nur bei
einer neuen Fassung wird gearbeitet. **Verschwindet dabei ein Slash-Befehl, bricht es
ab und fragt nach**, statt zu veröffentlichen — siehe den Abschnitt dazu weiter unten.

**Chromium stempelt ein Erstellungsdatum ins PDF.** Die Comic-PDFs unterscheiden sich
deshalb nach jedem Druck, auch wenn sich inhaltlich nichts geändert hat. Das Skript
fängt das ab: Ist das HTML unverändert, behält es die alte PDF-Fassung, statt einen
nichtssagenden Commit zu erzeugen.

## Reproduzierbarkeit

Die Skripte in `werkzeuge/` erzeugen die Dateien oben **byte-identisch**. Das ist
geprüft und soll so bleiben: Wer etwas am Inhalt ändert, ändert das Skript und baut
neu — nicht die fertige Datei von Hand.

## Zweisprachig: Deutsch ist die Quelle, Englisch fällt daraus ab

Seit dem 17.08.2026 gibt es jede Anleitung auch auf Englisch. Wichtigste Regel:
**Es gibt kein zweites Bauskript je Sprache.** Der Versuch wäre der klassische Weg
in zwei Fassungen, die auseinanderlaufen. Stattdessen:

- **Befehlsreferenz:** `texte_de.py` und `texte_en.py` tragen dieselben Schlüssel
  (Original-Bezeichner aus dem Programm), dazu je ein `SEITE`-Wörterbuch mit den
  Überschriften und Kästen. `build_ref.py` schreibt **beide** Fassungen in einem Lauf.
  Der Änderungskasten steht in `aenderungen.py` — DE und EN in **einer** Datei, damit
  beim Versionswechsel nur eine Stelle anzufassen ist.
- **Comics und Server-Anleitung:** `i18n.py` nimmt das fertige deutsche HTML und
  tauscht den Inhalt jedes Blatt-Elements gegen den Eintrag aus `texte_en.py`.
  Schlüssel ist der deutsche Text **einschließlich der Auszeichnung darin**
  (`<b>`, `<code>`, `<span class="chip-sub">`) — die trägt das Layout und muss auf
  beiden Seiten gleich aussehen.

Das Sicherheitsnetz ist die Vollständigkeitsprüfung: Fehlt zu einem deutschen Text
das Gegenstück, **bricht der Bau ab** und nennt den fehlenden Satz. Wer also einen
deutschen Satz umformuliert, bekommt die englische Nacharbeit sofort aufs Auge —
und nicht erst der Leser drei Monate später.

Zwei Dinge, die beim Umbau aufgefallen sind:

1. **Englisch ist nicht automatisch kürzer.** Auf der Dispatch-Seite des
   Cowork-Comics lief die `.chain` seitlich aus dem Blatt, weil vier Kettenglieder
   in der Übersetzung länger geraten waren (`.chain` steht auf `nowrap`). Die
   Überlauf-QA hat es gefunden — sie läuft deshalb über **alle vier** Comic-PDFs,
   nicht nur die deutschen.
2. **In Codeblöcken steckt Text.** `i18n.uebersetze(..., pre=True)` behandelt einen
   ganzen `<pre>`-Block als eine Einheit. Das ist für die Server-Anleitung nötig:
   dort steht Deutsch nicht nur in den Kommentar-Spans, sondern auch in
   `echo`-Ausgaben und in den Beispielaufträgen an Claude. Die Befehle selbst bleiben
   Zeichen für Zeichen gleich; der Platzhalter-Benutzer heißt englisch `myname`.

Die englischen Dateinamen sind fest und werden von `zielname_von()` im
Veröffentlichungsskript vergeben: `Claude-Code-Command-Reference.*`,
`claude-code-comic-en.*`, `cowork-comic-en.*`, `loop-comic-en.*`,
`AI-Server-Assistant-Edition-3.*`, `setup-prompt-en.txt`. Auf der Webseite liegen sie **im selben Ordner** wie die
deutschen; die Projektseiten bleiben deutsch und bekommen nur eine Zeile mit dem
Verweis darauf.

Die README ist gespalten: `README.md` ist die englische Kurzfassung, `README.de.md`
die ausführliche deutsche. Beide tragen oben den Sprachlink, und beide haben einen
Stand-Satz zur Referenzfassung, den das Veröffentlichungsskript automatisch nachzieht.

## Die drei Comics sind eine Leiter, keine Sammlung

Seit dem 18.08.2026 gibt es drei Comics, und sie bauen aufeinander auf. Die Achse ist
**nicht** „Büroarbeit oder Programmieren“ — das war die alte, zu enge Lesart. Die Achse
ist: **wie weit lässt Du Claude an Deine Sachen?**

| Stufe | Heft | Claude arbeitet … |
|---|---|---|
| 1 | `chat-comic/` | … im Gespräch. Alles geht durch Dich: hochladen, herunterladen. |
| 2 | `cowork-comic/` | … in Deinen Ordnern (Desktop-App). |
| 3 | `claude-code-comic/` | … auf dem ganzen Rechner, mit eigenen Werkzeugen, auch ohne Dich. |

Zwei Dinge, die man dabei falsch machen kann und die hier schon geprüft sind:

- **„Cowork = Desktop-App“ stimmt nicht ganz.** Cowork gibt es auch im Browser und am
  Handy; exklusiv ist der Desktop-App nur die **Ordnerfreigabe**. Die Stufengrenze ist
  also der Ordnerzugriff, nicht die App.
- **„Claude Code = Programmieren“ stimmt auch nicht.** Dieses Repo selbst ist der
  Gegenbeweis: Comics, PDFs, Webseiten, cron, Mail. Der Unterschied zu Stufe 2 ist der
  Zugriff auf den ganzen Rechner plus zwei Dinge, die es nur dort gibt — Claude eigene
  Werkzeuge beibringen (CLAUDE.md, Skills, MCP, Hooks) und dauerhaft ohne Dich laufen
  lassen.

Die Faustregel für den Leser: *etwas erledigen lassen* → Cowork. *Werkzeuge bauen, die
danach von allein laufen* → Code.

Auch inhaltlich sauber trennen: **Artifacts gehören in Stufe 1**, nicht in den
Cowork-Comic. Cowork erzeugt echte Dateien in Deinen Ordnern; ein Artifact entsteht im
Gespräch und bleibt dort. Genau dieser Unterschied macht die Stufen erst verständlich —
wer Artifacts in Cowork nachrüstet, verwischt ihn.

Der Chat-Comic ist gegen die offizielle Dokumentation geprüft (18.08.2026). Ein Fund
daraus, der die Stufengrenze schärft: **Auch der normale Chat baut echte Dateien** —
xlsx, docx, pptx, pdf, auf allen Plänen. Aber in einem abgeschotteten Bereich, den man
herunterlädt. Der Comic sagt das ausdrücklich, sonst wirkt Stufe 2 überflüssig.

**Seit dem 28.08.2026 gibt es dazu ein Special, `loop-comic/`.** Es ist bewusst
**kein** vierte Stufe — die Leiter bleibt bei drei Stufen entlang der Zugriffsfrage.
Das Special vertieft stattdessen ein einzelnes Thema *innerhalb* von Stufe 3
(`/loop` als Baustein für dauerhaft laufende Routinen: Auto-Pacing, Verifikation,
Tuning, Worktree-Isolation) und wird auf der Webseite auch entsprechend als
Bonusheft zu Comic 3 präsentiert, nicht als gleichrangiger vierter Punkt der Leiter.

## Verschwundene Slash-Befehle sind fast immer ein Auslesefehler

Am 14.08.2026 meldete der Abgleich, `/loop` sei entfallen. Tatsächlich war nur dessen
Name im Programm von einem Textliteral in eine Variable gewandert (`TEn="loop"`) —
Nebenprodukt des Verdichtens beim Bauen. `extract_slash.py` löst Namen deshalb jetzt
über eine **einmalig** aufgebaute Zuordnungstabelle auf; einzeln zu suchen wäre
unbezahlbar, die Datei hat rund 300 Mio Zeichen.

Wer daran wieder etwas ändert: **immer gegen die vorige Fassung gegenprüfen.** Der
reparierte Extraktor muss dort dieselben Befehle finden wie zuvor, nur eben mehr —
verlieren darf er keinen. Bei über Variablen aufgelöste Namen ist die
Verwechslungsgefahr höher, deshalb fliegen Treffer mit einer Ein-Wort-Beschreibung
(etwa `"method"`) wieder raus.

Praktisch heißt Gegenprüfen: den Extraktor aus einem Scratch-Ordner heraus für die
neue **und** die vorige Fassung laufen lassen und die erzeugten `slash-*.json` gegen
die in `befehlsreferenz/` liegenden vergleichen — der Unterschied darf nur aus
Ergänzungen bestehen, kein Feld eines bestehenden Eintrags (`desc`, `hint`,
`aliases`, `verfuegbar`) darf sich ändern. Erst dann in Ort und Stelle auslesen.

**Die Handbremse sieht nur, was zwischen zwei Fassungen verschwindet — nicht, was
schon vorher fehlte.** So fehlten `/artifact-pr-review`, `/code-review`,
`/ultrareview`, `/exit` und `/claude-code-docs` monatelang unbemerkt: Anker mit
gültigem Namen, aus denen sich kein Beschreibungstext lesen ließ, wurden wortlos
verworfen. Seit 05.09.2026 zählt `extract_slash.py` diese Fälle (`VERWORFEN`) und
gibt eine Zeile `VERWORFEN: N neu · M bekannt offen` aus, die `refcheck.sh` loggt
und bei `N>0` per Mail meldet. Die Beschreibung darf inzwischen fester Text,
Pfeilfunktion, Getter, Array, Backtick-Vorlage, Aliaskette (`E=A+\`…\``) oder eine
Hilfsfunktion (`get description(){return msr()}`, `description:_i` mit
`function _i(){…}`) sein; Laufzeitteile `${…}` werden zu „…". Letzter Rückfall ist
`menuDescription`. Die Liste der Bauformen steht im Docstring von `_text_suchen()`.
