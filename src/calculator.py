"""Calculator module. Operations: add, subtract, multiply, divide, power, modulo."""

<<<<<<< HEAD
def add(a, b=None):
    if isinstance(a, list):
        return sum(a)
=======
def add(a: float, b: float) -> float:
    """Add two numbers and return the result."""
>>>>>>> origin
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

def modulo(a, b):
    return a % b

