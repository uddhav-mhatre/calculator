"""Calculator module. Operations: add, subtract, multiply, divide, power, modulo."""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a,b):
    if b == 0 :
        raise ValueError("division not possible")
    return a / b
    
def modulo(a, b):
    return a % b