import report

def test_wrong_target(monkeypatch):
    monkeypatch.setattr('clock.now', lambda: 'frozen')
    assert report.header() == 'generated at frozen'

def test_right_target(monkeypatch):
    monkeypatch.setattr('report.now', lambda: 'frozen')
    assert report.header() == 'generated at frozen'
