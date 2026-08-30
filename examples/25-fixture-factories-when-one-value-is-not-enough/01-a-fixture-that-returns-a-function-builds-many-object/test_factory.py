import pytest

@pytest.fixture
def make_user():
    created = []
    def _make(name, credit=0):
        u = {'name': name, 'credit': credit}
        created.append(u)
        return u
    yield _make
    print('created', len(created), 'users')

def test_two_users(make_user):
    a = make_user('Ada', 10)
    b = make_user('Bob')
    assert a['credit'] == 10
    assert b['credit'] == 0
