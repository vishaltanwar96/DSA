def prime_factors(number: int) -> list[int]:
    """
    - Given a number if a number is divisible by 2 keep dividing it by 2 till all the factors of 2
    are exhausted.(Eliminates the only even prime factor 2 from the number).
    - If all factors of 2 are exhausted or there is no factor of 2, start a loop from number 3 till
    the square root of number or while the square of the number in loop is less than the number given
    for factorization. if the number is divisible by the current number in the loop, then keep dividing
    till it is divisible else increment the number in the loop by 2.(Eliminates all the odd factors from
    the number).
    - Even after the above two steps if the number is not equal to 1 then its safe to assume that the
    number itself is a prime number which can be factored out by itself.
    """

    factors = []
    while number % 2 == 0:
        number = number // 2
        factors.append(2)

    i = 3
    while i ** 2 <= number:
        if number % i == 0:
            number = number // i
            factors.append(i)
        else:
            i += 2

    if number != 1:
        factors.append(number)
    return factors
