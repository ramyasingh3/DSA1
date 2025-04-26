"""
Problem: Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays, and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9] or [9,4]
"""

from typing import List
from collections import Counter

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    counts = Counter(nums1)
    result = []
    for num in nums2:
        if counts[num] > 0:
            result.append(num)
            counts[num] -= 1
    return result

# Test cases
def test_intersect():
    assert sorted(intersect([1,2,2,1], [2,2])) == [2,2]
    assert sorted(intersect([4,9,5], [9,4,9,8,4])) == [4,9]
    assert intersect([], [1,2]) == []
    assert intersect([1,2], []) == []
    assert intersect([1], [1]) == [1]
    print("All test cases passed!")

if __name__ == "__main__":
    test_intersect() 