# yield fixtures, and teardown that runs even when the test fails

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `fixture`.

## Everything after yield runs when the test is done

`test_yield.py`

```python
import pytest

@pytest.fixture
def connection():
    print('OPEN')
    yield {'open': True}
    print('CLOSE')

def test_uses_it(connection):
    print('TEST BODY')
    assert connection['open']
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

test_yield.py::test_uses_it OPEN
TEST BODY
PASSEDCLOSE


============================== 1 passed in 0.01s ==============================
```

## Teardown still runs after a failure

`test_yield.py`

```python
import pytest

@pytest.fixture
def connection():
    print('OPEN')
    yield {'open': True}
    print('CLOSE')

def test_fails(connection):
    print('TEST BODY')
    assert connection['open'] is False
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

test_yield.py::test_fails OPEN
TEST BODY
FAILEDCLOSE


================================== FAILURES ===================================
_________________________________ test_fails __________________________________

connection = {'open': True}

    def test_fails(connection):
        print('TEST BODY')
>       assert connection['open'] is False
E       assert True is False

test_yield.py:11: AssertionError
=========================== short test summary info ===========================
FAILED test_yield.py::test_fails - assert True is False
============================== 1 failed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
