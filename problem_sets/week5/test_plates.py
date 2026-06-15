from plates import is_valid


def test_validity():
    assert is_valid("CS50") is True
    assert is_valid("CS05") is False
    assert is_valid("AAA22A") is False
    assert is_valid("AAA022") is False
    assert is_valid("PI3.14") is False

def test_length():
    assert is_valid("OUTATIME") is False
    assert is_valid("H") is False
    assert is_valid("AAA2222") is False

def test_alphabetical_start():
    assert is_valid("A1") is False
    assert is_valid("1CS50") is False
    assert is_valid("CS5A") is False
    assert is_valid("CS") is True


