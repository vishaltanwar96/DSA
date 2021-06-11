from typing import List, Tuple

from mathematics.hcf import euclidean_gcd


def reduce_fraction(numerator_arr: List[int], denominator_arr: List[int]) -> Tuple[int, int]:

    numerator = 1
    denominator = 1

    for num in numerator_arr:
        numerator *= num

    for num in denominator_arr:
        denominator *= num

    highest_common_factor = euclidean_gcd(numerator, denominator)

    return numerator // highest_common_factor, denominator // highest_common_factor
