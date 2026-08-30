# Fixture scope, the argument that silently changes everything

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `fixture`, `scope`.

## scope=module runs the fixture once for the whole file

`test_scope.py`

```python
import pytest

@pytest.fixture(scope='module')
def counter():
    print('FIXTURE BODY RAN')
    return {'n': 0}

def test_a(counter):
    counter['n'] += 1
    assert counter['n'] == 1

def test_b(counter):
    counter['n'] += 1
    assert counter['n'] == 1
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

test_scope.py::test_a FIXTURE BODY RAN
PASSED
test_scope.py::test_b FAILED

================================== FAILURES ===================================
___________________________________ test_b ____________________________________

counter = {'n': 2}

    def test_b(counter):
        counter['n'] += 1
>       assert counter['n'] == 1
E       assert 2 == 1

test_scope.py:14: AssertionError
=========================== short test summary info ===========================
FAILED test_scope.py::test_b - assert 2 == 1
========================= 1 failed, 1 passed in 0.01s =========================
```

## The default scope is function, and it fixes it

`test_scope.py`

```python
import pytest

@pytest.fixture
def counter():
    print('FIXTURE BODY RAN')
    return {'n': 0}

def test_a(counter):
    counter['n'] += 1
    assert counter['n'] == 1

def test_b(counter):
    counter['n'] += 1
    assert counter['n'] == 1
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

test_scope.py::test_a FIXTURE BODY RAN
PASSED
test_scope.py::test_b FIXTURE BODY RAN
PASSED

============================== 2 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
