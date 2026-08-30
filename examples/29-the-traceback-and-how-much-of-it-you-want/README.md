# The traceback, and how much of it you want

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## The default traceback shows every frame

`test_tb.py`

```python
def level_three(x):
    return 10 / x

def level_two(x):
    return level_three(x)

def level_one(x):
    return level_two(x)

def test_divide():
    assert level_one(0) == 1
```

```bash
pytest 
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collected 1 item

test_tb.py F                                                             [100%]

================================== FAILURES ===================================
_________________________________ test_divide _________________________________

    def test_divide():
>       assert level_one(0) == 1
               ^^^^^^^^^^^^

test_tb.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
test_tb.py:8: in level_one
    return level_two(x)
           ^^^^^^^^^^^^
test_tb.py:5: in level_two
    return level_three(x)
           ^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

x = 0

    def level_three(x):
>       return 10 / x
               ^^^^^^
E       ZeroDivisionError: division by zero

test_tb.py:2: ZeroDivisionError
=========================== short test summary info ===========================
FAILED test_tb.py::test_divide - ZeroDivisionError: division by zero
============================== 1 failed in 0.01s ==============================
```

## --tb=line gives you one line per failure

`test_tb.py`

```python
def level_three(x):
    return 10 / x

def level_two(x):
    return level_three(x)

def level_one(x):
    return level_two(x)

def test_divide():
    assert level_one(0) == 1
```

```bash
pytest --tb=line
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collected 1 item

test_tb.py F                                                             [100%]

================================== FAILURES ===================================
E   ZeroDivisionError: division by zero
test_tb.py:2: ZeroDivisionError: division by zero
=========================== short test summary info ===========================
FAILED test_tb.py::test_divide - ZeroDivisionError: division by zero
============================== 1 failed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
