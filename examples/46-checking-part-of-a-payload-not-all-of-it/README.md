# Checking part of a payload, not all of it

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `got`.

## Asserting the whole dictionary breaks on every new field

`api.py`

```python
def payload():
    return {'id': 7, 'name': 'Ada', 'created': '2026-08-29', 'version': 3}
```

`test_api.py`

```python
from api import payload

def test_whole_thing():
    assert payload() == {'id': 7, 'name': 'Ada'}
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

test_api.py F                                                            [100%]

================================== FAILURES ===================================
______________________________ test_whole_thing _______________________________

    def test_whole_thing():
>       assert payload() == {'id': 7, 'name': 'Ada'}
E       AssertionError: assert {'id': 7, 'na... 'version': 3} == {'id': 7, 'name': 'Ada'}
E         
E         Omitting 2 identical items, use -vv to show
E         Left contains 2 more items:
E         {'created': '2026-08-29', 'version': 3}
E         Use -v to get more diff

test_api.py:4: AssertionError
=========================== short test summary info ===========================
FAILED test_api.py::test_whole_thing - AssertionError: assert {'id': 7, 'na.....
============================== 1 failed in 0.01s ==============================
```

## Assert the subset you actually care about

`api.py`

```python
def payload():
    return {'id': 7, 'name': 'Ada', 'created': '2026-08-29', 'version': 3}
```

`test_api.py`

```python
from api import payload

def test_subset():
    got = payload()
    assert got['id'] == 7
    assert got['name'] == 'Ada'

def test_subset_in_one_line():
    got = payload()
    assert {'id': 7, 'name': 'Ada'}.items() <= got.items()
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

test_api.py::test_subset PASSED                                          [ 50%]
test_api.py::test_subset_in_one_line PASSED                              [100%]

============================== 2 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
