import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import add, multiply, subtract, divide

def test_add():
    assert add(2, 3) == 5
    assert add(7,3) == 10

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(3,4) == 12

def test_subtract():
    assert subtract(5,2) == 3
    assert subtract(15, 10) == 5

def test_divide():
    assert divide(20,4) == 5
    assert divide(100, 10) == 10