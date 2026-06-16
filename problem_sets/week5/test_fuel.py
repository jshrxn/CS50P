import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("1/2") == 50


def test_gauge():
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


def test_value_error():
    with pytest.raises(ValueError):
        convert("3/2")

    with pytest.raises(ValueError):
        convert("-1/4")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
