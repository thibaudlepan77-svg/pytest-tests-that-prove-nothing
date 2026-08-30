import billing

def test_says_good_morning():
    assert billing.greeting() == 'good morning'

def test_says_good_afternoon():
    assert billing.greeting() == 'good afternoon'
