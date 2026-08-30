# Randomness, and the test that fails once a week

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `sample`, `seed`, `got`.

## Seeded, the failure is identical on every machine

`test_random.py`

```python
import random

def pick_three():
    return random.sample(range(100), 3)

def test_all_below_ten():
    random.seed(0)
    assert all(x < 10 for x in pick_three())
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

test_random.py F                                                         [100%]

================================== FAILURES ===================================
_____________________________ test_all_below_ten ______________________________

    def test_all_below_ten():
        random.seed(0)
>       assert all(x < 10 for x in pick_three())
E       assert False
E        +  where False = all(<generator object test_all_below_ten.<locals>.<genexpr> at 0x000001F39C930860>)

test_random.py:8: AssertionError
=========================== short test summary info ===========================
FAILED test_random.py::test_all_below_ten - assert False
============================== 1 failed in 0.01s ==============================
```

## Assert the shape, not the values

`test_random.py`

```python
import random

def pick_three():
    return random.sample(range(100), 3)

def test_shape_not_values():
    random.seed(1234)
    got = pick_three()
    assert len(got) == 3
    assert len(set(got)) == 3
    assert all(0 <= x < 100 for x in got)
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

test_random.py::test_shape_not_values PASSED                             [100%]

============================== 1 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
