"""Main calculator module."""

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
    
def power(base, exp):
    return base ** exp