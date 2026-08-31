# Pytest raises exception test

_Your own exception types, and testing the chain._

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `raises`.

## A bare except in the code hides the cause

`loader.py`

```python
class LoadError(Exception):
    pass

def load(raw):
    try:
        return int(raw)
    except ValueError:
        raise LoadError('bad row')
```

`test_loader.py`

```python
import pytest
from loader import load, LoadError

def test_raises_load_error():
    with pytest.raises(LoadError):
        load('abc')

def test_keeps_the_cause():
    with pytest.raises(LoadError) as info:
        load('abc')
    assert isinstance(info.value.__cause__, ValueError)
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

test_loader.py::test_raises_load_error PASSED                            [ 50%]
test_loader.py::test_keeps_the_cause FAILED                              [100%]

================================== FAILURES ===================================
____________________________ test_keeps_the_cause _____________________________

    def test_keeps_the_cause():
        with pytest.raises(LoadError) as info:
            load('abc')
>       assert isinstance(info.value.__cause__, ValueError)
E       AssertionError: assert False
E        +  where False = isinstance(None, ValueError)
E        +    where None = LoadError('bad row').__cause__
E        +      where LoadError('bad row') = <ExceptionInfo LoadError('bad row') tblen=2>.value

test_loader.py:11: AssertionError
=========================== short test summary info ===========================
FAILED test_loader.py::test_keeps_the_cause - AssertionError: assert False
========================= 1 failed, 1 passed in 0.01s =========================
```

## raise from keeps the original, and the test proves it

`loader.py`

```python
class LoadError(Exception):
    pass

def load(raw):
    try:
        return int(raw)
    except ValueError as e:
        raise LoadError('bad row') from e
```

`test_loader.py`

```python
import pytest
from loader import load, LoadError

def test_keeps_the_cause():
    with pytest.raises(LoadError) as info:
        load('abc')
    assert isinstance(info.value.__cause__, ValueError)
    assert 'abc' in str(info.value.__cause__)
```

```bash
pytest -v
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 1 item

test_loader.py::test_keeps_the_cause PASSED                              [100%]

============================== 1 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
