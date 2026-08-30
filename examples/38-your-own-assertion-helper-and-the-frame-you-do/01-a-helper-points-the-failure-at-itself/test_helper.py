def assert_valid(user):
    assert 'name' in user
    assert user.get('credit', 0) >= 0

def test_user():
    assert_valid({'name': 'Ada', 'credit': -5})
