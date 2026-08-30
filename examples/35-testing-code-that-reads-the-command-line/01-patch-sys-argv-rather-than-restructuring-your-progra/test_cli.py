import sys
import cli

def test_with_name(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['cli', 'Ada'])
    assert cli.main() == 'hello Ada'

def test_without_name(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['cli'])
    assert cli.main() == 'usage: cli NAME'
