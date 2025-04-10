from typing import List

class Solution:
    def search_insert_binary(self, nums: List[int], target: int) -> int:
        """
        Binary search approach
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums)
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
                
        return left
        
    def search_insert_linear(self, nums: List[int], target: int) -> int:
        """
        Linear search approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
        
    def search_insert_bisect(self, nums: List[int], target: int) -> int:
        """
        Using bisect module
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        import bisect
        return bisect.bisect_left(nums, target)

def test_solution():
    solution = Solution()
    
    # Test Case 1: Target exists
    print("Test Case 1: Target exists")
    nums = [1, 3, 5, 6]
    target = 5
    result = solution.search_insert_binary(nums, target)
    print(f"Input: {nums}, target = {target}")
    print(f"Output: {result}")
    print()
    
    # Test Case 2: Target doesn't exist
    print("Test Case 2: Target doesn't exist")
    nums = [1, 3, 5, 6]
    target = 2
    result = solution.search_insert_binary(nums, target)
    print(f"Input: {nums}, target = {target}")
    print(f"Output: {result}")
    print()
    
    # Test Case 3: Target at end
    print("Test Case 3: Target at end")
    nums = [1, 3, 5, 6]
    target = 7
    result = solution.search_insert_binary(nums, target)
    print(f"Input: {nums}, target = {target}")
    print(f"Output: {result}")
    print()
    
    # Test Case 4: Target at beginning
    print("Test Case 4: Target at beginning")
    nums = [1, 3, 5, 6]
    target = 0
    result = solution.search_insert_binary(nums, target)
    print(f"Input: {nums}, target = {target}")
    print(f"Output: {result}")
    print()
    
    # Test Case 5: Empty array
    print("Test Case 5: Empty array")
    nums = []
    target = 5
    result = solution.search_insert_binary(nums, target)
    print(f"Input: {nums}, target = {target}")
    print(f"Output: {result}")
    print()
    
    # Test all methods
    print("Testing all methods:")
    nums = [1, 3, 5, 6]
    target = 2
    
    print("Binary Search:")
    result = solution.search_insert_binary(nums, target)
    print(f"Result: {result}")
    
    print("Linear Search:")
    result = solution.search_insert_linear(nums, target)
    print(f"Result: {result}")
    
    print("Bisect Module:")
    result = solution.search_insert_bisect(nums, target)
    print(f"Result: {result}")

if __name__ == "__main__":
    test_solution() 