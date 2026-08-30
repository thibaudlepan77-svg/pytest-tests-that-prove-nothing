import random

def pick_three():
    return random.sample(range(100), 3)

def test_all_below_ten():
    random.seed(0)
    assert all(x < 10 for x in pick_three())
