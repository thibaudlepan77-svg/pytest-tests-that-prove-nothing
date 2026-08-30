# A suite that passes alone and fails together

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## Run them separately and everything is green

`test_order.py`

```python
CACHE = {}

def test_writes():
    CACHE['user'] = 'Ada'
    assert CACHE['user'] == 'Ada'

def test_expects_empty():
    assert CACHE == {}
```

```bash
pytest -v test_order.py::test_expects_empty
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 1 item

test_order.py::test_expects_empty PASSED                                 [100%]

============================== 1 passed in 0.01s ==============================
```

## Run them together and the order decides

`test_order.py`

```python
CACHE = {}

def test_writes():
    CACHE['user'] = 'Ada'
    assert CACHE['user'] == 'Ada'

def test_expects_empty():
    assert CACHE == {}
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

test_order.py::test_writes PASSED                                        [ 50%]
test_order.py::test_expects_empty FAILED                                 [100%]

================================== FAILURES ===================================
_____________________________ test_expects_empty ______________________________

    def test_expects_empty():
>       assert CACHE == {}
E       AssertionError: assert {'user': 'Ada'} == {}
E         
E         Left contains 1 more item:
E         {'user': 'Ada'}
E         
E         Full diff:
E         - {}
E         + {
E         +     'user': 'Ada',
E         + }

test_order.py:8: AssertionError
=========================== short test summary info ===========================
FAILED test_order.py::test_expects_empty - AssertionError: assert {'user': 'A...
========================= 1 failed, 1 passed in 0.01s =========================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
