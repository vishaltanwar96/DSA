from typing import Union


def binary_search_recursive(arr: list[int], low: int, high: int, target: int) -> Union[None, int]:
    """
    Recursive implementation of binary search algorithm.
    Time Complexity: O(log n)
    Space Complexity: O(log n)
    """

    # Base Case
    if low > high:
        return None

    # Recursive Case
    middle = (low + high) // 2

    if arr[middle] < target:
        return binary_search_recursive(arr, middle + 1, high, target)
    elif arr[middle] > target:
        return binary_search_recursive(arr, low, middle - 1, target)
    else:
        return middle


def binary_search_iterative(arr: list[int], target: int) -> Union[None, int]:
    """
    Iterative Implementation of Binary Search.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """

    low = 0
    high = len(arr) - 1

    while high >= low:
        middle = (low + high) // 2
        if arr[middle] < target:
            low = middle + 1
        elif arr[middle] > target:
            high = middle - 1
        else:
            return middle
    return None


binary_search_iterative([11, 12, 13, 20, 25, 26, 34, 35, 42, 63, 67, 68, 80, 85, 87, 88, 93, 93, 97, 98], 98)