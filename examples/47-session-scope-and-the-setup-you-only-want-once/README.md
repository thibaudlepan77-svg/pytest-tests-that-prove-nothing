# session scope, and the setup you only want once

1 example. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `fixture`, `scope`.

## A session fixture runs once for the whole run

`conftest.py`

```python
import pytest

@pytest.fixture(scope='session')
def heavy():
    print('EXPENSIVE SETUP')
    return {'rows': 1000}

@pytest.fixture
def rows(heavy):
    return dict(heavy)
```

`test_a.py`

```python
def test_one(rows):
    rows['rows'] += 1
    assert rows['rows'] == 1001
```

`test_b.py`

```python
def test_two(rows):
    rows['rows'] += 1
    assert rows['rows'] == 1001
```

```bash
pytest -v -s
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 2 items

test_a.py::test_one EXPENSIVE SETUP
PASSED
test_b.py::test_two PASSED

============================== 2 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
