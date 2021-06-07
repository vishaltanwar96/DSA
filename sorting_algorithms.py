def selection_sort(arr):
    """
    This algorithm selects the minimum value at each pass and swaps it with
    index which is equal to the pass number and starts with 0 and
    is incremented by 1 at each pass. The algorithm requires you to make
    n passes where in each pass you scan all the elements for minimum value.
    Hence the runtime complexity of this algorithm is O(n^2)
    """

    for iteration_number in range(0, len(arr)):
        min_value_index = iteration_number
        min_value = arr[iteration_number]
        for index in range(iteration_number + 1, len(arr)):
            if arr[index] < min_value:
                min_value_index = index
                min_value = arr[index]
        arr[iteration_number], arr[min_value_index] = arr[min_value_index], arr[iteration_number]
    return arr


def merge_sort_helper(left_subarray, right_subarray, original_array):

    i, j, k = 0, 0, 0
    length_left_subarray = len(left_subarray)
    length_right_subarray = len(right_subarray)

    # Start comparing values from 0 index of left and right subarray.
    # if left array value is less than right array insert it in original array and vice versa
    # till one of the array values are exhausted
    # increment the pointer by 1 of the array whose value is inserted into original array
    # also increment the pointer by 1 for the original array indicating that
    # at each pass the original subarray is being sorted
    while i < length_left_subarray and j < length_right_subarray:
        if left_subarray[i] < right_subarray[j]:
            original_array[k] = left_subarray[i]
            i += 1
        else:
            original_array[k] = right_subarray[j]
            j += 1
        k += 1

    # fill in the values of the left subarray in the original array if there are any remaining
    while i < length_left_subarray:
        original_array[k] = left_subarray[i]
        i += 1
        k += 1
    # fill in the values of the right subarray in the original array if there are any remaining
    while j < length_right_subarray:
        original_array[k] = right_subarray[j]
        j += 1
        k += 1
    return original_array


def merge_sort(arr):
    """
    This sorting algorithm takes the divide and conquer approach to sort the array
    Each array is divided into two parts till each part is one element in length
    The conquer step is to combine the arrays while also comparing all the elements starting from 0th index
    in both the subarrays and replacing the min element with the value of `iteration` index of the original array.
    This algorithm has a time complexity of O(n*logn) although this uses extra space
    and has a space complexity of O(n)
    """

    arr_length = len(arr)
    # If the length of array is either one or empty return it since it is already sorted
    if arr_length < 2:
        return arr
    # else divide the array into two halves
    # each of the half is then recursively halved till
    # they are just one element long and then are combined and sorted using merge_sort_helper
    # sort each half by using the merge sort helper when all the recursion has given you the sorted halves.
    middle = arr_length // 2
    left_subarr = merge_sort(arr[:middle])
    right_subarr = merge_sort(arr[middle:])
    return merge_sort_helper(left_subarr, right_subarr, arr)


def bubble_sort(arr):
    """
    This algorithm sorts the given array by comparing adjacent elements with each other.
    It makes n-1 comparisons at each pass. So the time complexity for this algorithm is O(n*(n-1)) -> O(n^2)
    The biggest number is pushed to the right repeatedly at one iteration and
    we dont include the element at index (len(arr) - current_index) in our comparisons.
    Runtime complexity is O(n^2) and no extra space is used(INPLACE)
    """

    for iteration_number in range(0, len(arr)):
        for index in range(0, len(arr) - 1 - iteration_number):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
    return arr


def insertion_sort(arr):
    """
    This algorithm involves inserting values from certain index to another index so that it becomes sorted.
    We assume that there are two parts in an array, a sorted subarray and an unsorted subarray.
    We start with index value 1 assuming 0 is already sorted(since it's a single element) and go till len(arr) - 1.
    The unsorted value is checked if it can be inserted at a certain place in all the sorted values.
    We check if the unsorted value is less than the first encountered sorted value, if that's the case
    we continue to check for subsequent sorted values else we insert it before the last value that is greater than
    the unsorted value. So we basically treat the place of the first unsorted value as a hole and move the hole to
    appropriate position(We shift all the values and the hole) and insert the value there.
    Runtime complexity is O(n^2) and no extra space is used(INPLACE)
    """

    for index in range(1, len(arr)):
        value_at_initial_hole = arr[index]
        hole = index

        while hole > 0 and arr[hole - 1] > value_at_initial_hole:
            arr[hole] = arr[hole - 1]
            hole -= 1
        arr[hole] = value_at_initial_hole
    return arr


def quick_sort_partition_helper(arr, low, high):
    """
    Selects a pivot and helps in partitioning elements less than the pivot to its left and greater to its right.
    :returns pivot index
    """

    i = low + 1
    j = high - 1
    pivot_value = arr[low]

    while i < j:

        while arr[i] <= pivot_value:
            i += 1

        while arr[j] > pivot_value:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j


def quick_sort(arr, low, high):
    """Sorts array using partitioning"""

    if low < high:
        pivot = quick_sort_partition_helper(arr, low, high)
        quick_sort(arr, low, pivot)
        quick_sort(arr, pivot + 1, high)
    return arr
