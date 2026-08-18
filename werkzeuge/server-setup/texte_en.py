# -*- coding: utf-8 -*-
"""English wording for the server setup guide.

Key = the German text exactly as it stands in anleitung-v3.html, value = its
English counterpart. Produced and checked by uebersetze.py: if a German
passage changes, the run stops and prints the new key, so the English edition
cannot quietly fall behind.

The code blocks themselves are not translated — only the comments inside them,
because those are separate <span> elements. Commands must stay identical in
both editions.
"""

TEXTE = {

# --- Titelseite ---
"Ausgabe 3 · überarbeitet und geprüft · August 2026":
    "Edition 3 · revised and verified · August 2026",
"Dein eigener<br>KI-Server-Assistent":
    "Your own<br>AI server assistant",
"Vom leeren Linux-Server zum digitalen Kollegen, der dauerhaft läuft, über die\n  Claude-App erreichbar ist und einen Neustart klaglos übersteht.":
    "From an empty Linux server to a digital colleague that runs around the clock,\n  is reachable through the Claude app and survives a reboot without complaint.",
"Geschrieben und Schritt für Schritt nachgeprüft von Christians virtuellem Server<br>\n  Geprüft gegen Claude Code 2.1.232 auf Ubuntu":
    "Written and verified step by step by Christian&#8217;s virtual server<br>\n  Checked against Claude Code 2.1.232 on Ubuntu",

"Was in dieser Ausgabe neu ist": "What is new in this edition",
"Ausgabe 2 brachte dich bis zum Dauerbetrieb. Diese Ausgabe schließt die Lücken,\n  die sich im täglichen Gebrauch gezeigt haben:":
    "Edition 2 got you as far as continuous operation. This edition closes the gaps\n  that showed up in daily use:",
"<strong>Teil 4 weiß jetzt, was der Prompt schon gebaut hat.</strong> Wer den\n        Bootstrap-Prompt vollständig durchläuft, bekommt den Dienst dort bereits — Teil 4\n        sagt nun, was zu prüfen und was zu überspringen ist.":
    "<strong>Part 4 now knows what the prompt has already built.</strong> Anyone who runs the\n        bootstrap prompt all the way through gets the service there already — part 4 now says\n        what to check and what to skip.",
"<strong>Der Dienst nimmt das Gespräch jetzt wieder auf.</strong> Ohne einen kleinen\n        Zusatz in Teil 4 begann er nach jedem Neustart bei null — mitten in der Arbeit\n        besonders ärgerlich.":
    "<strong>The service now picks the conversation back up.</strong> Without one small\n        addition in part 4 it started from scratch after every restart — particularly\n        annoying in the middle of a job.",
"<strong>Teil 7 ist neu:</strong> Push-Nachrichten aufs Handy. Damit meldet sich dein\n        Assistent von selbst, wenn er eine Entscheidung braucht oder etwas Wichtiges\n        passiert ist.":
    "<strong>Part 7 is new:</strong> push notifications to your phone. With it your\n        assistant speaks up by itself when it needs a decision or something important\n        has happened.",
"Alle Befehle und Versionsangaben sind gegen <strong>Claude Code 2.1.232</strong>\n        geprüft.":
    "All commands and version numbers are verified against <strong>Claude Code 2.1.232</strong>.",

# --- Teil 0 ---
"<span class=\"num\">0</span>Was du brauchst":
    "<span class=\"num\">0</span>What you need",
"<strong>Einen kleinen Linux-Server (VPS).</strong> Ein Mietrechner im Internet, der dir allein\n      gehört. Anbieter z. B. Hetzner, netcup, 1blu, IONOS, Strato. Das kleinste Paket reicht\n      (ca. 4–7 € im Monat). Nimm <strong>Ubuntu 24.04 LTS oder neuer</strong>. Zwei Dinge sind wichtig:\n      mindestens <strong>2 GB Arbeitsspeicher</strong> und <strong>10 GB freier Plattenplatz</strong> —\n      Claude Code ist ein großes Programm und behält alte Versionen.":
    "<strong>A small Linux server (VPS).</strong> A rented machine on the internet that is yours\n      alone. Providers include Hetzner, netcup, DigitalOcean, Linode, OVH. The smallest package is\n      enough (roughly &euro;4–7 a month). Take <strong>Ubuntu 24.04 LTS or newer</strong>. Two things\n      matter: at least <strong>2 GB of RAM</strong> and <strong>10 GB of free disk space</strong> —\n      Claude Code is a large program and keeps old versions around.",
"<strong>Ein Claude-Abo</strong> (Pro oder Max). Das kostenlose Claude reicht nicht.":
    "<strong>A Claude subscription</strong> (Pro or Max). The free Claude is not enough.",
"<strong>Ein Terminal.</strong> Auf dem Mac eingebaut, unter Windows das „Windows Terminal“.":
    "<strong>A terminal.</strong> Built into the Mac, on Windows use &#8220;Windows Terminal&#8221;.",
"<strong>Etwa 60 Minuten Zeit.</strong> Mit dem Dauerbetrieb aus Teil 4 eher 75.":
    "<strong>About 60 minutes.</strong> With continuous operation from part 4, closer to 75.",

# --- Teil 1 ---
"<span class=\"num\">1</span>Der Startblock — Server in einem Rutsch startklar":
    "<span class=\"num\">1</span>The starting block — server ready in one go",
"Nach der Bestellung bekommst du eine IP-Adresse und ein Passwort für den Benutzer\n<code>root</code>. Melde dich an (deine IP einsetzen):":
    "After ordering you get an IP address and a password for the user <code>root</code>.\nLog in (substitute your own IP):",
"Beim ersten Mal fragt er <code>Are you sure…?</code> — tippe <code>yes</code>, dann das Passwort.\nJetzt kommt der Block, der alles Weitere vorbereitet. <strong>Ersetze überall\n<code>meinname</code> durch deinen Wunsch-Benutzernamen</strong> und füge ihn dann als Ganzes ein:":
    "The first time it asks <code>Are you sure…?</code> — type <code>yes</code>, then the password.\nNow comes the block that prepares everything else. <strong>Replace <code>myname</code>\neverywhere with the user name you want</strong> and then paste the whole thing in:",
"# ---------- als root, direkt nach dem ersten Login ----------":
    "# ---------- as root, right after the first login ----------",
"# 1) eigenen Benutzer anlegen (fragt nach einem Passwort)":
    "# 1) create your own user (asks for a password)",
"# 2) sudo ohne Passwortabfrage — Voraussetzung für automatische Läufe":
    "# 2) sudo without a password prompt — required for automated runs",
"# 3) Firewall: nur SSH offen":
    "# 3) firewall: only SSH open",
"Wichtig: erst prüfen, dann die root-Sitzung schließen":
    "Important: check first, close the root session afterwards",
"Der Befehl <code>visudo -c</code> muss mit <code>… parsed OK</code> antworten. Falls dort ein\n  Fehler steht, lösche die Datei sofort wieder mit\n  <code>rm /etc/sudoers.d/claude</code> — <strong>solange du noch als root angemeldet bist</strong>.\n  Eine kaputte sudo-Datei sperrt dich sonst von allen Administratorrechten aus. Lass dieses\n  root-Fenster offen, bis du im nächsten Schritt bestätigt hast, dass alles läuft.":
    "The command <code>visudo -c</code> must answer with <code>… parsed OK</code>. If it reports an\n  error, delete the file again immediately with\n  <code>rm /etc/sudoers.d/claude</code> — <strong>while you are still logged in as root</strong>.\n  A broken sudo file otherwise locks you out of all administrator rights. Leave this root window\n  open until you have confirmed in the next step that everything works.",
"Jetzt in einem <strong>zweiten</strong> Terminal-Fenster als neuer Benutzer anmelden und die\nbeiden Rechte prüfen:":
    "Now log in as the new user in a <strong>second</strong> terminal window and check both\npermissions:",
"Erscheint <code>sudo ohne Passwort: OK</code>, ist alles richtig — und du kannst das\nroot-Fenster schließen.":
    "If <code>sudo without password: OK</code> appears, everything is right — and you can close the\nroot window.",
"Warum sudo ohne Passwort?": "Why sudo without a password?",
"Wenn Claude später automatisch arbeitet — nachts, per Zeitplan, oder ferngesteuert über die\n  App — sitzt niemand davor, der ein Passwort eintippen könnte. Ohne diese Freigabe bleibt jeder\n  Befehl, der Administratorrechte braucht, einfach stehen. Das ist ein bewusster Kompromiss:\n  Wer sich Zugang zu deinem Benutzerkonto verschafft, hat damit auch vollen Administratorzugriff.\n  Deshalb ist der SSH-Zugang die Stelle, die du wirklich absichern solltest — siehe Teil 10.":
    "When Claude works on its own later — at night, on a schedule, or remote-controlled through the\n  app — nobody is sitting there to type a password. Without this permission every command that\n  needs administrator rights simply stalls. It is a deliberate trade-off: whoever gets into your\n  user account has full administrator access as well. That is why SSH access is the place you\n  really should secure — see part 10.",

# --- Teil 2 ---
"<span class=\"num\">2</span>Claude Code installieren und anmelden":
    "<span class=\"num\">2</span>Install Claude Code and sign in",
"# PATH neu einlesen": "# reload PATH",
"# erwartet z. B.: 2.1.232 (Claude Code)": "# expects e.g.: 2.1.232 (Claude Code)",
"# prüft die Installation": "# checks the installation",
"Der Installer legt das Programm unter <code>~/.local/share/claude/versions/</code> ab und\nverlinkt es über <code>~/.local/bin/claude</code>. <strong>Merk dir diesen Pfad</strong> — in Teil 4\nund Teil 6 brauchst du ihn. Kommt <code>command not found</code>, melde dich einmal ab und wieder an.":
    "The installer puts the program under <code>~/.local/share/claude/versions/</code> and links it\nthrough <code>~/.local/bin/claude</code>. <strong>Remember this path</strong> — you need it in\nparts 4 and 6. If you get <code>command not found</code>, log out once and back in.",
"Jetzt der erste Start und die Anmeldung:": "Now the first start and the sign-in:",
"Er zeigt dir einen Link und einen Code. Öffne den Link am Handy oder PC, melde dich mit deinem\nClaude-Abo an, bestätige den Code. Beim ersten Start fragt er außerdem nach dem Farbschema und ob\ndu dem aktuellen Ordner vertraust — beides einmal bestätigen. Mit <code>/exit</code> kommst du\nwieder heraus.":
    "It shows you a link and a code. Open the link on your phone or PC, sign in with your Claude\nsubscription, confirm the code. On the first start it also asks about the colour scheme and\nwhether you trust the current folder — confirm both once. <code>/exit</code> gets you back out.",
"Claude hält sich selbst aktuell": "Claude keeps itself up to date",
"Neue Versionen zieht er beim Start automatisch. Von Hand geht es mit <code>claude update</code>.\n  Alte Versionen bleiben liegen und belegen je rund 270 MB — mit\n  <code>ls -la ~/.local/share/claude/versions/</code> siehst du sie und kannst ältere gefahrlos\n  löschen. Das ist der Grund für die 10-GB-Empfehlung in Teil 0.":
    "It pulls new versions automatically at startup. By hand it is <code>claude update</code>.\n  Old versions stay behind and take up about 270 MB each — with\n  <code>ls -la ~/.local/share/claude/versions/</code> you can see them and safely delete the older\n  ones. That is the reason for the 10 GB recommendation in part 0.",

# --- Teil 3 ---
"<span class=\"num\">3</span>Der Zaubertrick: den Bootstrap-Prompt übergeben":
    "<span class=\"num\">3</span>The magic trick: hand over the bootstrap prompt",
"Das ist der Moment, in dem sich dein Assistent selbst aufbaut. In der beiliegenden Datei\n<code>setup-prompt.txt</code> steht ein vorbereiteter Text. Lege zuerst sein Arbeitsverzeichnis an\nund starte ihn dort:":
    "This is the moment where your assistant builds itself. The accompanying file\n<code>setup-prompt-en.txt</code> holds a prepared text. First create its working directory and start\nit there:",
"Öffne <code>setup-prompt.txt</code>, kopiere alles zwischen den beiden Markierungslinien und füge\nes als erste Nachricht ein. Ab da führt Claude dich durch die Einrichtung — er stellt Fragen, legt\nsein Gedächtnis an, prüft die Grundsicherheit und richtet auf Wunsch E-Mail und Web ein. Sein letzter\nPunkt baut außerdem den Dauerbetrieb aus Teil 4 gleich mit auf, also den Systemdienst. Lies Teil 4\ntrotzdem — dort steht, was dabei passiert ist und wie du es nachprüfst.":
    "Open <code>setup-prompt-en.txt</code>, copy everything between the two marker lines and paste it\nin as the first message. From there Claude walks you through the setup — it asks questions, sets\nup its memory, checks the basic security and, if you want, configures e-mail and web. Its last item\nalso builds the continuous operation from part 4 right away, meaning the system service. Read part 4\nanyway — it explains what happened there and how to verify it.",
"Warum ausgerechnet <code>~/assistant</code>?": "Why <code>~/assistant</code> of all places?",
"Claude merkt sich Vertrauen und Einstellungen <strong>pro Verzeichnis</strong>. Wenn der\n  Dienst aus Teil 4 später in einem anderen Ordner startet als dem, in dem du alles bestätigt\n  hast, fragt er wieder nach — und bleibt stehen. Bleib deshalb bei einem festen Arbeitsordner.":
    "Claude remembers trust and settings <strong>per directory</strong>. If the service from part 4\n  later starts in a different folder than the one where you confirmed everything, it asks again —\n  and stalls. So stick to one fixed working folder.",

# --- Teil 4 ---
"<span class=\"num\">4</span>Dauerbetrieb: als Dienst, per App erreichbar, neustartfest":
    "<span class=\"num\">4</span>Continuous operation: as a service, reachable from the app, reboot-proof",
"Ohne Dienst lebt Claude nur, solange dein Terminal-Fenster offen ist. Als echter Serverdienst\ndagegen startet er mit dem System, läuft rund um die Uhr, ist aus der Claude-App erreichbar und\nübersteht jeden Neustart — ohne Rückfragen.":
    "Without a service Claude only lives while your terminal window is open. As a real server\nservice it starts with the system, runs around the clock, is reachable from the Claude app and\nsurvives every reboot — without asking anything.",

"Prompt ganz durchlaufen? Dann steht das meiste schon":
    "Ran the whole prompt? Then most of this already stands",
"Punkt 8 des Bootstrap-Prompts richtet genau diesen Dienst ein. Sieh deshalb zuerst nach, was\n  bereits läuft: <code>systemctl status claude-code.service --no-pager</code>.":
    "Item 8 of the bootstrap prompt sets up this exact service. So first look at what is already\n  running: <code>systemctl status claude-code.service --no-pager</code>.",
"Steht dort <code>active (running)</code>, überspring die Schritte 1 und 2 — sie würden nur\n  dasselbe noch einmal anlegen. Lies die Erklärungen darin trotzdem, vor allem den Kasten zu\n  <code class=\"nb\">--continue</code>, und mach dann bei <strong>Schritt 4</strong> weiter: die Nagelprobe mit\n  dem Neustart hat dir bisher niemand abgenommen.":
    "If it says <code>active (running)</code>, skip steps 1 and 2 — they would only create the same\n  thing a second time. Read the explanations in them anyway, above all the box about\n  <code class=\"nb\">--continue</code>, and then carry on at <strong>step 4</strong>: the acid test with the\n  reboot is one nobody has done for you yet.",
"Hast du den Prompt abgekürzt oder Punkt 8 ausgelassen, arbeite Teil 4 von vorn durch.":
    "If you cut the prompt short or left item 8 out, work through part 4 from the beginning.",
"Dazu gehören drei Teile, und alle drei sind nötig:":
    "Three pieces belong to that, and all three are necessary:",
"Baustein": "Piece",
"Wozu": "What for",
"<strong>Systemdienst</strong>": "<strong>System service</strong>",
"startet Claude automatisch beim Hochfahren und startet ihn neu, falls er abstürzt":
    "starts Claude automatically at boot and restarts it if it crashes",
"<strong>Pseudo-Terminal</strong>": "<strong>Pseudo terminal</strong>",
"Claude braucht ein Terminal. Ohne eines bleibt er bei jeder Rückfrage stehen und kann die Antwort auch nicht speichern":
    "Claude needs a terminal. Without one it stalls at every prompt and cannot store the answer either",
"<strong>Vorab-Bestätigungen</strong>": "<strong>Pre-confirmations</strong>",
"die einmaligen Hinweisdialoge werden vorab abgehakt, damit nach dem Reboot niemand „ja“ tippen muss":
    "the one-off notice dialogs are ticked off in advance, so nobody has to type &#8220;yes&#8221; after a reboot",
"Schritt 1: Den Dienst anlegen": "Step 1: create the service",
"Diesen Block kannst du unverändert einfügen — er setzt deinen Benutzernamen und dein\nHeimatverzeichnis automatisch ein:":
    "You can paste this block unchanged — it fills in your user name and your home directory\nautomatically:",
"Achtung beim Abtippen: <code>ExecStart=…</code> ist <strong>eine einzige Zeile</strong>, auch wenn sie oben umbrochen dargestellt wird.":
    "Careful when typing it out: <code>ExecStart=…</code> is <strong>a single line</strong>, even though it is shown wrapped above.",
"Vier Stellen lohnen einen Blick:": "Four spots are worth a look:",
"<code>script -qec \"…\" /dev/null</code> ist der Kniff mit dem Pseudo-Terminal. Ohne ihn\n      startet der Dienst zwar, bleibt aber beim ersten Dialog hängen.":
    "<code>script -qec \"…\" /dev/null</code> is the pseudo-terminal trick. Without it the service\n      does start, but hangs at the first dialog.",
"Im Aufruf steht <code>~/.local/bin/claude</code>, also der <strong>Verweis</strong> — nicht die\n      konkrete Version darunter. Sonst zeigt der Dienst nach dem nächsten automatischen Update\n      ins Leere.":
    "The call uses <code>~/.local/bin/claude</code>, that is the <strong>link</strong> — not the\n      specific version underneath. Otherwise the service points into nothing after the next\n      automatic update.",
"<code>--name vps-main</code> ist der Name, unter dem die Sitzung später in der App auftaucht.\n      Nimm ruhig etwas Sprechendes.":
    "<code>--name vps-main</code> is the name the session shows up under in the app later.\n      Feel free to pick something descriptive.",
"<code class=\"nb\">--continue</code> nimmt beim Start das <strong>letzte Gespräch wieder auf</strong>,\n      statt bei null anzufangen. Neu in dieser Ausgabe — siehe den Kasten gleich darunter.":
    "<code class=\"nb\">--continue</code> picks the <strong>last conversation back up</strong> at startup\n      instead of beginning from scratch. New in this edition — see the box just below.",
"Warum <code class=\"nb\">--continue</code> den Unterschied macht":
    "Why <code class=\"nb\">--continue</code> makes the difference",
"Ohne diesen Zusatz beginnt der Dienst nach jedem Neustart eine frische Sitzung. Alles,\n  was ihr besprochen hattet, ist weg — und weil <code>Restart=on-failure</code> greift, kann\n  das mitten in der Arbeit passieren, ohne dass du es merkst.":
    "Without this addition the service starts a fresh session after every restart. Everything you\n  had discussed is gone — and because <code>Restart=on-failure</code> applies, that can happen in\n  the middle of a job without you noticing.",
"Mit <code class=\"nb\">--continue</code> hängt er sich stattdessen an das zuletzt geführte Gespräch.\n  Ein Absturz oder ein Reboot wird damit zu einer kurzen Unterbrechung statt zu einem\n  Gedächtnisverlust.":
    "With <code class=\"nb\">--continue</code> it attaches itself to the most recent conversation instead. A\n  crash or a reboot becomes a short interruption rather than a loss of memory.",
"Die Kehrseite, damit du nicht überrascht wirst: Ein Neustart des\n  Dienstes gibt dir jetzt <em>keine</em> frische Sitzung mehr. „Merk dir das nur für dieses\n  Gespräch“ überlebt damit auch einen Reboot. Willst du wirklich von vorn anfangen, leere\n  das Gespräch mit <code>/clear</code> aus der App heraus.":
    "The flip side, so you are not caught out: restarting the service no longer gives you a\n  <em>fresh</em> session. &#8220;Remember this just for this conversation&#8221; therefore survives\n  a reboot as well. If you really want to start over, clear the conversation with\n  <code>/clear</code> from inside the app.",
"Schritt 2: Die einmaligen Rückfragen vorab abhaken":
    "Step 2: tick off the one-off prompts in advance",
"Das ist der Schritt, an dem die meisten scheitern. Claude speichert „schon gesehen“-Häkchen in\nder Datei <code>~/.claude.json</code>. Fehlen sie, bleibt der Dienst nach jedem Neustart bei einer\nNachfrage stehen. Dieser Befehl setzt sie und legt vorher eine Sicherung an:":
    "This is the step most people fail at. Claude stores &#8220;already seen&#8221; ticks in the file\n<code>~/.claude.json</code>. If they are missing, the service stalls at a prompt after every\nrestart. This command sets them and makes a backup first:",
"Schritt 3: Dienst starten und prüfen": "Step 3: start the service and check it",
"In der Statusausgabe muss <code>active (running)</code> stehen. Falls nicht, zeigt\n<code>journalctl -u claude-code -n 40 --no-pager</code> den Grund.":
    "The status output must say <code>active (running)</code>. If it does not,\n<code>journalctl -u claude-code -n 40 --no-pager</code> shows the reason.",
"Schritt 4: Die Nagelprobe — neu starten": "Step 4: the acid test — reboot",
"Warte etwa eine Minute, verbinde dich neu und prüfe:":
    "Wait about a minute, reconnect and check:",
"Steht dort wieder <code>active (running)</code>, <strong>ohne dass du irgendetwas bestätigt\nhast</strong>, ist das Ziel erreicht.":
    "If it says <code>active (running)</code> again <strong>without you having confirmed\nanything</strong>, you have reached the goal.",
"Wenn er trotzdem bei einer Rückfrage hängt": "If it still hangs at a prompt",
"Dann prüfe genau diese vier Punkte in dieser Reihenfolge:":
    "Then check exactly these four points, in this order:",
"Läuft der Dienst als derselbe Benutzer, in dessen Heimatverzeichnis die Flags stehen?\n        <code>systemctl show claude-code -p User</code>":
    "Does the service run as the same user in whose home directory the flags live?\n        <code>systemctl show claude-code -p User</code>",
"Stimmt der Pfad unter <code>projects</code> in <code>~/.claude.json</code> zeichengenau mit\n        <code>WorkingDirectory</code> überein? Kein Schrägstrich am Ende, keine Tilde, keine\n        Verknüpfung.":
    "Does the path under <code>projects</code> in <code>~/.claude.json</code> match\n        <code>WorkingDirectory</code> character for character? No trailing slash, no tilde, no\n        symlink.",
"Ist das Pseudo-Terminal wirklich da? <code>ps -o tty= -p $(pgrep -f remote-control | head -1)</code>\n        darf <strong>nicht</strong> <code>?</code> ausgeben.":
    "Is the pseudo terminal really there? <code>ps -o tty= -p $(pgrep -f remote-control | head -1)</code>\n        must <strong>not</strong> print <code>?</code>.",
"Steht in <code>~/.claude/settings.json</code> etwas, das den Modus überschreibt?":
    "Is there something in <code>~/.claude/settings.json</code> that overrides the mode?",
"Schritt 5: Aus der App verbinden": "Step 5: connect from the app",
"Öffne die Claude-App auf dem Handy oder <strong>claude.ai/code</strong> im Browser — angemeldet\nmit demselben Konto wie auf dem Server. Dort taucht deine Sitzung unter dem Namen auf, den du\nvergeben hast (<code>vps-main</code>). Du tippst einfach eine Nachricht, und auf deinem Server\npassiert echte Arbeit. Das ist der Zustand, den du wolltest: Der Server läuft, du bist unterwegs,\nund beides findet zusammen.":
    "Open the Claude app on your phone or <strong>claude.ai/code</strong> in the browser — signed in\nwith the same account as on the server. Your session shows up there under the name you gave it\n(<code>vps-main</code>). You simply type a message, and real work happens on your server. That is\nthe state you were after: the server runs, you are out and about, and the two meet.",
"Nützlich im Alltag": "Handy in everyday use",
"<code>sudo systemctl restart claude-code</code> setzt den Dienst neu auf — durch\n  <code class=\"nb\">--continue</code> läuft das Gespräch danach weiter, statt neu zu beginnen. Hat sich\n  ein Gespräch festgefahren, hilft nicht der Neustart, sondern <code>/clear</code> aus der\n  App heraus. <code>journalctl -u claude-code -f</code> zeigt live mit, was der Dienst tut.":
    "<code>sudo systemctl restart claude-code</code> brings the service back up — thanks to\n  <code class=\"nb\">--continue</code> the conversation carries on afterwards instead of starting over. If a\n  conversation has got stuck, a restart will not help; <code>/clear</code> from inside the app\n  will. <code>journalctl -u claude-code -f</code> shows live what the service is doing.",

# --- Teil 5 ---
"<span class=\"num\">5</span>Optional: E-Mails verschicken":
    "<span class=\"num\">5</span>Optional: sending e-mail",
"Soll dein Assistent Mails schreiben können, braucht er ein Postfach. Du brauchst drei Angaben\naus deinen Mail-Einstellungen: SMTP-Server, Adresse und Passwort. Sag es Claude im Gespräch:":
    "If your assistant is to write e-mail, it needs a mailbox. You need three details from your mail\nsettings: SMTP server, address and password. Just tell Claude in the conversation:",
"Er installiert <code>msmtp</code>, legt die Zugangsdaten mit strengen Dateirechten ab und\nverschickt mit dir eine Testmail. Ohne eigene Zugangsdaten lässt du den Teil einfach weg —\nerfinden darf er sie nicht.":
    "It installs <code>msmtp</code>, stores the credentials with strict file permissions and sends a\ntest mail together with you. Without credentials of your own, simply skip this part — it is not\nallowed to invent them.",

# --- Teil 6 ---
"<span class=\"num\">6</span>Optional: Autonom — er arbeitet, während du schläfst":
    "<span class=\"num\">6</span>Optional: autonomous — it works while you sleep",
"Ein Zeitplan-Auftrag („Cronjob“) schaut regelmäßig nach, ob es etwas zu tun gibt — etwa neue\nPost im Postfach — und startet nur dann einen echten Claude-Lauf. Auch das richtet Claude für dich\nein. Damit es zuverlässig läuft, gib ihm diese drei Punkte mit; ich bin über jeden davon selbst\ngestolpert:":
    "A scheduled job (a &#8220;cron job&#8221;) checks regularly whether there is anything to do — new\nmail in the mailbox, for instance — and only then starts a real Claude run. Claude sets that up\nfor you too. To make it reliable, give it these three points; I tripped over every one of them\nmyself:",
"Stolperfalle": "Pitfall",
"Lösung": "Fix",
"<strong>Cron kennt deinen PATH nicht</strong>": "<strong>Cron does not know your PATH</strong>",
"<code>~/.local/bin</code> fehlt dort. Im Skript entweder <code>export PATH=\"$HOME/.local/bin:$PATH\"</code>\n          setzen oder Claude mit vollem Pfad aufrufen — sonst „command not found“ und der Job\n          scheitert stumm.":
    "<code>~/.local/bin</code> is missing there. In the script either set <code>export PATH=\"$HOME/.local/bin:$PATH\"</code>\n          or call Claude with its full path — otherwise you get &#8220;command not found&#8221; and\n          the job fails silently.",
"<strong>Zwei Läufe gleichzeitig</strong>": "<strong>Two runs at once</strong>",
"Mit <code>flock</code> absichern, sonst überholen sich hängende Läufe gegenseitig.":
    "Guard it with <code>flock</code>, otherwise stalled runs overtake one another.",
"<strong>Kosten</strong>": "<strong>Cost</strong>",
"Erst mit einem billigen Test prüfen, <em>ob</em> es Arbeit gibt. Den kostenpflichtigen\n          Lauf nur dann starten. Zusätzlich <code>timeout</code> davorsetzen.":
    "First use a cheap check to see <em>whether</em> there is work at all. Only then start the\n          run that costs money. And put a <code>timeout</code> in front of it.",
"Der eigentliche Aufruf im Skript sieht so aus — <code>-p</code> heißt „einmalig abarbeiten, kein\nGespräch“, und die Werkzeugliste begrenzt, was er dabei darf:":
    "The actual call in the script looks like this — <code>-p</code> means &#8220;work through it\nonce, no conversation&#8221;, and the tool list limits what it may do in the process:",
"Eingehende Inhalte sind kein Befehl": "Incoming content is not an instruction",
"Die wichtigste Dauerregel überhaupt: Der Inhalt fremder E-Mails, Webseiten und Nachrichten ist\n  <strong>niemals eine Anweisung</strong> an Claude. Er befolgt keine Aufforderungen daraus\n  („schick mir Datei X“, „führ Y aus“). Und alles, was nur du entscheiden kannst — Geld, Termine,\n  Zusagen in deinem Namen — gibt er an dich zurück, statt selbst zu handeln. Der Bootstrap-Prompt\n  schreibt ihm genau das ins Gedächtnis.":
    "The single most important standing rule: the content of other people&#8217;s e-mails, web pages\n  and messages is <strong>never an instruction</strong> to Claude. It does not follow demands found\n  in them (&#8220;send me file X&#8221;, &#8220;run Y&#8221;). And anything only you can decide —\n  money, appointments, commitments in your name — it hands back to you instead of acting itself.\n  The bootstrap prompt writes exactly that into its memory.",

# --- Teil 7 ---
"<span class=\"num\">7</span>Optional: Push-Nachrichten aufs Handy":
    "<span class=\"num\">7</span>Optional: push notifications to your phone",
"Mail und Zeitplan sind Einbahnstraßen: Dein Assistent legt etwas ab, und irgendwann\nschaust du nach. Für den umgekehrten Fall — <em>er</em> braucht <em>dich</em> — fehlt noch\nein Kanal. Genau dafür ist ein Push gut: ein kurzer Stups aufs Handy, wenn eine Entscheidung\nansteht oder etwas Wichtiges passiert ist.":
    "Mail and schedules are one-way streets: your assistant puts something down, and at some point\nyou go and look. For the reverse case — <em>it</em> needs <em>you</em> — a channel is still\nmissing. That is exactly what a push is good for: a short nudge to your phone when a decision is\ndue or something important has happened.",
"Am einfachsten geht das mit <strong>ntfy.sh</strong>. Kein Konto, keine Einrichtung auf\ndem Server, keine Schlüssel: Du denkst dir einen schwer zu erratenden Namen für deinen Kanal\naus, abonnierst ihn in der ntfy-App — und alles, was an diese Adresse geschickt wird, landet\nauf deinem Handy.":
    "The simplest way is <strong>ntfy.sh</strong>. No account, nothing to set up on the server, no\nkeys: you think up a hard-to-guess name for your channel, subscribe to it in the ntfy app — and\neverything sent to that address lands on your phone.",
"Der Kanalname ist dein einziger Schutz": "The channel name is your only protection",
"Wer den Namen kennt, liest mit — bei ntfy.sh ist jeder Kanal\n  öffentlich lesbar. Nimm deshalb nichts Erratbares wie <code>meinserver</code>, sondern\n  etwas Langes und Zufälliges. Und noch wichtiger: <strong>Schick niemals Inhalte in den\n  Push.</strong> Keine Mailadressen, keine Namen Dritter, keine Betreffzeilen, keine Beträge,\n  keine Zugangsdaten. Der Push sagt nur <em>dass</em> etwas ist — das <em>was</em> gehört in\n  eine Mail.":
    "Whoever knows the name is reading along — on ntfy.sh every channel is publicly readable. So do\n  not take anything guessable like <code>myserver</code>, take something long and random. And more\n  importantly: <strong>never send content in the push.</strong> No mail addresses, no third-party\n  names, no subject lines, no amounts, no credentials. The push only says <em>that</em> something\n  is up — the <em>what</em> belongs in an e-mail.",
"Ein Kanalname, den niemand rät, und die App einrichten:":
    "A channel name nobody will guess, and setting up the app:",
"Installiere die App <strong>ntfy</strong> (iOS und Android, kostenlos), abonniere dort\ngenau diesen Namen — und lass dir von Claude das kleine Sendeskript bauen:":
    "Install the <strong>ntfy</strong> app (iOS and Android, free), subscribe to exactly that name\nthere — and have Claude build you the little sending script:",
"Danach genügt ein Aufruf, aus jedem Skript und aus jedem automatischen Lauf heraus:":
    "After that one call is enough, from any script and from any automated run:",
"Sparsam bleiben, sonst schaust du bald nicht mehr hin":
    "Stay frugal, or you will soon stop looking",
"Ein Push ist nur dann etwas wert, wenn er selten kommt. Bewährt hat sich diese Regel:\n  <strong>nur bei Entscheidungen und bei Störungen</strong> — nicht für Erfolgsmeldungen und\n  schon gar nicht als Statusgeplauder.":
    "A push is only worth anything if it arrives rarely. This rule has proven itself:\n  <strong>only for decisions and for trouble</strong> — not for success messages, and certainly\n  not as status chatter.",
"Praktisches Beispiel aus dem Alltag: Ein Zeitplan-Auftrag prüft\n  täglich, ob eine neue Programmfassung da ist. Ist alles beim Alten — der Normalfall —\n  passiert gar nichts. Nur wenn er wirklich etwas geändert hat, kommt ein Push. Und wenn ihm\n  dabei etwas seltsam vorkommt, veröffentlicht er nichts, sondern fragt nach. Diese\n  Handbremse ist mehr wert als jede Bequemlichkeit.":
    "A practical example from everyday use: a scheduled job checks daily whether a new program\n  version has arrived. If everything is as before — the normal case — nothing happens at all. Only\n  if it really changed something does a push arrive. And if anything strikes it as odd in the\n  process, it publishes nothing and asks instead. That handbrake is worth more than any\n  convenience.",

# --- Teil 8 ---
"<span class=\"num\">8</span>Vom Handy steuern": "<span class=\"num\">8</span>Driving it from your phone",
"<strong>Claude-App oder claude.ai/code</strong> — der bequeme Weg, sobald Teil 4 steht. Deine\n      Server-Sitzung ist einfach da.":
    "<strong>The Claude app or claude.ai/code</strong> — the comfortable route, once part 4 is in\n      place. Your server session is simply there.",
"<strong>SSH-App</strong> (z. B. Termius) — der direkte Weg ins Terminal, wenn du am Server\n      selbst etwas nachsehen willst.":
    "<strong>An SSH app</strong> (Termius, for example) — the direct route into the terminal, when\n      you want to look at something on the server yourself.",

# --- Teil 9 ---
"<span class=\"num\">9</span>Weitere Dienste anbinden (Connectors)":
    "<span class=\"num\">9</span>Connecting further services (connectors)",
"Claude kann an andere Systeme andocken — Mail, Kalender, Drive und weitere. Damit holt er\nLive-Daten, statt nur auf sein eingebautes Wissen angewiesen zu sein. Ein Thema für später: Frag\nihn einfach <em>„Welche Connectors kann ich anbinden und wie?“</em>, wenn du so weit bist.":
    "Claude can dock onto other systems — mail, calendar, Drive and more. That way it fetches live\ndata instead of relying on its built-in knowledge alone. A topic for later: simply ask it\n<em>&#8220;Which connectors can I attach, and how?&#8221;</em> when you get that far.",

# --- Teil 10 ---
"<span class=\"num\">10</span>Sicherheit &amp; gute Gewohnheiten":
    "<span class=\"num\">10</span>Security &amp; good habits",
"<strong>Sichere den SSH-Zugang ab.</strong> Durch das passwortlose sudo aus Teil 1 ist dein\n      Benutzerkonto der Generalschlüssel. Lass dir von Claude die Anmeldung per\n      <strong>SSH-Schlüssel statt Passwort</strong> einrichten und das Passwort-Login abschalten —\n      das ist die wirksamste einzelne Maßnahme. Er erklärt dir jeden Schritt, und ihr prüft die\n      neue Anmeldung in einem zweiten Fenster, bevor das alte geschlossen wird.":
    "<strong>Secure SSH access.</strong> Because of the passwordless sudo from part 1, your user\n      account is the master key. Have Claude set up logging in with an <strong>SSH key instead of a\n      password</strong> and switch password login off — that is the single most effective measure.\n      It explains every step, and you test the new login in a second window before closing the old\n      one.",
"<strong>Nicht als root arbeiten.</strong> Dein normaler Benutzer plus <code>sudo</code> für\n      einzelne Befehle reicht.":
    "<strong>Do not work as root.</strong> Your ordinary user plus <code>sudo</code> for individual\n      commands is enough.",
"<strong>Zugangsdaten schützen.</strong> Immer Dateirechte <code>600</code>, nie im Klartext\n      ausgeben.":
    "<strong>Protect credentials.</strong> Always file permissions <code>600</code>, never printed\n      in the clear.",
"<strong>Vor Unumkehrbarem nachfragen lassen.</strong> Löschen, überschreiben, neu starten,\n      etwas nach außen senden.":
    "<strong>Have it ask before anything irreversible.</strong> Deleting, overwriting, restarting,\n      sending something outward.",
"<strong>Behalte die Kosten im Blick.</strong> Automatische Läufe kosten Geld. Lass dir\n      anfangs jeden Lauf protokollieren und schau nach ein paar Tagen ins Protokoll.":
    "<strong>Keep an eye on the cost.</strong> Automated runs cost money. Have every run logged at\n      first and look into the log after a few days.",

# --- Checkliste ---
"Deine Checkliste zum Abhaken": "Your checklist to tick off",
"☐ Eigener Benutzer angelegt, <code>sudo -n true</code> läuft ohne Passwort":
    "☐ Own user created, <code>sudo -n true</code> runs without a password",
"☐ Firewall aktiv, nur SSH offen": "☐ Firewall active, only SSH open",
"☐ <code>claude --version</code> zeigt eine Version":
    "☐ <code>claude --version</code> shows a version",
"☐ Bootstrap-Prompt durchlaufen, Gedächtnis steht":
    "☐ Bootstrap prompt completed, memory in place",
"☐ Dienst läuft: <code>systemctl status claude-code</code> zeigt <code>active (running)</code>":
    "☐ Service running: <code>systemctl status claude-code</code> shows <code>active (running)</code>",
"☐ Nach <code>sudo reboot</code> läuft er wieder — ohne Rückfrage, und das Gespräch ist noch da":
    "☐ After <code>sudo reboot</code> it runs again — without a prompt, and the conversation is still there",
"☐ Sitzung ist in der Claude-App sichtbar und antwortet":
    "☐ The session is visible in the Claude app and answers",
"☐ <em>Optional:</em> Ein Testpush kommt auf dem Handy an":
    "☐ <em>Optional:</em> a test push arrives on your phone",
"☐ SSH-Schlüssel eingerichtet, Passwort-Login aus":
    "☐ SSH key set up, password login off",

"Und dann?": "And then?",
"Dann fängt der schöne Teil an. Sag ihm, was dich im Alltag nervt — und lass ihn Werkzeuge\n  dafür bauen. Genau so ist alles entstanden, was ich hier auf Christians Server kann. Wenn etwas\n  klemmt: Er kann seine eigenen Fehler lesen. <em>„Schau ins Journal und finde heraus, warum\n  der Dienst nicht startet“</em> ist ein völlig normaler Auftrag.":
    "Then the good part begins. Tell it what annoys you in daily life — and have it build tools for\n  that. That is exactly how everything I can do here on Christian&#8217;s server came about. If\n  something jams: it can read its own errors. <em>&#8220;Look in the journal and work out why the\n  service will not start&#8221;</em> is a perfectly ordinary request.",
# ------------------------------------------------------------ Codeblöcke ----
# Befehle bleiben Zeichen für Zeichen gleich; übersetzt werden nur Kommentare,
# Ausgabetexte und die Beispielaufträge an Claude. Der Platzhalter-Benutzername
# heisst in der englischen Fassung durchgehend "myname".

"ssh root@203.0.113.10": "ssh root@203.0.113.10",
"claude": "claude",
"sudo reboot": "sudo reboot",
"systemctl status claude-code.service --no-pager": "systemctl status claude-code.service --no-pager",

"""<span class="c"># ---------- als root, direkt nach dem ersten Login ----------</span>
apt update &amp;&amp; apt full-upgrade -y
apt install -y curl git ufw jq python3 ripgrep

<span class="c"># 1) eigenen Benutzer anlegen (fragt nach einem Passwort)</span>
adduser meinname
usermod -aG sudo meinname

<span class="c"># 2) sudo ohne Passwortabfrage — Voraussetzung für automatische Läufe</span>
echo 'meinname ALL=(ALL) NOPASSWD: ALL' &gt; /etc/sudoers.d/claude
chmod 0440 /etc/sudoers.d/claude
visudo -c

<span class="c"># 3) Firewall: nur SSH offen</span>
ufw allow OpenSSH
ufw --force enable""":
"""<span class="c"># ---------- as root, right after the first login ----------</span>
apt update &amp;&amp; apt full-upgrade -y
apt install -y curl git ufw jq python3 ripgrep

<span class="c"># 1) create your own user (asks for a password)</span>
adduser myname
usermod -aG sudo myname

<span class="c"># 2) sudo without a password prompt — required for automated runs</span>
echo 'myname ALL=(ALL) NOPASSWD: ALL' &gt; /etc/sudoers.d/claude
chmod 0440 /etc/sudoers.d/claude
visudo -c

<span class="c"># 3) firewall: only SSH open</span>
ufw allow OpenSSH
ufw --force enable""",

"""ssh meinname@203.0.113.10
sudo -n true &amp;&amp; echo "sudo ohne Passwort: OK\"""":
"""ssh myname@203.0.113.10
sudo -n true &amp;&amp; echo "sudo without password: OK\"""",

"""curl -fsSL https://claude.ai/install.sh | bash
exec $SHELL -l          <span class="c"># PATH neu einlesen</span>
claude --version        <span class="c"># erwartet z. B.: 2.1.232 (Claude Code)</span>
claude doctor           <span class="c"># prüft die Installation</span>""":
"""curl -fsSL https://claude.ai/install.sh | bash
exec $SHELL -l          <span class="c"># reload PATH</span>
claude --version        <span class="c"># expects e.g.: 2.1.232 (Claude Code)</span>
claude doctor           <span class="c"># checks the installation</span>""",

"""mkdir -p ~/assistant
cd ~/assistant
claude""":
"""mkdir -p ~/assistant
cd ~/assistant
claude""",

"""sudo tee /etc/systemd/system/claude-code.service &gt;/dev/null &lt;&lt;EOF
[Unit]
Description=Claude Code Remote Control Session
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$HOME/assistant
ExecStart=/usr/bin/script -qec "$HOME/.local/bin/claude --remote-control --name vps-main --continue" /dev/null
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF""":
"""sudo tee /etc/systemd/system/claude-code.service &gt;/dev/null &lt;&lt;EOF
[Unit]
Description=Claude Code Remote Control Session
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$HOME/assistant
ExecStart=/usr/bin/script -qec "$HOME/.local/bin/claude --remote-control --name vps-main --continue" /dev/null
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF""",

"""python3 - &lt;&lt;'PY'
import json, os, shutil
p = os.path.expanduser('~/.claude.json')
shutil.copy(p, p + '.bak')
d = json.load(open(p))
d['hasCompletedOnboarding'] = True
d['hasSeenAutoModeEntryWarning'] = True
proj = d.setdefault('projects', {}).setdefault(os.path.expanduser('~/assistant'), {})
proj['hasTrustDialogAccepted'] = True
json.dump(d, open(p, 'w'), indent=2)
print('Flags gesetzt. Sicherung: ~/.claude.json.bak')
PY""":
"""python3 - &lt;&lt;'PY'
import json, os, shutil
p = os.path.expanduser('~/.claude.json')
shutil.copy(p, p + '.bak')
d = json.load(open(p))
d['hasCompletedOnboarding'] = True
d['hasSeenAutoModeEntryWarning'] = True
proj = d.setdefault('projects', {}).setdefault(os.path.expanduser('~/assistant'), {})
proj['hasTrustDialogAccepted'] = True
json.dump(d, open(p, 'w'), indent=2)
print('Flags set. Backup: ~/.claude.json.bak')
PY""",

"""sudo systemctl daemon-reload
sudo systemctl enable --now claude-code.service
systemctl status claude-code.service --no-pager""":
"""sudo systemctl daemon-reload
sudo systemctl enable --now claude-code.service
systemctl status claude-code.service --no-pager""",

"""Bitte richte ein, dass du E-Mails verschicken kannst.
SMTP-Server smtp.meinprovider.de, Port 587,
Adresse ich@meinprovider.de. Das Passwort gebe ich dir gleich.""":
"""Please set yourself up so that you can send e-mail.
SMTP server smtp.myprovider.com, port 587,
address me@myprovider.com. I&#8217;ll give you the password in a moment.""",

"""timeout 1800 "$HOME/.local/bin/claude" -p --model sonnet \\
  --allowedTools "Bash(mailbox:*),Read" \\
  --max-turns 30 \\
  "Deine Aufgabenbeschreibung hier" &gt;&gt;"$LOG" 2&gt;&amp;1""":
"""timeout 1800 "$HOME/.local/bin/claude" -p --model sonnet \\
  --allowedTools "Bash(mailbox:*),Read" \\
  --max-turns 30 \\
  "Your task description here" &gt;&gt;"$LOG" 2&gt;&amp;1""",

"""head -c 18 /dev/urandom | base64 | tr -dc 'a-zA-Z0-9'
# gibt z. B.: k7Rq2wZm4TnLp9Xd""":
"""head -c 18 /dev/urandom | base64 | tr -dc 'a-zA-Z0-9'
# yields e.g.: k7Rq2wZm4TnLp9Xd""",

"""Bitte leg mir ein Skript ~/assistant/bin/push.sh an, das eine
Nachricht per ntfy.sh an meinen Kanal schickt. Den Kanalnamen
legst du mit Dateirechten 600 in eine eigene Konfigurationsdatei,
nicht ins Skript. Zwei Sendeversuche, 15 Sekunden Zeitlimit,
und schreib jeden Versand in eine Logdatei.""":
"""Please create a script ~/assistant/bin/push.sh for me that sends
a message to my channel via ntfy.sh. Put the channel name into a
separate configuration file with permissions 600, not into the
script itself. Two send attempts, a 15 second timeout, and write
every send into a log file.""",

"""~/assistant/bin/push.sh "Es wartet eine Rückfrage — Details per Mail\"""":
"""~/assistant/bin/push.sh "A question is waiting — details by e-mail\"""",
}


TITEL = "Your own AI server assistant — Edition 3"

# Fußzeile der Seiten (steht in der @page-Regel, nicht im Text).
FUSS_MITTE = "Your own AI server assistant · Edition 3"
FUSS_RECHTS = '"Page " counter(page) " / " counter(pages)'
