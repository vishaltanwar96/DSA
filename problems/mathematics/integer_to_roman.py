def int_to_roman(num: int) -> str:
    """
    Conversion is supported till 9999.
    A helper hashmap is needed to map values to a string representation of that number in roman.
    For converting a number to roman number we follow a simple stategy.
    We extract each digit from the number and mulitply with its 10^multiplier.
    if the number is directly present in map we return it otherwise we check if the extracted digit lies between
    9 and 5 if so we simply subtract 5 from it and if anything is remaining (1, 2, 3) we simply prepend
    multiplier * number_string_roman else we append multiplier * number_string_roman.
    """

    number_roman_string_map = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    multiplier = 0
    roman_number = ''

    while num > 0:
        digit = num % 10
        face_value = digit * (10 ** multiplier)

        if face_value in number_roman_string_map:
            roman_number = number_roman_string_map[face_value] + roman_number
        elif 5 < digit < 9:
            leftover = digit - 5
            roman_number = number_roman_string_map[10 ** multiplier] * leftover + roman_number
            roman_number = number_roman_string_map[5 * (10 ** multiplier)] + roman_number
        else:
            roman_number = number_roman_string_map[10 ** multiplier] * digit + roman_number

        num //= 10
        multiplier += 1

    return roman_number
