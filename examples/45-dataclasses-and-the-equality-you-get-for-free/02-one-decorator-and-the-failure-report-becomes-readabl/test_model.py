from model import Point

def test_equal():
    assert Point(1, 2) == Point(1, 2)

def test_shows_the_difference():
    assert Point(1, 2) == Point(1, 3)
