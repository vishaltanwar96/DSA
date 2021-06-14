def add_digits(num: int) -> int:
    """
    A number which is obtained by iteratively summing the digits till only 1 digit is left in a number is called
    Digital root. for eg: 3459 = 3+4+5+9 = 21 = 2+1 = 3(This is the digital root of a number)
    In base 10 number system we can directly obtain the digital root using number % 9 (number mod 9, except when the
    number is 9 itself, since 9 % 9 = 0 but the digital root will be 9 itself.
    The approach below is the iterative process which delivers the results in O(n) time and O(1) space
    """
    sum_digits = 0

    while num > 0:
        sum_digits += num % 10
        num //= 10

        if num == 0 and sum_digits < 10:
            return sum_digits
        elif num == 0 and sum_digits > 10:
            num = sum_digits
            sum_digits = 0


def add_digits_constant_time(number: int) -> int:

    if number <= 9:
        return number
    if number % 9 == 0:
        return 9
    return number % 9
