def factorial(number: int) -> int:
    """
    Recursively calculates the factorial of a number
    Time complexity is O(n) and Space complexity is also O(n) as the stack requires function calls
    equal to n at the same time.
    """

    if number < 0:
        raise ValueError('Factorial cannot be calculated for negative numbers')

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)
