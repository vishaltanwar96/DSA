def two_sum_sorted_array(array: list[int], target: int) -> list[int]:
    """
    Question: Given an array of integers numbers that is already sorted in non-decreasing order,
    find two numbers such that they add up to a specific target number.
    Return the indices of the two numbers (1-indexed) as an integer array answer of size 2,
    where 1 <= answer[0] < answer[1] <= numbers.length.
    The tests are generated such that there is exactly one solution. You may not use the same element twice.

    Solution 1(Naive): Use two loops to check each and every combination of two numbers and compare it with target.
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    >>> for i in range(len(array)):
    ...     for j in range(i + 1, len(array)):
    ...         if array[i] + array[j] == target:
    ...             return [i + 1, j + 1]

    Solution 2(A Bit Opmitimised in time complexity): Loop over the array and get each element and its index position
    as key value pairs in a dictionary. Now iterate over the array again and substract the current element from the
    target, if the result is in the dictionary return its value(index) else continue loop
    Time Complexity = O(n)
    Space Complexity = O(n)

    >>> value_index_mapper = {element: index for index, element in enumerate(array)}
    >>> for index in range(len(array)):
    ...     remainder = (target - array[index])
    ...     if remainder in value_index_mapper:
    ...         return [index + 1, value_index_mapper[remainder] + 1]

    Solution 3(Optimized): We can take advantage of the fact that the array is sorted and can use two pointer approach.
    Place the first pointer at the very start of the array and second pointer at the very end of the array.
    Now keep checking the sum of elements present at both the incides. If the sum of both the elements is greater than
    target then we need to decrement the pointer at the end, since we can get the less sum in that direction(array is
    sorted in ascending order) and if the sum is less than the target we need to increment the pointer at the start of
    array(if we increment it we increment the effective sum) and if the sum is equal to the target then we simply exit
    the loop and return a list of start_index + 1 and end_index + 1
    Time complexity = O(n)
    Space complexity = O(1)
    """

    start_index, end_index = 0, len(array) - 1
    while start_index < end_index:
        if array[start_index] + array[end_index] > target:
            end_index -= 1
        elif array[start_index] + array[end_index] < target:
            start_index += 1
        else:
            break
    return [start_index + 1, end_index + 1]
