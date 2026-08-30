# Arrange, act, assert, and why the shape matters

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## One test, three sections, one reason to fail

`basket.py`

```python
def total(items, discount=0):
    s = sum(i['price'] * i['qty'] for i in items)
    return round(s * (1 - discount), 2)
```

`test_basket.py`

```python
from basket import total

def test_applies_discount():
    items = [{'price': 10.0, 'qty': 2}, {'price': 5.0, 'qty': 1}]

    got = total(items, discount=0.1)

    assert got == 22.5
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

test_basket.py::test_applies_discount PASSED                             [100%]

============================== 1 passed in 0.01s ==============================
```

## Three assertions, and the report stops at the first

`basket.py`

```python
def total(items, discount=0):
    s = sum(i['price'] * i['qty'] for i in items)
    return round(s * (1 - discount), 2)
```

`test_basket.py`

```python
from basket import total

def test_everything_at_once():
    assert total([]) == 0
    assert total([{'price': 1.0, 'qty': 1}], discount=0.5) == 0.6
    assert total([{'price': 1.0, 'qty': 3}]) == 3.0
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

test_basket.py::test_everything_at_once FAILED                           [100%]

================================== FAILURES ===================================
___________________________ test_everything_at_once ___________________________

    def test_everything_at_once():
        assert total([]) == 0
>       assert total([{'price': 1.0, 'qty': 1}], discount=0.5) == 0.6
E       AssertionError: assert 0.5 == 0.6
E        +  where 0.5 = total([{'price': 1.0, 'qty': 1}], discount=0.5)

test_basket.py:5: AssertionError
=========================== short test summary info ===========================
FAILED test_basket.py::test_everything_at_once - AssertionError: assert 0.5 =...
============================== 1 failed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
