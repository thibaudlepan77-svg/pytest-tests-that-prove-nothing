def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def test_reads_it_twice():
    g = evens(6)
    assert list(g) == [0, 2, 4]
    assert list(g) == [0, 2, 4]
