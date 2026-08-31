# Pytest call fixture

_autouse, the fixture nobody asked for._

1 example. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `fixture`, `autouse`.

## An autouse fixture runs for every test in scope

`test_auto.py`

```python
import pytest

STATE = {'calls': 0}

@pytest.fixture(autouse=True)
def reset():
    STATE['calls'] = 0

def test_a():
    STATE['calls'] += 1
    assert STATE['calls'] == 1

def test_b():
    STATE['calls'] += 1
    assert STATE['calls'] == 1
```

```bash
pytest -v
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 2 items

test_auto.py::test_a PASSED                                              [ 50%]
test_auto.py::test_b PASSED                                              [100%]

============================== 2 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
