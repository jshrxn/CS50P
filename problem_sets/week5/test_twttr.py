from twttr import shorten


def test_lowercase_vowels():
    assert shorten("twitter") == "twttr"


def test_uppercase_vowels():
    assert shorten("TWITTER") == "TWTTR"


def test_numbers():
    assert shorten("CS50") == "CS50"


def test_punctuation():
    assert shorten("Hello, World!") == "Hll, Wrld!"


def test_only_vowels():
    assert shorten("aeiouAEIOU") == ""
