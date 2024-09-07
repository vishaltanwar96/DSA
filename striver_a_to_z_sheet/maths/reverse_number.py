def reverse_number(num: int) -> int:
    number = num
    reversed_num = 0
    while number != 0:
        last_digit = number % 10
        reversed_num = reversed_num * 10 + last_digit
        number //= 10
    return reversed_num
