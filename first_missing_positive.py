"""
Problem: First Missing Positive

Given an unsorted integer array nums, find the smallest missing positive integer.

Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
"""

from typing import List

def first_missing_positive(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1

# Test cases
def test_first_missing_positive():
    assert first_missing_positive([1,2,0]) == 3
    assert first_missing_positive([3,4,-1,1]) == 2
    assert first_missing_positive([7,8,9,11,12]) == 1
    assert first_missing_positive([1]) == 2
    assert first_missing_positive([2,1]) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_first_missing_positive() 