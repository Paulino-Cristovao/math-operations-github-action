"""
Module containing basic mathematical operations.
"""

def add(a: float, b: float) -> float:
    """
    Return the sum of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    assert isinstance(a, (int, float)), "First argument must be a number"
    assert isinstance(b, (int, float)), "Second argument must be a number"
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Return the difference of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference of the two numbers.
    """
    assert isinstance(a, (int, float)), "First argument must be a number"
    assert isinstance(b, (int, float)), "Second argument must be a number"
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Return the product of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    assert isinstance(a, (int, float)), "First argument must be a number"
    assert isinstance(b, (int, float)), "Second argument must be a number"
    return a * b


def divide(a: float, b: float) -> float:
    """
    Return the division of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The division of the two numbers.
    
    Raises:
        ValueError: If the second number is zero.
    """
    assert isinstance(a, (int, float)), "First argument must be a number"
    assert isinstance(b, (int, float)), "Second argument must be a number"
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


