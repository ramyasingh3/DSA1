# Two Sum

## Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Examples
1. Basic case:
   ```
   Input: nums = [2, 7, 11, 15], target = 9
   Output: (0, 1)
   Explanation: Because nums[0] + nums[1] == 9, we return (0, 1).
   ```

2. Duplicate numbers:
   ```
   Input: nums = [3, 3], target = 6
   Output: (0, 1)
   ```

3. No solution:
   ```
   Input: nums = [1, 2, 3, 4], target = 8
   Output: None
   ```

4. Negative numbers:
   ```
   Input: nums = [-1, -2, -3, -4, -5], target = -8
   Output: (2, 4)
   ```

## Solution Approaches

### 1. Brute Force (O(n²))
- Iterate through each element in the array
- For each element, iterate through the remaining elements
- Check if the sum equals the target
- Return the indices if found

### 2. Hashmap (O(n))
- Create a hashmap to store numbers and their indices
- For each number, calculate its complement (target - number)
- Check if the complement exists in the hashmap
- If found, return the indices
- Otherwise, add the current number to the hashmap

### 3. Two Pointers (O(n log n))
- Sort the array
- Use two pointers (left and right)
- Move pointers based on the sum compared to target
- Find original indices after finding the solution

## Time Complexity
- Brute Force: O(n²)
- Hashmap: O(n)
- Two Pointers: O(n log n)

## Space Complexity
- Brute Force: O(1)
- Hashmap: O(n)
- Two Pointers: O(n) for sorting

## Usage
```python
from two_sum import Solution

solution = Solution()
nums = [2, 7, 11, 15]
target = 9

# Using brute force
result = solution.two_sum_brute_force(nums, target)
print(result)  # Output: (0, 1)

# Using hashmap (recommended)
result = solution.two_sum_hashmap(nums, target)
print(result)  # Output: (0, 1)

# Using two pointers
result = solution.two_sum_two_pointers(nums, target)
print(result)  # Output: (0, 1)
```

## Common Applications
- Finding pairs in arrays
- Data validation
- Financial calculations
- Game development
- Cryptography 