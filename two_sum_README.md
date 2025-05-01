# Two Sum

## Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Examples
```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: Because nums[1] + nums[2] == 6, we return [1, 2]

Input: nums = [3, 3], target = 6
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 6, we return [0, 1]
```

## Solution Approach
The solution uses a hash map (dictionary) to achieve O(n) time complexity. Here's how it works:

1. Create a hash map to store number -> index mapping
2. For each number in the array:
   - Calculate the complement (target - current number)
   - If complement exists in the hash map:
     - Return the indices of complement and current number
   - Otherwise:
     - Store current number and its index in the hash map
3. If no solution is found, raise a ValueError

## Time and Space Complexity
- Time Complexity: O(n), where n is the length of the input array
  - We process each element exactly once
- Space Complexity: O(n), where n is the length of the input array
  - In the worst case, we store all elements in the hash map

## Alternative Approaches
1. Brute Force (O(n²) time, O(1) space):
   - Use two nested loops to check all possible pairs
   - Simple but inefficient for large arrays

2. Two Pointers (O(n log n) time, O(1) space):
   - Sort the array first
   - Use two pointers from start and end
   - Move pointers based on sum comparison
   - Note: This approach requires additional space to store original indices

## Implementation
The solution is implemented in `two_sum.py` with:
- Type hints for better code clarity
- Comprehensive error handling
- Detailed test cases
- Clear documentation

## Solution Approaches

### 1. Brute Force (O(n²))
- Check all possible pairs of numbers
- Time Complexity: O(n²)
- Space Complexity: O(1)
- Best for small arrays or understanding the problem

### 2. Hash Table (O(n))
- Use a hash table to store complements
- For each number, check if its complement exists
- Time Complexity: O(n)
- Space Complexity: O(n)
- Best for most practical cases

### 3. Sort and Two Pointers (O(n log n))
- Sort the array and use two pointers
- Move pointers based on sum comparison
- Time Complexity: O(n log n)
- Space Complexity: O(n)
- Best when array is already sorted

## Time Complexity
- Brute Force: O(n²)
- Hash Table: O(n)
- Sort and Two Pointers: O(n log n)

## Space Complexity
- Brute Force: O(1)
- Hash Table: O(n)
- Sort and Two Pointers: O(n)

## Usage
```python
from two_sum import Solution

solution = Solution()

# Using brute force
print(solution.two_sum_brute_force([2,7,11,15], 9))  # Output: (0, 1)

# Using hash table
print(solution.two_sum_hash([2,7,11,15], 9))  # Output: (0, 1)

# Using sort and two pointers
print(solution.two_sum_sort([2,7,11,15], 9))  # Output: (0, 1)
```

## Common Applications
- Finding pairs in data analysis
- Financial calculations
- Resource allocation
- Scheduling problems
- Network routing
- Database queries 