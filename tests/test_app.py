import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import *

def test_add():
    assert add(2, 3) == 5
    assert add(7,3) == 10

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(3,4) == 12

def test_subtract():
    assert subtract(5,2) == 3
    assert subtract(15, 10) == 5