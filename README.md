# ShellSieve

Local shell-history session mapping and anomaly triage.

ShellSieve reads history as data. It never executes or replays history entries.

FEATURES
- Bash, Zsh and plain history parsing
- Approximate session grouping from timestamps
- Command-family classification
- Timestamp regression detection
- History-clearing pattern detection
- Download-to-shell indicators
- Destructive-command candidates
- Redaction of common credential-looking values
- JSON and Markdown reports
- No network, telemetry or command execution

INSTALL
1. git clone https://github.com/Tinytim695/shellsieve.git
2. cd shellsieve
3. chmod +x shellsieve
4. sudo install -m 0755 shellsieve /usr/local/bin/shellsieve

USAGE
shellsieve ~/.bash_history
shellsieve ~/.zsh_history --format zsh
shellsieve ~/.bash_history --json report.json
shellsieve ~/.bash_history --markdown report.md

SAFETY
History contents are never executed or modified. Reports redact common secret-looking values.

ShellSieve is a triage aid, not a definitive attribution or incident verdict.

License: MIT
