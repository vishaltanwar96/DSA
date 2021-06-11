def euclidean_gcd(num1: int, num2: int) -> int:
    """
    Calculates the highest common factor or greatest common divisor between two numbers.
    As the euclidean algorithm states:
    if num1 == 0 then HCF/GCD between two numbers is num2
    if num2 == 0 then HCF/GCD between two numbers is num1
    if Dividend(num1) = Divisor(num2) * Quotient + Remainder and Divisor != 0 then
    GCD(num1, num2) = GCD(num2, Remainder)
    GCD(Dividend, Divisor) = GCD(Divisor, Remainder)
    Algorithm Explanation At:
    https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
    Also to calculate the GCD of multiple numbers, we can use this:
    GCD(a, b, c, d, e...) = GCD(GCD(GCD(GCD(a, b), c), d), e...)
    """

    if num1 < num2:
        num1, num2 = num2, num1
    if num2 == 0:
        return num1
    return euclidean_gcd(num2, num1 % num2)


def gcd_multiple_nums(*numbers: int) -> int:
    """GCD of 0 and the number is equal to the number itself hence we can start off of that and build the result"""

    def _gcd(a: int, b: int) -> int:

        if a < b:
            a, b, = b, a
        if b == 0:
            return a
        return _gcd(b, a % b)

    result = 0
    for number in numbers:
        result = _gcd(result, number)
    return result
