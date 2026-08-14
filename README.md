# claude-school

Deutschsprachige Anleitungen zu Claude — zwei Comics für den Einstieg und eine
vollständige Befehlsreferenz. Jede Anleitung gibt es als PDF und als HTML-Datei,
beide in sich abgeschlossen (Schriften eingebettet, keine externen Dateien).

| Anleitung | Umfang | Für wen |
|---|---|---|
| [**Claude Cowork als Comic**](cowork-comic/cowork-anleitung.pdf) | 23 Seiten | Einstieg ohne Programmierkenntnisse — Cowork läuft in der normalen Claude-App, ohne Terminal |
| [**Claude Code als Comic**](claude-code-comic/claude-anleitung.pdf) | 34 Seiten | Einstieg für alle, die im Terminal arbeiten — CLAUDE.md, Skills, MCP, Hooks, Subagents |
| [**Befehlsreferenz**](befehlsreferenz/Claude-Code-Befehlsreferenz-2.1.229.pdf) | 8 Seiten | Nachschlagen — alle Terminal-Befehle, Optionen und Slash-Befehle |

## Woher die Inhalte stammen

Die **Befehlsreferenz** ist nicht abgeschrieben, sondern direkt aus der installierten
Fassung ausgelesen: `claude --help`, die Hilfe jedes Unterbefehls und die
Befehlsdefinitionen im Programm selbst. Stand: Version 2.1.229 — 62 Optionen,
109 verfügbare Slash-Befehle, 5 angelegt aber abgeschaltet.

Die **Comics** sind gegen die offizielle Anthropic-Dokumentation geprüft, nicht aus
dem Gedächtnis geschrieben. Figuren und Schaubilder sind handgeschriebenes SVG.

Beide Comics lassen bewusst Themen aus, die schnell veralten (Preise, Nutzungsgrenzen).
Was fehlt, steht am Ende der jeweiligen Projektseite.

## Selbst bauen

Die Skripte in [`werkzeuge/`](werkzeuge/) sind die Werkzeuge zur Erstellung — sie
erzeugen die Dateien oben byte-identisch. Nur Python 3 nötig, keine Bibliotheken;
zum Drucken Chromium (Comics) bzw. WeasyPrint (Referenz).

```bash
cd werkzeuge/cowork-comic && python3 build.py     # -> cowork-anleitung.html
cd werkzeuge/befehlsreferenz && python3 build_ref.py
```

Jede Anleitung hat ihren eigenen Ordner, die Schriften liegen gemeinsam in
`werkzeuge/schriften/`. Details und Fallstricke stehen in [`CLAUDE.md`](CLAUDE.md).

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
