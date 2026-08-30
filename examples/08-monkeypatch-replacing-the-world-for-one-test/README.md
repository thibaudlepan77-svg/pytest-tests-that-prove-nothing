# monkeypatch, replacing the world for one test

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `get`, `setenv`, `setattr`, `header`.

## A test that reads the real environment is not a test

`test_env.py`

```python
import os

def region():
    return os.environ.get('APP_REGION', 'unset')

def test_region(monkeypatch):
    monkeypatch.setenv('APP_REGION', 'eu-west-1')
    assert region() == 'eu-west-1'

def test_region_is_restored():
    assert region() == 'unset'
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

test_env.py::test_region PASSED                                          [ 50%]
test_env.py::test_region_is_restored PASSED                              [100%]

============================== 2 passed in 0.01s ==============================
```

## Patch where the name is looked up, not where it is defined

`clock.py`

```python
def now():
    return 'real time'
```

`report.py`

```python
from clock import now

def header():
    return 'generated at ' + now()
```

`test_patch.py`

```python
import report

def test_wrong_target(monkeypatch):
    monkeypatch.setattr('clock.now', lambda: 'frozen')
    assert report.header() == 'generated at frozen'

def test_right_target(monkeypatch):
    monkeypatch.setattr('report.now', lambda: 'frozen')
    assert report.header() == 'generated at frozen'
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

test_patch.py::test_wrong_target FAILED                                  [ 50%]
test_patch.py::test_right_target PASSED                                  [100%]

================================== FAILURES ===================================
______________________________ test_wrong_target ______________________________

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x000002AD35663490>

    def test_wrong_target(monkeypatch):
        monkeypatch.setattr('clock.now', lambda: 'frozen')
>       assert report.header() == 'generated at frozen'
E       AssertionError: assert 'generated at real time' == 'generated at frozen'
E         
E         - generated at frozen
E         + generated at real time

test_patch.py:5: AssertionError
=========================== short test summary info ===========================
FAILED test_patch.py::test_wrong_target - AssertionError: assert 'generated a...
========================= 1 failed, 1 passed in 0.01s =========================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
