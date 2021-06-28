def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Question: Given two sorted arrays nums1 and nums2 of size m and n respectively,
    return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

    Solution 1(Naive):
    Initialize a third array. Take a pointer at starting of each array. Now compare the elements of the two arrays at
    respective pointer positions. Pointers are there to help us insert the lower value of the two values in comparison.
    Insert the lower value in the array. Now if the array length is odd simply return the len(array) // 2 index element
    and if it's even then sum of element at index len(array) // 2 and (len(array) // 2) - 1 and sum / 2 is returned.
    Time Complexity: O(m+n)
    Space Complexity: O(m+n)
    """
    i, j = 0, 0
    nums = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1

    while i < len(nums1):
        nums.append(nums1[i])
        i += 1

    while j < len(nums2):
        nums.append(nums2[j])
        j += 1

    if len(nums) % 2 != 0:
        return nums[len(nums) // 2]
    else:
        return (nums[len(nums) // 2] + nums[(len(nums) // 2) - 1]) / 2
