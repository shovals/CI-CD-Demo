from flask import Flask

app = Flask(__name__)

def add(a, b):
    # This function adds two numbers
    return a + b

def multiply(a, b):
    # This function multiply 2 numbers
    return a * b

def subtract(a, b):
    # This function subtract 2 numbers
    return a-b

def divide(a, b):
    # This function divide 2 numbers
    if b == 0:
        return "Can't divide in 0"
    else:
        return a/b


# Home route
@app.route("/")
def home():
    return f"Add: {add(2,3)}, Multiply: {multiply(2,3)}, Subtract: {subtract(7,3)}, Divide: {divide(30,5)}"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render uses this automatically
    app.run(host="0.0.0.0", port=port)
