def calculate_order(number: int) -> int:
    """Calculates the number of digits in a number"""

    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count


def is_armstrong(number: int) -> bool:
    """
    Checks whether a number is armstrong or not.
    An armstrong number is a number which satisfies this equation:
    abc = a^order(abc) + b^order(abc) + c^order(abc)
    """

    order = calculate_order(number)
    total = 0
    number_clone = number

    while number > 0:
        remainder = number % 10
        total += remainder ** order
        number //= 10

    return total == number_clone
