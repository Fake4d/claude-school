#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt die englische Server-Anleitung aus der deutschen.

Anders als die Comics und die Befehlsreferenz hat diese Anleitung kein
Bauskript — anleitung-v3.html ist von Hand geschrieben und damit selbst die
Quelle. Die englische Fassung entsteht deshalb daraus: jedes Textelement wird
gegen texte_en.py getauscht, alles andere (Layout, Farben, Befehle) bleibt
Zeichen für Zeichen gleich.

    python3 uebersetze.py            -> anleitung-v3-en.html

Fehlt eine Übersetzung, bricht der Lauf ab und nennt den fehlenden Text. So
kann eine geänderte deutsche Stelle nicht still im Englischen stehen bleiben.
"""
import pathlib, sys
import i18n, texte_en

HERE = pathlib.Path(__file__).parent
QUELLE = HERE / "anleitung-v3.html"
ZIEL = HERE / "anleitung-v3-en.html"

html = QUELLE.read_text(encoding="utf-8")
# pre=True: Codeblöcke sind je EINE Einheit - in ihnen steht deutscher Text auch
# ausserhalb der Kommentar-Spans (echo-Ausgaben, Beispielaufträge an Claude).
en, fehlt = i18n.uebersetze(html, texte_en.TEXTE, pre=True)

if fehlt:
    print("FEHLENDE ÜBERSETZUNGEN (texte_en.py):")
    for f in fehlt:
        print("   ", repr(f))
    sys.exit(1)

# Was ausserhalb der Textelemente steht: Sprachkennung, Titel, Seitenfusszeile.
ersetzungen = [
    ('<html lang="de">', '<html lang="en">'),
    ("<title>Dein eigener KI-Server-Assistent — Ausgabe 3</title>",
     f"<title>{texte_en.TITEL}</title>"),
    ('content: "Dein eigener KI-Server-Assistent · Ausgabe 3";',
     f'content: "{texte_en.FUSS_MITTE}";'),
    ('content: "Seite " counter(page) " / " counter(pages);',
     f"content: {texte_en.FUSS_RECHTS};"),
]
for alt, neu in ersetzungen:
    if alt not in en:
        print(f"WARNUNG: nicht gefunden, bitte pruefen: {alt[:60]}")
    en = en.replace(alt, neu, 1)

ZIEL.write_text(en, encoding="utf-8")
print(f"geschrieben: {ZIEL.name}  ({len(en)/1024:.0f} KB)")
