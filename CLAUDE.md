# Hinweise für Claude

Notizen an mein künftiges Ich. Hier steht, was beim Arbeiten an diesem Repo
wirklich weh tut — nicht, was man sich aus den Dateien selbst zusammenlesen kann.

## Bauweg

Alle drei Anleitungen entstehen gleich: ein Python-Skript schreibt **eine einzige
HTML-Datei**, daraus wird das PDF gedruckt. Kein Framework, keine Abhängigkeiten
außer dem Drucker.

- Comics: `build.py` → HTML → **Chromium headless** → PDF
- Befehlsreferenz: `build_ref.py` → HTML → **WeasyPrint** → PDF

Die Comics brauchen Chromium, weil WeasyPrint das Flexbox-Layout der Panels nicht
sauber umbricht. Umgekehrt reicht der Referenz WeasyPrint völlig.

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

Liegen gemeinsam in `werkzeuge/schriften/`. Beide `build.py` suchen sie **erst neben
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
`~/claude/{befehlsreferenz,claude-anleitung,cowork-anleitung}` — die Dateien in diesem
Repo sind Kopien daraus und sollten nicht direkt bearbeitet werden.

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
