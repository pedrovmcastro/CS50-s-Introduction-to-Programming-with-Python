from bank import value

def test_whatsup():
    assert value("What's up?") == 100

def test_hey():
    assert value("hey") == 20

def test_Hey():
    assert value("Hey") == 20

def test_hello():
    assert value("Hello") == 0

def test_hellosir():
    assert value("Hello, sir!") == 0
