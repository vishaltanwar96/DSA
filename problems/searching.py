from typing import Union


def binary_search_recursive(arr: list[int], low: int, high: int, target: int) -> Union[None, int]:
    """
    Recursive implementation of binary search algorithm.
    Base Case will happen when the pointer at left will be to the right of right pointer or right pointer will be to
    the left of left pointer which indicates that the target element is not there in the array.
    Now, we will calculate the middle index between the two pointers. If the element at the middle index is the target
    then we simple return the middle index. If the element at middle index is greater than the target then we check the
    subarray from index low to middle - 1 and if the element at middle index is less than the target then we check for
    the target in subarray middle + 1 to high and we check that recursively.
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
    We start with two pointers low set to 0 and high set to the last index of array. While our high pointer is greater
    than or equal to the low pointer calculate the middle index and check if the element at middle index is target,
    if it is greater than target we simply set high = middle - 1 and if it is less than target then we set
    low = middle + 1 till we go out of bounds using either high or low.
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
