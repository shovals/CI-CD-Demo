import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from app import *

app = Flask(__name__)

@app.route("/")
def home():
    return f"Add: {add(2,3)}, Multiply: {multiply(2,3)}, Subtract: {subtract(7,3)}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


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