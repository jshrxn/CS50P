import pytest
from project import Password
from project import PasswordAnalyzer

def test_project_password_charecteristics():
    password_obj = Password("Hello123")
    assert password_obj.password_length == 8
    assert password_obj.uppercase_count == 1
    assert password_obj.lowercase_count == 4
    assert password_obj.digit_count == 3
    assert password_obj.symbol_count == 0

def test_character_pool():
    password_obj = Password("Hello123")
    analyzer = PasswordAnalyzer(password_obj)

    assert analyzer.character_pool() == 62

def test_search_space():
    password_obj = Password("Hello123")
    analyzer = PasswordAnalyzer(password_obj)

    assert analyzer.search_space() == pytest.approx(218340105584896)

def test_entropy():
    password_obj = Password("Hello123")
    analyzer = PasswordAnalyzer(password_obj)

    assert analyzer.entropy() == pytest.approx(47.633570483095)

def test_strength_rating():
    password_obj = Password("Hello123")
    analyzer = PasswordAnalyzer(password_obj)

    assert analyzer.strength_rating() == "Moderate"

def test_crack_time():
    password_obj = Password("Hello123")
    analyzer = PasswordAnalyzer(password_obj)

    assert analyzer.crack_time() == pytest.approx(218340105.584896)




