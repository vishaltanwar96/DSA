import math


def count_bruteforce(num: int) -> int:
    """
    Bruteforce approach
    Time Complexity: O(log base 10 N + 1)
    Space Complexity: O(1)
    """
    n = 0
    num_replica = num
    while num_replica > 0:
        num_replica //= 10
        n += 1
    return n


def count_optimal(num: int) -> int:
    """
    Optimal Approach
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return int(math.log10(num)) + 1
