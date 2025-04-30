"""
Two Sum Implementation

This file contains multiple implementations to find two numbers in an array that add up to a target value.

Problem Statement:
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target. You may assume that each input would have exactly one
solution, and you may not use the same element twice.

Time Complexity: O(n) for optimal solution using hash map
Space Complexity: O(n) for hash map approach
"""

def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers that add up to target using brute force approach.
    
    Args:
        nums (list[int]): List of integers
        target (int): Target sum
        
    Returns:
        list[int]: Indices of the two numbers that add up to target
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_hashmap(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers that add up to target using hash map approach.
    This is the optimal solution with O(n) time complexity.
    
    Args:
        nums (list[int]): List of integers
        target (int): Target sum
        
    Returns:
        list[int]: Indices of the two numbers that add up to target
    """
    num_map = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []

def two_sum_two_pointers(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers that add up to target using two pointers approach.
    Note: This approach requires the array to be sorted.
    
    Args:
        nums (list[int]): List of integers
        target (int): Target sum
        
    Returns:
        list[int]: Indices of the two numbers that add up to target
    """
    # Create a list of tuples containing (value, original_index)
    nums_with_index = [(num, i) for i, num in enumerate(nums)]
    nums_with_index.sort()  # Sort based on values
    
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums_with_index[left][0] + nums_with_index[right][0]
        
        if current_sum == target:
            return [nums_with_index[left][1], nums_with_index[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

def test_two_sum():
    """Test cases for two sum implementations"""
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),     # Basic case
        ([3, 2, 4], 6, [1, 2]),          # Middle elements
        ([3, 3], 6, [0, 1]),             # Same numbers
        ([1, 2, 3, 4, 5], 9, [3, 4]),    # Larger array
        ([0, 0], 0, [0, 1]),             # Zero values
        ([-1, -2, -3, -4], -7, [2, 3]),  # Negative numbers
    ]
    
    for nums, target, expected in test_cases:
        # Test brute force approach
        result_bf = two_sum_brute_force(nums, target)
        assert sorted(result_bf) == sorted(expected), f"Brute force test failed for {nums} with target {target}"
        
        # Test hashmap approach
        result_hm = two_sum_hashmap(nums, target)
        assert sorted(result_hm) == sorted(expected), f"Hashmap test failed for {nums} with target {target}"
        
        # Test two pointers approach
        result_tp = two_sum_two_pointers(nums, target)
        assert sorted(result_tp) == sorted(expected), f"Two pointers test failed for {nums} with target {target}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_two_sum()
    
    # Example usage
    test_arrays = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 2, 3, 4, 5], 9),
        ([-1, -2, -3, -4], -7)
    ]
    
    print("\nTesting various arrays:")
    for nums, target in test_arrays:
        print(f"\nArray: {nums}, Target: {target}")
        print(f"Using brute force: {two_sum_brute_force(nums, target)}")
        print(f"Using hashmap: {two_sum_hashmap(nums, target)}")
        print(f"Using two pointers: {two_sum_two_pointers(nums, target)}") 