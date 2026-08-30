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
