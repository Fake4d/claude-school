# claude-school

***English** · [Deutsch](README.de.md)*

Guides to Claude — **three comics that build on one another**, plus a complete command
reference and a hands-on guide to setting up your own server assistant. Every guide
comes in **English and German**, each as a PDF and as a single HTML file, both
self-contained (fonts embedded, no external files).

The three comics follow one question: **how far do you let Claude at your things?**
In the conversation everything passes through you. With the desktop app Claude works
in your folders. In the terminal it works on the whole machine — and keeps running
without you.

| Guide | Length | Who for |
|---|---|---|
| [**Claude in conversation as a comic**](chat-comic/chat-comic-en.pdf) | 22 pages | Stage 1 — nothing to install: artifacts, projects, memory, research |
| [**Claude Cowork as a comic**](cowork-comic/cowork-comic-en.pdf) | 23 pages | Stage 2 — desktop app: Claude works directly in your folders |
| [**Claude Code as a comic**](claude-code-comic/claude-code-comic-en.pdf) | 34 pages | Stage 3 — terminal: the whole machine, your own tools, runs without you |
| [**Command reference**](befehlsreferenz/Claude-Code-Command-Reference.pdf) | 9 pages | Looking things up — every terminal command, option and slash command |
| [**Your own AI server assistant**](server-setup/AI-Server-Assistant-Edition-3.pdf) | 10 pages | Building it yourself — from an empty rented server to Claude running around the clock |

The German editions live next to them in the same folders; the
[German README](README.de.md) lists them.

## Where the content comes from

The **command reference** is not copied from the documentation but read straight out
of the installed build: `claude --help`, the help of every subcommand, and the command
definitions inside the program itself. As of version 2.1.234 — 62 options,
124 available slash commands, 5 present but switched off. A scheduled job keeps it
current on every new release of the program.

The **comics** are checked against Anthropic's official documentation rather than
written from memory; the characters and diagrams are hand-written SVG. Both leave out
topics that go stale quickly (prices, usage limits) on purpose.

The **server guide** was followed step by step on a live server. It contains no real
credentials — user name, IP address and mail account are placeholders to replace.

## Building it yourself

The scripts in [`werkzeuge/`](werkzeuge/) ("werkzeuge" = tools) reproduce the files
above byte for byte. Python 3 only, no libraries; for printing you need Chromium
(comics) or WeasyPrint (reference and server guide).

```bash
cd werkzeuge/chat-comic && python3 build.py        # -> both languages
cd werkzeuge/befehlsreferenz && python3 build_ref.py
cd werkzeuge/server-setup && python3 uebersetze.py
```

Note that the tooling itself is written in German — file names, comments and variable
names. The published guides are not.

### How the English edition is produced

There is deliberately **no second build script per language** — that would be the one
copy which eventually falls behind. Instead the German edition is the source, and the
English wording sits beside it in `texte_en.py`:

- **Command reference:** `texte_de.py` and `texte_en.py` carry the same keys;
  `build_ref.py` writes both editions in a single run.
- **Comics and server guide:** `i18n.py` swaps the content of every text element in the
  finished HTML for its entry in `texte_en.py`. Layout, artwork and commands are left
  untouched.

The point of it is the completeness check: if a German text has no English
counterpart, **the build stops** and names the missing sentence. So a changed German
passage cannot quietly stay German.

### Finding pages that got cut off

The comic pages have a fixed height and `overflow:hidden` — too much content is
silently cut off when printing, with no error message.
[`werkzeuge/qa-ueberlauf.py`](werkzeuge/qa-ueberlauf.py) measures, for every page, the
distance from the outermost ink to all four edges of the sheet and reports what gets
too tight.

```bash
python3 werkzeuge/qa-ueberlauf.py cowork-comic/cowork-anleitung.pdf
```

Exit code 1 on suspicion — so it can be hung into a publishing pipeline as a gate.
That is exactly how it is used here: nothing gets published without passing. It works
for any PDF with a fixed page size, not just these comics.

## Licence and credits

The comics go back to an English Instagram comic by *okaashish* — characters and
dramaturgy are borrowed, the content rewritten and brought up to August 2026.
Fonts: *Patrick Hand* and *Caveat* (SIL Open Font License).
