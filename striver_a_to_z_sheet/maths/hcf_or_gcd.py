def hcf_brute_force(number1, number2) -> int:
    hcf = 1
    for number in range(1, min(number1, number2) + 1):
        if number1 % number == 0 and number2 % number == 0:
            hcf = number
    return hcf


def hcf_optimised(number1: int, number2: int) -> int:
    if number1 == 0:
        return number2
    if number2 == 0:
        return number1
    if number1 > number2:
        return hcf_optimised(number1 % number2, number2)
    return hcf_optimised(number2 % number1, number1)
