# Fixture factories, when one value is not enough

1 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## A fixture that returns a function builds many objects

`test_factory.py`

```python
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
```

```bash
pytest -v -s
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 1 item

test_factory.py::test_two_users PASSEDcreated 2 users


============================== 1 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
