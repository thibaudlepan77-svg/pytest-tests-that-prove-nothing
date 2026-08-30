# Time, the dependency you cannot mock by wishing

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `now`, `greeting`.

## A function that calls the clock is untestable as written

`billing.py`

```python
from datetime import datetime

def greeting():
    h = datetime.now().hour
    return 'good morning' if h < 12 else 'good afternoon'
```

`test_billing.py`

```python
import billing

def test_says_good_morning():
    assert billing.greeting() == 'good morning'

def test_says_good_afternoon():
    assert billing.greeting() == 'good afternoon'
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

test_billing.py::test_says_good_morning FAILED                           [ 50%]
test_billing.py::test_says_good_afternoon PASSED                         [100%]

================================== FAILURES ===================================
___________________________ test_says_good_morning ____________________________

    def test_says_good_morning():
>       assert billing.greeting() == 'good morning'
E       AssertionError: assert 'good afternoon' == 'good morning'
E         
E         - good morning
E         + good afternoon

test_billing.py:4: AssertionError
=========================== short test summary info ===========================
FAILED test_billing.py::test_says_good_morning - AssertionError: assert 'good...
========================= 1 failed, 1 passed in 0.01s =========================
```

## Inject the clock and both branches become testable

`billing.py`

```python
from datetime import datetime

def greeting(now=None):
    h = (now or datetime.now()).hour
    return 'good morning' if h < 12 else 'good afternoon'
```

`test_billing.py`

```python
from datetime import datetime
import billing

def test_morning():
    assert billing.greeting(datetime(2026, 1, 1, 9)) == 'good morning'

def test_afternoon():
    assert billing.greeting(datetime(2026, 1, 1, 15)) == 'good afternoon'
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

test_billing.py::test_morning PASSED                                     [ 50%]
test_billing.py::test_afternoon PASSED                                   [100%]

============================== 2 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
