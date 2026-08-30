def build():
    return {'id': 1, 'name': 'Ada', 'active': True, 'credit': 90}

def test_shape():
    assert build() == {'id': 1, 'name': 'Ada', 'active': True, 'credit': 100}
