def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def test_materialise_once():
    got = list(evens(6))
    assert got == [0, 2, 4]
    assert len(got) == 3
    assert all(x % 2 == 0 for x in got)
