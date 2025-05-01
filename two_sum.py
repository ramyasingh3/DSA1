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

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers
    such that they add up to target.
    
    Args:
        nums (list[int]): List of integers
        target (int): Target sum
        
    Returns:
        list[int]: List containing the indices of two numbers that add up to target
        
    Raises:
        ValueError: If no solution exists
    """
    # Dictionary to store number -> index mapping
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # If complement exists in map, we found our pair
        if complement in num_map:
            return [num_map[complement], i]
        
        # Store current number and its index
        num_map[num] = i
    
    # If we get here, no solution exists
    raise ValueError("No two numbers in the array sum up to the target")

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
        result_hm = two_sum(nums, target)
        assert sorted(result_hm) == sorted(expected), f"Hashmap test failed for {nums} with target {target}"
        
        # Test two pointers approach
        result_tp = two_sum_two_pointers(nums, target)
        assert sorted(result_tp) == sorted(expected), f"Two pointers test failed for {nums} with target {target}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_two_sum()
    
    # Example usage
    test_cases = [
        ([2, 7, 11, 15], 9),      # Expected: [0, 1]
        ([3, 2, 4], 6),           # Expected: [1, 2]
        ([3, 3], 6),              # Expected: [0, 1]
        ([1, 5, 3, 7, 9], 12),    # Expected: [1, 3]
        ([-1, -2, -3, -4], -7),   # Expected: [2, 3]
    ]
    
    for nums, target in test_cases:
        try:
            result = two_sum(nums, target)
            print(f"Input: nums = {nums}, target = {target}")
            print(f"Output: {result}")
            print(f"Explanation: nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {target}\n")
        except ValueError as e:
            print(f"Input: nums = {nums}, target = {target}")
            print(f"Error: {str(e)}\n") 