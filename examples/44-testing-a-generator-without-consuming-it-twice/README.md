# Testing a generator without consuming it twice

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## A generator is empty the second time you read it

`test_gen.py`

```python
def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def test_reads_it_twice():
    g = evens(6)
    assert list(g) == [0, 2, 4]
    assert list(g) == [0, 2, 4]
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

test_gen.py F                                                            [100%]

================================== FAILURES ===================================
_____________________________ test_reads_it_twice _____________________________

    def test_reads_it_twice():
        g = evens(6)
        assert list(g) == [0, 2, 4]
>       assert list(g) == [0, 2, 4]
E       assert [] == [0, 2, 4]
E         
E         Right contains 3 more items, first extra item: 0
E         Use -v to get more diff

test_gen.py:9: AssertionError
=========================== short test summary info ===========================
FAILED test_gen.py::test_reads_it_twice - assert [] == [0, 2, 4]
============================== 1 failed in 0.01s ==============================
```

## Materialise once, then assert as many times as you like

`test_gen.py`

```python
def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def test_materialise_once():
    got = list(evens(6))
    assert got == [0, 2, 4]
    assert len(got) == 3
    assert all(x % 2 == 0 for x in got)
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

test_gen.py::test_materialise_once PASSED                                [100%]

============================== 1 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
