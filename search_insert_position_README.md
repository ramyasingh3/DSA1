# Search Insert Position

## Problem Description
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

## Examples
1. Target exists:
   ```
   Input: nums = [1, 3, 5, 6], target = 5
   Output: 2
   ```

2. Target doesn't exist:
   ```
   Input: nums = [1, 3, 5, 6], target = 2
   Output: 1
   ```

3. Target at end:
   ```
   Input: nums = [1, 3, 5, 6], target = 7
   Output: 4
   ```

## Solution Approaches

### 1. Binary Search (O(log n))
- Uses binary search to find position
- Time Complexity: O(log n)
- Space Complexity: O(1)
- Best for most cases

### 2. Linear Search (O(n))
- Uses linear search to find position
- Time Complexity: O(n)
- Space Complexity: O(1)
- Best for small arrays

### 3. Bisect Module (O(log n))
- Uses Python's bisect module
- Time Complexity: O(log n)
- Space Complexity: O(1)
- Best for Python-specific solutions

## Time Complexity
- Binary Search: O(log n)
- Linear Search: O(n)
- Bisect Module: O(log n)

## Space Complexity
- All approaches: O(1)

## Usage
```python
from search_insert_position import Solution

solution = Solution()
nums = [1, 3, 5, 6]
target = 2

# Using binary search
index = solution.search_insert_binary(nums, target)
print(f"Insert position: {index}")

# Using linear search
index = solution.search_insert_linear(nums, target)
print(f"Insert position: {index}")

# Using bisect module
index = solution.search_insert_bisect(nums, target)
print(f"Insert position: {index}")
```

## Common Applications
- Database indexing
- Search algorithms
- Insertion operations
- Range queries
- Interview preparation
- Algorithm design 