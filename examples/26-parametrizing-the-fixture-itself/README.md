# Parametrizing the fixture itself

1 example. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `fixture`, `params`.

## params on a fixture runs every test that uses it, once per value

`test_indirect.py`

```python
import pytest

@pytest.fixture(params=['sqlite', 'postgres', 'mysql'])
def backend(request):
    return request.param

def test_connects(backend):
    assert backend in ('sqlite', 'postgres', 'mysql')

def test_name_is_lower(backend):
    assert backend == backend.lower()
```

```bash
pytest -v
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 6 items

test_indirect.py::test_connects[sqlite] PASSED                           [ 16%]
test_indirect.py::test_connects[postgres] PASSED                         [ 33%]
test_indirect.py::test_connects[mysql] PASSED                            [ 50%]
test_indirect.py::test_name_is_lower[sqlite] PASSED                      [ 66%]
test_indirect.py::test_name_is_lower[postgres] PASSED                    [ 83%]
test_indirect.py::test_name_is_lower[mysql] PASSED                       [100%]

============================== 6 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
