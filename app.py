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
    if b == 0:
        return "Can't divide in 0"
    else:
        return a/b


if __name__ == "__main__":
    print("Add:", add(2, 3))
    print("Multiply:", multiply(2, 3))
    print("Subtract:", subtract(10,7))
    print("Divide:", divide(30, 5))