import os
from pathlib import Path

def find_config():
    return Path('settings.txt').exists()

def test_finds_it(tmp_path, monkeypatch):
    (tmp_path / 'settings.txt').write_text('x', encoding='utf-8')
    monkeypatch.chdir(tmp_path)
    assert find_config() is True

def test_back_where_we_started():
    assert find_config() is False
