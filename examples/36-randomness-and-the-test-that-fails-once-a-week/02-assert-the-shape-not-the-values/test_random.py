import random

def pick_three():
    return random.sample(range(100), 3)

def test_shape_not_values():
    random.seed(1234)
    got = pick_three()
    assert len(got) == 3
    assert len(set(got)) == 3
    assert all(0 <= x < 100 for x in got)
