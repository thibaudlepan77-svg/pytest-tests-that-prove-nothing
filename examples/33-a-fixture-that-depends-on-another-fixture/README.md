# Pytest fixture example

_A fixture that depends on another fixture._

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `fixture`.

## Fixtures compose, and pytest works out the order

`test_compose.py`

```python
import pytest

@pytest.fixture
def config():
    print('BUILD config')
    return {'host': 'localhost', 'port': 5432}

@pytest.fixture
def client(config):
    print('BUILD client')
    return {'url': config['host'] + ':' + str(config['port'])}

def test_url(client):
    assert client['url'] == 'localhost:5432'
```

```bash
pytest -v -s
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 1 item

test_compose.py::test_url BUILD config
BUILD client
PASSED

============================== 1 passed in 0.01s ==============================
```

## A test can override a fixture for itself

`conftest.py`

```python
import pytest

@pytest.fixture
def config():
    return {'host': 'localhost', 'port': 5432}
```

`test_override.py`

```python
import pytest

@pytest.fixture
def config():
    return {'host': 'example.com', 'port': 443}

def test_uses_local_override(config):
    assert config['host'] == 'example.com'
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

test_override.py::test_uses_local_override PASSED                        [100%]

============================== 1 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
