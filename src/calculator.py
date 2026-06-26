"""Calculator module. Operations: add, subtract, multiply, divide, power, modulo."""

from typing import Union

def add(a: Union[float, list], b: float = None) -> float:
    """Add two numbers, or sum a list of numbers."""
    if isinstance(a, list):
        return sum(a)
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

