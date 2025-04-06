from typing import List, Tuple, Optional

class Solution:
    def two_sum_brute_force(self, nums: List[int], target: int) -> Optional[Tuple[int, int]]:
        """
        Brute force solution with O(n²) time complexity.
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return (i, j)
        return None

    def two_sum_hashmap(self, nums: List[int], target: int) -> Optional[Tuple[int, int]]:
        """
        Optimized solution using hashmap with O(n) time complexity.
        """
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return (num_map[complement], i)
            num_map[num] = i
        return None

    def two_sum_two_pointers(self, nums: List[int], target: int) -> Optional[Tuple[int, int]]:
        """
        Two pointers solution with O(n log n) time complexity.
        Note: This solution requires the array to be sorted.
        """
        nums_sorted = sorted(nums)
        left, right = 0, len(nums) - 1
        
        while left < right:
            current_sum = nums_sorted[left] + nums_sorted[right]
            if current_sum == target:
                # Find original indices
                original_left = nums.index(nums_sorted[left])
                original_right = nums.index(nums_sorted[right])
                if original_left == original_right:
                    original_right = nums.index(nums_sorted[right], original_left + 1)
                return (original_left, original_right)
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return None

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Test Case 1:")
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Brute Force: {solution.two_sum_brute_force(nums1, target1)}")
    print(f"Hashmap: {solution.two_sum_hashmap(nums1, target1)}")
    print(f"Two Pointers: {solution.two_sum_two_pointers(nums1, target1)}")
    print()
    
    # Test Case 2: Duplicate numbers
    nums2 = [3, 3]
    target2 = 6
    print("Test Case 2:")
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Brute Force: {solution.two_sum_brute_force(nums2, target2)}")
    print(f"Hashmap: {solution.two_sum_hashmap(nums2, target2)}")
    print(f"Two Pointers: {solution.two_sum_two_pointers(nums2, target2)}")
    print()
    
    # Test Case 3: No solution
    nums3 = [1, 2, 3, 4]
    target3 = 8
    print("Test Case 3:")
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Brute Force: {solution.two_sum_brute_force(nums3, target3)}")
    print(f"Hashmap: {solution.two_sum_hashmap(nums3, target3)}")
    print(f"Two Pointers: {solution.two_sum_two_pointers(nums3, target3)}")
    print()
    
    # Test Case 4: Negative numbers
    nums4 = [-1, -2, -3, -4, -5]
    target4 = -8
    print("Test Case 4:")
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Brute Force: {solution.two_sum_brute_force(nums4, target4)}")
    print(f"Hashmap: {solution.two_sum_hashmap(nums4, target4)}")
    print(f"Two Pointers: {solution.two_sum_two_pointers(nums4, target4)}")

if __name__ == "__main__":
    test_solution() 