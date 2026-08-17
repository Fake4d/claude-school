# -*- coding: utf-8 -*-
"""Übersetzt eine fertig gebaute Comicseite in eine andere Sprache.

Warum so und nicht mit Textbausteinen im Bauskript: die Comicseiten sind
Layout und Text in einem Guss — jeder Kasten, jede Beschriftung, jede
Sprechblase steckt mitten im HTML. Ein zweites Bauskript je Sprache würde
mit dem ersten auseinanderlaufen, und jeden Text einzeln zu verpacken hätte
das Layout unlesbar gemacht.

Stattdessen läuft das deutsche Ergebnis durch dieses Modul: es sucht alle
Blatt-Elemente (solche, die nur Text und Inline-Auszeichnung enthalten) und
tauscht deren Inhalt gegen den Eintrag aus dem Wörterbuch. Dadurch gibt es
weiterhin genau EIN Bauskript, und ein neuer deutscher Text kann nicht still
untergehen: fehlt sein Gegenstück, bricht der Bau mit einer Liste ab.

Nicht übersetzt werden Inhalte ohne Buchstaben (Pfeile, Ziffern, Zeichen) —
die sind in jeder Sprache gleich und blähen das Wörterbuch nur auf.
"""
import re

# Auszeichnung, die innerhalb eines Satzes stehen darf, ohne ihn zu zerteilen.
INLINE = "code|b|i|em|strong|kbd|br|span|sup|sub|small|a|u"
# Elemente, deren Inhalt eine Übersetzungseinheit sein kann.
BLOCK = "div|p|span|b|i|li|td|th|h1|h2|h3|h4|text|a|figcaption"

def _muster(pre):
    """pre=True: ein ganzer <pre>-Block ist EINE Einheit (Befehl samt Kommentaren).

    Gebraucht für Anleitungen mit Codeblöcken: dort steht deutscher Text auch
    ausserhalb der Kommentar-Spans, etwa in einem echo oder in einem
    Beispielauftrag an Claude.
    """
    bloecke = ("pre|" + BLOCK) if pre else BLOCK
    return re.compile(
        r"<(" + bloecke + r")\b([^>]*)>"
        r"((?:[^<]|<(?:" + INLINE + r")\b[^>]*>|</(?:" + INLINE + r")>)*?)"
        r"</\1>",
        re.DOTALL)


EINHEIT = _muster(False)

_BUCHSTABE = re.compile(r"[A-Za-zÀ-ÿ]")
_TAG = re.compile(r"<[^>]+>")


def hat_text(inhalt):
    """Buchstaben nur im sichtbaren Teil zählen, nicht in Attributen —
    sonst gälten die Strichlinien der Dokument-Symbole als Text."""
    return bool(_BUCHSTABE.search(_TAG.sub("", inhalt)))


def _ohne_stil(html):
    """Grenzen des <style>-Blocks, der nie angefasst wird."""
    m = re.search(r"<style\b.*?</style>", html, re.DOTALL)
    return (m.start(), m.end()) if m else (-1, -1)


def einheiten(html, pre=False):
    """Alle Übersetzungseinheiten der Seite, in Reihenfolge, ohne Dubletten."""
    stil_a, stil_e = _ohne_stil(html)
    gesehen, raus = set(), []
    for m in _muster(pre).finditer(html):
        if stil_a <= m.start() < stil_e:
            continue
        inhalt = m.group(3)
        if not hat_text(inhalt) or inhalt in gesehen:
            continue
        gesehen.add(inhalt)
        raus.append(inhalt)
    return raus


def uebersetze(html, woerterbuch, pre=False):
    """Seite übersetzen. Gibt (neues_html, fehlende_texte) zurück."""
    stil_a, stil_e = _ohne_stil(html)
    fehlt, ersetzungen = [], []
    for m in _muster(pre).finditer(html):
        if stil_a <= m.start() < stil_e:
            continue
        inhalt = m.group(3)
        if not hat_text(inhalt):
            continue
        if inhalt not in woerterbuch:
            if inhalt not in fehlt:
                fehlt.append(inhalt)
            continue
        ersetzungen.append((m.start(3), m.end(3), woerterbuch[inhalt]))
    # von hinten nach vorn, damit die Fundstellen davor gültig bleiben
    for a, e, neu in reversed(ersetzungen):
        html = html[:a] + neu + html[e:]
    return html, fehlt
