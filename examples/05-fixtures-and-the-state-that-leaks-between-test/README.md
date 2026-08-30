# Fixtures, and the state that leaks between tests

3 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## A module level list is shared by every test

`test_leak.py`

```python
ITEMS = []

def test_one():
    ITEMS.append('a')
    assert len(ITEMS) == 1

def test_two():
    ITEMS.append('b')
    assert len(ITEMS) == 1
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

test_leak.py::test_one PASSED                                            [ 50%]
test_leak.py::test_two FAILED                                            [100%]

================================== FAILURES ===================================
__________________________________ test_two ___________________________________

    def test_two():
        ITEMS.append('b')
>       assert len(ITEMS) == 1
E       AssertionError: assert 2 == 1
E        +  where 2 = len(['a', 'b'])

test_leak.py:9: AssertionError
=========================== short test summary info ===========================
FAILED test_leak.py::test_two - AssertionError: assert 2 == 1
========================= 1 failed, 1 passed in 0.01s =========================
```

## A fixture gives each test its own copy

`test_leak.py`

```python
import pytest

@pytest.fixture
def items():
    return []

def test_one(items):
    items.append('a')
    assert len(items) == 1

def test_two(items):
    items.append('b')
    assert len(items) == 1
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

test_leak.py::test_one PASSED                                            [ 50%]
test_leak.py::test_two PASSED                                            [100%]

============================== 2 passed in 0.01s ==============================
```

## A default argument is created once, at import time

`test_default.py`

```python
def collect(value, bucket=[]):
    bucket.append(value)
    return bucket

def test_first():
    assert collect(1) == [1]

def test_second():
    assert collect(2) == [2]
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

test_default.py::test_first PASSED                                       [ 50%]
test_default.py::test_second FAILED                                      [100%]

================================== FAILURES ===================================
_________________________________ test_second _________________________________

    def test_second():
>       assert collect(2) == [2]
E       assert [1, 2] == [2]
E         
E         At index 0 diff: 1 != 2
E         Left contains one more item: 2
E         
E         Full diff:
E           [
E         +     1,
E               2,
E           ]

test_default.py:9: AssertionError
=========================== short test summary info ===========================
FAILED test_default.py::test_second - assert [1, 2] == [2]
========================= 1 failed, 1 passed in 0.01s =========================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
