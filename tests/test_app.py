import pytest
from app import add, multiply, subtract, divide

from flask import Flask, jsonify

app = Flask(__name__)

# Your calculation functions
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

@app.route("/")
def home():
    a, b = 2, 3
    c, d = 7, 3
    e, f = 30, 5
    return jsonify({
        "Add": add(a, b),
        "Multiply": multiply(a, b),
        "Subtract": subtract(c, d),
        "Divide": divide(e, f)
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render sets this automatically
    app.run(host="0.0.0.0", port=port)


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