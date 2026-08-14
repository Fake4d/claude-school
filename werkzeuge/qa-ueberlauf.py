#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Findet abgeschnittene Seiten in einem PDF mit festem Seitenformat.

Die Comicseiten haben eine feste Höhe und `overflow:hidden`. Zu viel Inhalt wird
deshalb beim Drucken **stillschweigend abgeschnitten** — keine Fehlermeldung, und
beim Durchblättern übersieht man es zuverlässig.

Dieses Werkzeug misst je Seite, wie weit die äußerste Tinte vom Blattrand entfernt
ist. Wird ein Rand zu knapp, ist die Seite verdächtig.

    python3 qa-ueberlauf.py datei.pdf [weitere.pdf ...]
    python3 qa-ueberlauf.py --alle datei.pdf     # auch unauffällige Seiten zeigen

Rückgabewert 1, wenn mindestens eine Seite verdächtig ist — so lässt sich das
Werkzeug als Sperre in einen Veröffentlichungsablauf hängen.

Zwei Dinge, die auf die harte Tour gelernt wurden:

1. **Alle vier Ränder prüfen, nicht nur unten.** Eine frühere Fassung sah nur nach
   unten — dabei war eine Seite rechts abgeschnitten und fiel lange nicht auf.
2. **Der obere Rand ist bei diesen Comics immer knapp**, weil der Seitenzahl-
   Aufkleber absichtlich weit oben sitzt. Er wird deshalb nicht geprüft; mit
   `--oben` lässt sich das abschalten.

Braucht `pdftoppm` (Paket poppler-utils) und Pillow.
"""
import argparse
import glob
import os
import subprocess
import sys
import tempfile

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow fehlt:  pip install pillow")

SCHWELLE = 10      # Pixel bei 50 dpi; darunter gilt ein Rand als zu knapp
AUFLOESUNG = 50    # grob genug für Tempo, fein genug für den Zweck
HELL = 240         # alles Dunklere zählt als Tinte


def raender(bildpfad):
    """Abstand der äußersten Tinte zu oben, unten, links, rechts (in Pixeln)."""
    bild = Image.open(bildpfad).convert("L")
    breite, hoehe = bild.size
    px = bild.load()

    oben = unten = links = rechts = None
    for y in range(hoehe):
        if any(px[x, y] < HELL for x in range(breite)):
            oben = y
            break
    if oben is None:
        return None                      # leere Seite, nichts zu prüfen
    for y in range(hoehe - 1, -1, -1):
        if any(px[x, y] < HELL for x in range(breite)):
            unten = hoehe - 1 - y
            break
    for x in range(breite):
        if any(px[x, y] < HELL for y in range(hoehe)):
            links = x
            break
    for x in range(breite - 1, -1, -1):
        if any(px[x, y] < HELL for y in range(hoehe)):
            rechts = breite - 1 - x
            break
    return {"oben": oben, "unten": unten, "links": links, "rechts": rechts}


def pruefe(pdf, schwelle, mit_oben, alle_zeigen):
    with tempfile.TemporaryDirectory() as tmp:
        stamm = os.path.join(tmp, "seite")
        try:
            subprocess.run(["pdftoppm", "-jpeg", "-r", str(AUFLOESUNG), pdf, stamm],
                           check=True, capture_output=True)
        except FileNotFoundError:
            sys.exit("pdftoppm fehlt:  apt install poppler-utils")
        except subprocess.CalledProcessError as e:
            sys.exit(f"pdftoppm scheiterte an {pdf}: {e.stderr.decode()[:200]}")

        zu_pruefen = ["unten", "links", "rechts"] + (["oben"] if mit_oben else [])
        verdaechtig = []
        for bild in sorted(glob.glob(stamm + "-*.jpg")):
            nr = os.path.basename(bild).split("-")[-1].split(".")[0]
            r = raender(bild)
            if r is None:
                continue
            eng = [k for k in zu_pruefen if r[k] < schwelle]
            if eng:
                verdaechtig.append(nr)
                print(f"  Seite {nr}: zu knapp {', '.join(eng)}   "
                      + " ".join(f"{k}={r[k]}" for k in ("oben", "unten", "links", "rechts")))
            elif alle_zeigen:
                print(f"  Seite {nr}: ok   "
                      + " ".join(f"{k}={r[k]}" for k in ("oben", "unten", "links", "rechts")))
        return verdaechtig


def main():
    p = argparse.ArgumentParser(description="Findet abgeschnittene Seiten in PDFs.")
    p.add_argument("pdfs", nargs="+")
    p.add_argument("--schwelle", type=int, default=SCHWELLE,
                   help=f"Randabstand in Pixeln, ab dem gewarnt wird (Vorgabe {SCHWELLE})")
    p.add_argument("--oben", action="store_true",
                   help="oberen Rand mitprüfen (bei den Comics sitzt dort die Seitenzahl)")
    p.add_argument("--alle", action="store_true", help="auch unauffällige Seiten zeigen")
    a = p.parse_args()

    fehler = False
    for pdf in a.pdfs:
        print(f"{os.path.basename(pdf)}:")
        schlimm = pruefe(pdf, a.schwelle, a.oben, a.alle)
        if schlimm:
            print(f"  -> {len(schlimm)} verdächtige Seite(n): {', '.join(schlimm)}")
            fehler = True
        else:
            print("  -> alle Seiten sauber")
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())
