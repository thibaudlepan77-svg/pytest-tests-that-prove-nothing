def greet(name):
    print('Hello, ' + name)

def test_twice(capsys):
    greet('Ada')
    first = capsys.readouterr().out
    second = capsys.readouterr().out
    assert first == 'Hello, Ada\n'
    assert second == 'Hello, Ada\n'
