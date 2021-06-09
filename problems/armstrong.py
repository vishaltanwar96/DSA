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
    The time complexity for calculating the armstrong number is O(log n) since we are dividing the
    number x amount of times to size it down to 1 and hence log n is the time complexity.
    and the space complexity is O(1) as extra space is not required if the number of digits
    scale up and down, the amount of space remains constant.
    """

    order = calculate_order(number)
    total = 0
    number_clone = number

    while number > 0:
        remainder = number % 10
        total += remainder ** order
        number //= 10

    return total == number_clone
