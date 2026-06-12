from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0

def test_hvalue():
    assert value("h") == 20
    assert value("Hey There!") == 20

def test_case_sensitivity():
    assert value("HeLLo") == 0

def test_else():
    assert value("what's up?") == 100

