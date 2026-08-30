def save(path, text):
    path.write_text(text, encoding='utf-8')
    return path

def test_writes(tmp_path):
    f = save(tmp_path / 'out.txt', 'hello')
    assert f.read_text(encoding='utf-8') == 'hello'

def test_starts_empty(tmp_path):
    assert list(tmp_path.iterdir()) == []
