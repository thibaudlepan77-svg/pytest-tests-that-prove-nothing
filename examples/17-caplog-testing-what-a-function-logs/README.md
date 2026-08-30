# caplog, testing what a function logs

1 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## caplog gives you the records, not the formatted text

`test_log.py`

```python
import logging

log = logging.getLogger('billing')

def charge(amount):
    if amount < 0:
        log.warning('negative amount %s', amount)
        return 0
    return amount

def test_logs_warning(caplog):
    with caplog.at_level(logging.WARNING):
        charge(-5)
    assert 'negative amount' in caplog.text
    assert caplog.records[0].levelname == 'WARNING'
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

test_log.py::test_logs_warning PASSED                                    [100%]

============================== 1 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
