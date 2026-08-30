# Dataclasses, and the equality you get for free

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## A plain class compares by identity, so the test fails

`model.py`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

`test_model.py`

```python
from model import Point

def test_equal():
    assert Point(1, 2) == Point(1, 2)
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

test_model.py F                                                          [100%]

================================== FAILURES ===================================
_________________________________ test_equal __________________________________

    def test_equal():
>       assert Point(1, 2) == Point(1, 2)
E       assert <model.Point object at 0x000002989D65C050> == <model.Point object at 0x000002989D5D0E10>
E        +  where <model.Point object at 0x000002989D65C050> = Point(1, 2)
E        +  and   <model.Point object at 0x000002989D5D0E10> = Point(1, 2)

test_model.py:4: AssertionError
=========================== short test summary info ===========================
FAILED test_model.py::test_equal - assert <model.Point object at 0x000002989D...
============================== 1 failed in 0.01s ==============================
```

## One decorator, and the failure report becomes readable

`model.py`

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```

`test_model.py`

```python
from model import Point

def test_equal():
    assert Point(1, 2) == Point(1, 2)

def test_shows_the_difference():
    assert Point(1, 2) == Point(1, 3)
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

test_model.py::test_equal PASSED                                         [ 50%]
test_model.py::test_shows_the_difference FAILED                          [100%]

================================== FAILURES ===================================
__________________________ test_shows_the_difference __________________________

    def test_shows_the_difference():
>       assert Point(1, 2) == Point(1, 3)
E       AssertionError: assert Point(x=1, y=2) == Point(x=1, y=3)
E         
E         Omitting 1 identical items, use -vv to show
E         Differing attributes:
E         ['y']
E         
E         Drill down into differing attribute y:
E           y: 2 != 3

test_model.py:7: AssertionError
=========================== short test summary info ===========================
FAILED test_model.py::test_shows_the_difference - AssertionError: assert Poin...
========================= 1 failed, 1 passed in 0.01s =========================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
