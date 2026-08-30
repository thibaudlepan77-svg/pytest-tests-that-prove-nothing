# pytest.warns, and the warning you should turn into an error

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## A deprecation warning that nobody sees

`test_warn.py`

```python
import warnings

def old_api():
    warnings.warn('old_api is deprecated', DeprecationWarning)
    return 42

def test_still_works():
    assert old_api() == 42
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

test_warn.py::test_still_works PASSED                                    [100%]

============================== warnings summary ===============================
test_warn.py::test_still_works
  /test_warn.py:4: DeprecationWarning: old_api is deprecated
    warnings.warn('old_api is deprecated', DeprecationWarning)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 1 passed, 1 warning in 0.01s =========================
```

## pytest.warns asserts the warning is actually raised

`test_warn.py`

```python
import warnings
import pytest

def old_api():
    warnings.warn('old_api is deprecated', DeprecationWarning)
    return 42

def new_api():
    return 42

def test_warns():
    with pytest.warns(DeprecationWarning, match='deprecated'):
        old_api()

def test_new_does_not_warn():
    with pytest.warns(DeprecationWarning):
        new_api()
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

test_warn.py::test_warns PASSED                                          [ 50%]
test_warn.py::test_new_does_not_warn FAILED                              [100%]

================================== FAILURES ===================================
___________________________ test_new_does_not_warn ____________________________

    def test_new_does_not_warn():
>       with pytest.warns(DeprecationWarning):
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT WARN. No warnings of type (<class 'DeprecationWarning'>,) were emitted.
E        Emitted warnings: [].

test_warn.py:16: Failed
=========================== short test summary info ===========================
FAILED test_warn.py::test_new_does_not_warn - Failed: DID NOT WARN. No warnin...
========================= 1 failed, 1 passed in 0.01s =========================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
