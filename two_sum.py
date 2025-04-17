from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers in the array that add up to the target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing the indices of the two numbers that add up to target
    """
    # Create a dictionary to store the complement of each number
    num_dict = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # If complement exists in dictionary, return the indices
        if complement in num_dict:
            return [num_dict[complement], i]
        
        # Store the current number and its index
        num_dict[num] = i
    
    # If no solution found, return empty list
    return []

def test_two_sum():
    """Test cases for the two sum solution."""
    
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
        ([1, 2, 3, 4, 5], 10, []),
        ([], 0, []),
        # Edge cases
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
        ([1, 1, 1, 1, 1], 2, [0, 1]),
        # Large numbers
        ([1000000, 2000000, 3000000], 5000000, [1, 2])
    ]
    
    print("Testing Two Sum Solution...")
    for nums, target, expected in test_cases:
        result = two_sum(nums, target)
        
        print(f"\nInput: nums = {nums}, target = {target}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_two_sum() 