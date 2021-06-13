def reverse_array(array: list[int], start: int, end: int) -> list[int]:

    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array


def rotate_array(array: list[int], k: int) -> list[int]:
    """
    Takes an array of integers and a factor by which the array needs to be rotated.
    """

    start = 0
    length_array = len(array)
    end = length_array - 1
    k = k % length_array
    reverse_array(array, start, k - 1)
    reverse_array(array, k, end)
    reverse_array(array, start, end)
    return array
