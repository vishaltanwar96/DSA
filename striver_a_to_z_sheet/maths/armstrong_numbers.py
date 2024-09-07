import math


def is_armstrong(number: int) -> bool:
    number_clone = number
    number_of_digits = int(math.log10(number)) + 1
    another_number = 0
    while number_clone != 0:
        last_digit = number_clone % 10
        another_number += last_digit ** number_of_digits
        number_clone //= 10
    return number == another_number
