def factorial(number: int) -> int:
    """Recursively calculates the factorial of a number"""

    if number < 0:
        raise ValueError('Factorial cannot be calculated for negative numbers')

    if number == 0:
        return 1

    return number * factorial(number - 1)
