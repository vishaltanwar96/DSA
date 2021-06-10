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
    """

    if num2 == 0:
        return num1
    else:
        if num1 < num2:
            num1, num2 = num2, num1
        return euclidean_gcd(num2, num1 % num2)
