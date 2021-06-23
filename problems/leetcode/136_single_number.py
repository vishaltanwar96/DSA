def single_number(nums: list[int]) -> int:
    """
    Question:
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space

    Solution 1:
    Loop on the array and store the count of each number in a dictionary.
    Loop on the dictionary and return the number whose count is 1.
    Time complexity = O(n)
    Space complexity = O(n)

    Solution 2:
    Initialize a variable with value 0. Loop the array and xor the number with the result and store it back in result.
    return the result, it will be the single number.
    Time Complexity = O(n)
    Space Complexity = O(1)
    XOR TRUTH TABLE:
    1 ^ 1 == 0
    0 ^ 0 == 0
    1 ^ 0 == 1
    0 ^ 1 == 1

    0 XOR number == number
    number XOR number == 0 (since the bits in the number will be equal and equal bits are 0 when XOR is performed.
    Hence it will ultimately yield the number which is the single one.
    """

    result = 0  # We initialize the number with 0 so that the xor of 0 with number results in the number again.
    for num in nums:  # At Each Iteration
        result = result ^ num
    return result


assert single_number([1, 2, 3, 4, 5, 6, 5, 3, 4, 1, 2]) == 6
assert single_number([99]) == 99
assert single_number([28, 38, 44, 38, 28, 44, 56]) == 56
