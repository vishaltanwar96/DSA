"""
Properties of LCM
- LCM between two numbers is never less than any of the numbers
- LCM * GCD = Number 1 * Number 2
- LCM between two consecutive numbers is num1 * num2 itself
- LCM(a, b, c, d, e...) = LCM(LCM(LCM(LCM(a, b), c), d), e...)
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
