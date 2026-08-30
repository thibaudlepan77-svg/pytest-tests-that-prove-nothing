# Naming your cases with ids

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## Without ids, the report shows the raw values

`test_ids.py`

```python
import pytest

def vat(amount, country):
    rates = {'FR': 0.20, 'DE': 0.19, 'JP': 0.10}
    return round(amount * (1 + rates[country]), 2)

@pytest.mark.parametrize('amount,country,expected', [
    (100, 'FR', 120.0),
    (100, 'DE', 119.0),
    (100, 'JP', 110.0),
])
def test_vat(amount, country, expected):
    assert vat(amount, country) == expected
```

```bash
pytest -v
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 3 items

test_ids.py::test_vat[100-FR-120.0] PASSED                               [ 33%]
test_ids.py::test_vat[100-DE-119.0] PASSED                               [ 66%]
test_ids.py::test_vat[100-JP-110.0] PASSED                               [100%]

============================== 3 passed in 0.01s ==============================
```

## With ids, the report reads like a sentence

`test_ids.py`

```python
import pytest

def vat(amount, country):
    rates = {'FR': 0.20, 'DE': 0.19, 'JP': 0.10}
    return round(amount * (1 + rates[country]), 2)

@pytest.mark.parametrize('amount,country,expected', [
    (100, 'FR', 120.0),
    (100, 'DE', 119.0),
    (100, 'JP', 110.0),
], ids=['france', 'germany', 'japan'])
def test_vat(amount, country, expected):
    assert vat(amount, country) == expected
```

```bash
pytest -v
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 3 items

test_ids.py::test_vat[france] PASSED                                     [ 33%]
test_ids.py::test_vat[germany] PASSED                                    [ 66%]
test_ids.py::test_vat[japan] PASSED                                      [100%]

============================== 3 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
