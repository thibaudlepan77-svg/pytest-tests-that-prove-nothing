# Reading the diff on dictionaries and lists

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## pytest shows you which key differs, not just that they differ

`test_diff.py`

```python
def build():
    return {'id': 1, 'name': 'Ada', 'active': True, 'credit': 90}

def test_shape():
    assert build() == {'id': 1, 'name': 'Ada', 'active': True, 'credit': 100}
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

test_diff.py F                                                           [100%]

================================== FAILURES ===================================
_________________________________ test_shape __________________________________

    def test_shape():
>       assert build() == {'id': 1, 'name': 'Ada', 'active': True, 'credit': 100}
E       AssertionError: assert {'id': 1, 'na... 'credit': 90} == {'id': 1, 'na...'credit': 100}
E         
E         Omitting 3 identical items, use -vv to show
E         Differing items:
E         {'credit': 90} != {'credit': 100}
E         Use -v to get more diff

test_diff.py:5: AssertionError
=========================== short test summary info ===========================
FAILED test_diff.py::test_shape - AssertionError: assert {'id': 1, 'na... 'cr...
============================== 1 failed in 0.01s ==============================
```

## On long lists it points at the index

`test_diff.py`

```python
def test_list():
    got = [1, 2, 3, 4, 5, 6]
    want = [1, 2, 3, 4, 9, 6]
    assert got == want
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

test_diff.py F                                                           [100%]

================================== FAILURES ===================================
__________________________________ test_list __________________________________

    def test_list():
        got = [1, 2, 3, 4, 5, 6]
        want = [1, 2, 3, 4, 9, 6]
>       assert got == want
E       assert [1, 2, 3, 4, 5, 6] == [1, 2, 3, 4, 9, 6]
E         
E         At index 4 diff: 5 != 9
E         Use -v to get more diff

test_diff.py:4: AssertionError
=========================== short test summary info ===========================
FAILED test_diff.py::test_list - assert [1, 2, 3, 4, 5, 6] == [1, 2, 3, 4, 9, 6]
============================== 1 failed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
