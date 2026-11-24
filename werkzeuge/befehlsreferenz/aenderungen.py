# -*- coding: utf-8 -*-
"""Der Kasten „Was sich seit der letzten Fassung geändert hat" — je Sprache.

Wird bei jeder neuen Programmfassung neu geschrieben (siehe bin/refcheck.sh).
BEIDE Sprachen beschreiben denselben Sachverhalt; wenn Du eine änderst, ändere
die andere mit. Reines HTML, wie es im Kasten steht (<p>…</p>).
"""

DE = """
<p>Gegenüber {vorg}: <b>ein neuer Befehl, <code>/claude-approvals</code>; sonst nichts Inhaltliches.</b></p>
<ul>
<li><code>/claude-approvals</code> ist neu: Skill für Claude-Approvals-Richtliniendateien (<code>.claude/approvals.yml</code>) und eigene Klassifizierer (<code>.claude/classifiers/</code>). Er ist vor dem Anlegen, Ändern, Aufräumen oder Erklären gedacht, auch vor oder nach dem Deinstallieren oder Aussetzen der Claude-GitHub-App; nicht für CODEOWNERS, Branch-Protection, GitHub Actions oder Claude Codes eigene Berechtigungen.</li>
<li><code>claude auth</code>: In der Hilfe der Unterbefehle steht <code>logout</code> jetzt mit <code>[options]</code>.</li>
</ul>
<p><code>claude --help</code> ist zeichengleich. Slash-Befehle: 136 statt 135 (einer neu, keiner weg, keine geänderte Beschreibung).</p>
"""

EN = """
<p>Compared with {vorg}: <b>one new command, <code>/claude-approvals</code>; nothing else of substance.</b></p>
<ul>
<li><code>/claude-approvals</code> is new: a skill for Claude Approvals policy files (<code>.claude/approvals.yml</code>) and custom classifiers (<code>.claude/classifiers/</code>). It is meant for use before creating, changing, cleaning up or explaining them, and before or after uninstalling or suspending the Claude GitHub App; not for CODEOWNERS, branch protection, GitHub Actions or Claude Code's own permission settings.</li>
<li><code>claude auth</code>: in the subcommand help, <code>logout</code> is now listed with <code>[options]</code>.</li>
</ul>
<p><code>claude --help</code> is character-for-character identical. Slash commands: 136 instead of 135 (one new, none removed, no description changed).</p>
"""
