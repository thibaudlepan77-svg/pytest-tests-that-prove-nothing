def level_three(x):
    return 10 / x

def level_two(x):
    return level_three(x)

def level_one(x):
    return level_two(x)

def test_divide():
    assert level_one(0) == 1
