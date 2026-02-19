from src.checker import is_even, is_odd

def test_even_number():
    assert is_even(4) is True

def test_odd_number():
    assert is_even(7) is False

def test_is_odd():
    assert is_odd(9) is True
