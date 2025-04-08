# Palindrome Number

## Problem Description
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise. A palindrome number reads the same backward as forward.

## Examples
1. Positive palindrome:
   ```
   Input: x = 121
   Output: true
   ```

2. Negative number:
   ```
   Input: x = -121
   Output: false
   ```

3. Non-palindrome:
   ```
   Input: x = 10
   Output: false
   ```

## Solution Approaches

### 1. String Conversion (O(n))
- Convert number to string
- Compare with its reverse
- Time Complexity: O(n)
- Space Complexity: O(n)
- Best for readability

### 2. Half Number Comparison (O(log n))
- Compare first half with second half
- Handle even and odd length numbers
- Time Complexity: O(log n)
- Space Complexity: O(1)
- Best for performance

### 3. Full Number Reversal (O(log n))
- Reverse the entire number
- Compare with original
- Time Complexity: O(log n)
- Space Complexity: O(1)
- Best for understanding

## Time Complexity
- String: O(n)
- Half/Full: O(log n)

## Space Complexity
- String: O(n)
- Half/Full: O(1)

## Usage
```python
from palindrome_number import Solution

solution = Solution()

# Using string method
print(solution.is_palindrome_string(121))  # Output: True

# Using half comparison method
print(solution.is_palindrome_half(12321))  # Output: True

# Using full reversal method
print(solution.is_palindrome_reverse(10))  # Output: False
```

## Common Applications
- Number validation
- Data integrity checks
- Cryptography
- Game development
- Mathematical puzzles 