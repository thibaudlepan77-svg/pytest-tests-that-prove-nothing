import os

def region():
    return os.environ.get('APP_REGION', 'unset')

def test_region(monkeypatch):
    monkeypatch.setenv('APP_REGION', 'eu-west-1')
    assert region() == 'eu-west-1'

def test_region_is_restored():
    assert region() == 'unset'
