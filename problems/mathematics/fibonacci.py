def fibonacci_recursive_unmemoized(number):
    """
    Unoptimised Approach to solve fibonacci sequence problem. Doesn't use any memoization. Just simple recursion
    Runtime grows exponentially as number becomes bigger and bigger. O(2^n)
    """

    if number < 0:
        raise ValueError('number cannot be negative')

    if number == 0 or number == 1:
        return number
    return fibonacci_recursive_unmemoized(number - 1) + fibonacci_recursive_unmemoized(number - 2)


def fibonacci_iterative(number):
    """
    Iterative approach to generate fibonacci number. generate a result by adding first and second that is
    F(n) = F(n-1) + F(n-2). calculate the result swap first with second and second with result. Repeat the process from
    number 2 till number itself since F(0) = 0 and F(1) = 1
    """

    if number < 0:
        raise ValueError('number cannot be negative')
    if number == 0 or number == 1:
        return number
    first = 0
    second = 1
    result = 0
    for i in range(2, number + 1):
        result = first + second
        first, second = second, result
    return result


cache = [-1 for _ in range(51)]


def fibonacci_recursive_memoized(number):
    """
    This approach is Dynamic Programming using memoization.
    Recursion + Memoization (Reduce down Large Problem into sub problems and if there's an overlap/ if you've
    encountered the sub problem before use the sub problem's result instead of calculating it again)
    """

    global cache
    if number < 0:
        raise ValueError('number cannot be negative')
    if number == 0 or number == 1:
        return number

    if cache[number] == -1:
        result = fibonacci_recursive_memoized(number - 1) + fibonacci_recursive_memoized(number - 2)
        cache[number] = result
    else:
        result = cache[number]
    return result


print(fibonacci_iterative(40))
print(fibonacci_recursive_memoized(40))
print(fibonacci_recursive_unmemoized(40))
