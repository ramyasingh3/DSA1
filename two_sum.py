from typing import List, Tuple

class Solution:
    def two_sum_brute_force(self, nums: List[int], target: int) -> Tuple[int, int]:
        """
        Brute force approach checking all possible pairs.
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return (i, j)
        return (-1, -1)

    def two_sum_hash(self, nums: List[int], target: int) -> Tuple[int, int]:
        """
        Using hash table to store complements.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return (num_dict[complement], i)
            num_dict[num] = i
        return (-1, -1)

    def two_sum_sort(self, nums: List[int], target: int) -> Tuple[int, int]:
        """
        Using sorting and two pointers.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        # Create a list of tuples containing value and original index
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        # Sort based on the number value
        nums_with_index.sort()
        
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            if current_sum == target:
                return (nums_with_index[left][1], nums_with_index[right][1])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return (-1, -1)

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case
    nums = [2, 7, 11, 15]
    target = 9
    print("Test Case 1:")
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Brute Force: {solution.two_sum_brute_force(nums, target)}")
    print(f"Hash Method: {solution.two_sum_hash(nums, target)}")
    print(f"Sort Method: {solution.two_sum_sort(nums, target)}")
    print()
    
    # Test Case 2: Multiple solutions
    nums = [3, 2, 4]
    target = 6
    print("Test Case 2:")
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Brute Force: {solution.two_sum_brute_force(nums, target)}")
    print(f"Hash Method: {solution.two_sum_hash(nums, target)}")
    print(f"Sort Method: {solution.two_sum_sort(nums, target)}")
    print()
    
    # Test Case 3: Negative numbers
    nums = [-1, -2, -3, -4, -5]
    target = -8
    print("Test Case 3:")
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Brute Force: {solution.two_sum_brute_force(nums, target)}")
    print(f"Hash Method: {solution.two_sum_hash(nums, target)}")
    print(f"Sort Method: {solution.two_sum_sort(nums, target)}")
    print()
    
    # Test Case 4: No solution
    nums = [1, 2, 3, 4]
    target = 8
    print("Test Case 4:")
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Brute Force: {solution.two_sum_brute_force(nums, target)}")
    print(f"Hash Method: {solution.two_sum_hash(nums, target)}")
    print(f"Sort Method: {solution.two_sum_sort(nums, target)}")
    print()
    
    # Test Case 5: Large array
    nums = list(range(1000))
    target = 1997
    print("Test Case 5:")
    print(f"Input: nums = [0,1,2,...,999], target = {target}")
    print(f"Brute Force: {solution.two_sum_brute_force(nums, target)}")
    print(f"Hash Method: {solution.two_sum_hash(nums, target)}")
    print(f"Sort Method: {solution.two_sum_sort(nums, target)}")

if __name__ == "__main__":
    test_solution() 