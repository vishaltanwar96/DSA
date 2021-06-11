"""
Properties of LCM
- LCM between two numbers is never less than any of the numbers
- LCM * GCD = Number 1 * Number 2
- LCM between two consecutive numbers is num1 * num2 itself
- LCM(a, b, c, d, e...) = LCM(LCM(LCM(LCM(a, b), c), d), e...)
https://www.cuemath.com/learn/Mathematics/lowest-common-multiple/
"""
from mathematics.hcf import euclidean_gcd


def lcm(num1: int, num2: int) -> int:
    """Iterative solution to calculate lcm"""

    maximum = max(num1, num2)

    value = maximum
    while True:
        try:
            condition = value % num1 == 0 and value % num2 == 0
        except ZeroDivisionError:
            return 0
        if condition:
            break
        else:
            value += maximum
    return value


def lcm_using_gcd(num1: int, num2: int) -> int:
    """LCM * GCD = Number 1 * Number 2"""

    return (num1 * num2) // euclidean_gcd(num1, num2)


def lcm_multiple_numbers(*numbers):
    """
    LCM of a number with itself is equal to the number since the 'least common multiple' of the number is the
    number itself and we can start to build our solution based on that.
    """

    if not numbers:
        return 1

    result = numbers[0]
    for number in numbers:
        result = lcm(result, number)
    return result
