def hcf_brute_force(number1, number2) -> int:
    hcf = 1
    for number in range(1, min(number1, number2) + 1):
        if number1 % number == 0 and number2 % number == 0:
            hcf = number
    return hcf
