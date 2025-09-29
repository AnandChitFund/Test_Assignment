# tests/test_main.py
from main import add_numbers

def test_add_positive():
    assert add_numbers(2, 3) == 5

def test_add_negative():
    assert add_numbers(-1, -5) == -6

def test_add_zero():
    assert add_numbers(0, 0) == 0
