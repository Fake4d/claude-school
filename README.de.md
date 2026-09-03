# claude-school

*[English](README.md) · **Deutsch***

Anleitungen zu Claude — **drei Comics in aufeinander aufbauenden Stufen**, dazu ein
Special, eine vollständige Befehlsreferenz und eine Praxisanleitung zum
Selbstaufsetzen. Jede Anleitung gibt es auf **Deutsch und Englisch**, jeweils als PDF
und als HTML-Datei, beide in sich abgeschlossen (Schriften eingebettet, keine
externen Dateien).

Die drei Comics folgen einer Frage: **wie weit lässt Du Claude an Deine Sachen?**
Im Gespräch geht alles durch Dich hindurch. Mit der Desktop-App arbeitet Claude in
Deinen Ordnern. Im Terminal arbeitet es auf dem ganzen Rechner — und läuft ohne Dich
weiter. Das **Loop-Engineering-Special** baut auf Stufe 3 auf, gehört aber nicht zur
Leiter: es vertieft nur ein einzelnes Thema (`/loop` im Dauerbetrieb).

| Anleitung | Umfang | Für wen | Englisch |
|---|---|---|---|
| [**Claude im Gespräch als Comic**](chat-comic/chat-anleitung.pdf) | 22 Seiten | Stufe 1 — nichts zu installieren: Artifacts, Projekte, Gedächtnis, Research | [PDF](chat-comic/chat-comic-en.pdf) |
| [**Claude Cowork als Comic**](cowork-comic/cowork-anleitung.pdf) | 23 Seiten | Stufe 2 — Desktop-App: Claude arbeitet direkt in Deinen Ordnern | [PDF](cowork-comic/cowork-comic-en.pdf) |
| [**Claude Code als Comic**](claude-code-comic/claude-anleitung.pdf) | 34 Seiten | Stufe 3 — Terminal: der ganze Rechner, eigene Werkzeuge, läuft ohne Dich | [PDF](claude-code-comic/claude-code-comic-en.pdf) |
| [**Loop Engineering als Comic**](loop-comic/loop-anleitung.pdf) | 9 Seiten | Special — Bonusheft zu Stufe 3: aus `/loop` wird eine Werkstatt aus Routinen im Dauerbetrieb | [PDF](loop-comic/loop-comic-en.pdf) |
| [**Befehlsreferenz**](befehlsreferenz/Claude-Code-Befehlsreferenz.pdf) | 9 Seiten | Nachschlagen — alle Terminal-Befehle, Optionen und Slash-Befehle | [PDF](befehlsreferenz/Claude-Code-Command-Reference.pdf) |
| [**Dein eigener KI-Server-Assistent**](server-setup/KI-Server-Assistent-Ausgabe-3.pdf) | 10 Seiten | Selbst aufsetzen — vom leeren Mietserver zum Claude im Dauerbetrieb | [PDF](server-setup/AI-Server-Assistant-Edition-3.pdf) |

## Woher die Inhalte stammen

Die **Befehlsreferenz** ist nicht abgeschrieben, sondern direkt aus der installierten
Fassung ausgelesen: `claude --help`, die Hilfe jedes Unterbefehls und die
Befehlsdefinitionen im Programm selbst. Stand: Version 2.1.259 — 64 Optionen,
129 verfügbare Slash-Befehle, 5 angelegt aber abgeschaltet. Ein Zeitplan-Auftrag hält
sie bei jeder neuen Programmfassung von selbst aktuell.

Die **Comics** sind gegen die offizielle Anthropic-Dokumentation geprüft, nicht aus dem
Gedächtnis geschrieben; Figuren und Schaubilder sind handgeschriebenes SVG.

Die **Server-Anleitung** ist auf einem laufenden Server Schritt für Schritt
nachvollzogen. Sie enthält keine echten Zugangsdaten — Benutzername, IP-Adresse und
Mailkonto sind Platzhalter zum Ersetzen.

Alle drei Comics lassen bewusst Themen aus, die schnell veralten (Preise, Nutzungsgrenzen).
Was fehlt, steht am Ende der jeweiligen Projektseite.

## Selbst bauen

Die Skripte in [`werkzeuge/`](werkzeuge/) sind die Werkzeuge zur Erstellung — sie
erzeugen die Dateien oben byte-identisch. Nur Python 3 nötig, keine Bibliotheken;
zum Drucken Chromium (Comics) bzw. WeasyPrint (Referenz).

```bash
cd werkzeuge/chat-comic && python3 build.py       # -> beide Sprachen
cd werkzeuge/befehlsreferenz && python3 build_ref.py
cd werkzeuge/server-setup && python3 uebersetze.py
```

Jede Anleitung hat ihren eigenen Ordner, die Schriften liegen gemeinsam in
`werkzeuge/schriften/`. Details und Fallstricke stehen in [`CLAUDE.md`](CLAUDE.md).

### Wie die englische Fassung entsteht

Es gibt bewusst **kein zweites Bauskript je Sprache** — das wäre die eine Kopie, die
irgendwann hinterherhinkt. Stattdessen ist die deutsche Fassung die Quelle, und der
englische Wortlaut steht daneben in `texte_en.py`:

- **Befehlsreferenz:** `texte_de.py` und `texte_en.py` haben dieselben Schlüssel;
  `build_ref.py` schreibt beide Fassungen in einem Lauf.
- **Comics und Server-Anleitung:** `i18n.py` tauscht im fertigen HTML den Inhalt jedes
  Textelements gegen den Eintrag aus `texte_en.py`. Layout, Grafik und Befehle bleiben
  unangetastet.

Der springende Punkt ist die Vollständigkeitsprüfung: Fehlt zu einem deutschen Text
das englische Gegenstück, **bricht der Bau ab** und nennt den fehlenden Satz. Eine
geänderte deutsche Stelle kann also nicht still auf Deutsch stehen bleiben.

### Abgeschnittene Seiten finden

Die Comicseiten haben feste Höhe und `overflow:hidden` — zu viel Inhalt wird beim
Drucken stillschweigend abgeschnitten, ohne Fehlermeldung. Dagegen hilft
[`werkzeuge/qa-ueberlauf.py`](werkzeuge/qa-ueberlauf.py): es misst je Seite den
Abstand der äußersten Tinte zu allen vier Blatträndern und meldet, was zu knapp wird.

```bash
python3 werkzeuge/qa-ueberlauf.py cowork-comic/cowork-anleitung.pdf
```

Rückgabewert 1 bei Verdacht — damit lässt es sich als Sperre in einen
Veröffentlichungsablauf hängen. Genau so wird es hier verwendet: ohne bestandene
Prüfung wird nichts veröffentlicht. Es taugt für jedes PDF mit festem Seitenformat,
nicht nur für diese Comics.

## Lizenz und Hinweise

Die Comics gehen auf einen englischen Instagram-Comic von *okaashish* zurück —
Figuren und Dramaturgie sind übernommen, die Inhalte neu geschrieben und auf
August 2026 gebracht. Schriften: *Patrick Hand* und *Caveat* (SIL Open Font License).
