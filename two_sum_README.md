# Two Sum

## Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## Examples
1. Basic case:
   ```
   Input: nums = [2,7,11,15], target = 9
   Output: [0,1]
   Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
   ```

2. Multiple solutions:
   ```
   Input: nums = [3,2,4], target = 6
   Output: [1,2]
   ```

3. Negative numbers:
   ```
   Input: nums = [-1,-2,-3,-4,-5], target = -8
   Output: [2,4]
   ```

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