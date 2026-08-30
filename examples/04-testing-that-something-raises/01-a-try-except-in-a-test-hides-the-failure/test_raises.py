def divide(a, b):
    return a / b

def test_bad_way():
    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass
