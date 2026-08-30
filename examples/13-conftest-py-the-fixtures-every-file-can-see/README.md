# conftest.py, the fixtures every file can see

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `fixture`.

## A fixture in conftest is available without importing it

`conftest.py`

```python
import pytest

@pytest.fixture
def customer():
    return {'id': 1, 'name': 'Ada', 'credit': 100}
```

`test_orders.py`

```python
def test_has_credit(customer):
    assert customer['credit'] == 100
```

`test_billing.py`

```python
def test_name(customer):
    assert customer['name'] == 'Ada'
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

test_billing.py::test_name PASSED                                        [ 50%]
test_orders.py::test_has_credit PASSED                                   [100%]

============================== 2 passed in 0.01s ==============================
```

## Nothing is imported, and that is the part people distrust

`conftest.py`

```python
import pytest

@pytest.fixture
def customer():
    return {'id': 1, 'name': 'Ada', 'credit': 100}
```

`test_typo.py`

```python
def test_wrong_name(custmer):
    assert custmer['name'] == 'Ada'
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

test_typo.py::test_wrong_name ERROR                                      [100%]

=================================== ERRORS ====================================
______________________ ERROR at setup of test_wrong_name ______________________
file /test_typo.py, line 1
  def test_wrong_name(custmer):
E       fixture 'custmer' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, capfd, capfdbinary, caplog, capsys, capsysbinary, capteesys, customer, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, subtests, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

test_typo.py:1
=========================== short test summary info ===========================
ERROR test_typo.py::test_wrong_name
============================== 1 error in 0.01s ===============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
