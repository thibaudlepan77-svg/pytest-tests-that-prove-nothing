from datetime import datetime
import billing

def test_morning():
    assert billing.greeting(datetime(2026, 1, 1, 9)) == 'good morning'

def test_afternoon():
    assert billing.greeting(datetime(2026, 1, 1, 15)) == 'good afternoon'
