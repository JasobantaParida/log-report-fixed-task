from pathlib import Path
import json

def load():
    return json.loads(Path("/app/report.json").read_text())

def test_total_requests():
    data = load()
    assert data["total_requests"] == 6

def test_unique_ips():
    data = load()
    assert data["unique_ips"] == 3

def test_top_path():
    data = load()
    assert data["top_path"] == "/index.html"
