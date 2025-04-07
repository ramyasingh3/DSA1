# Reverse Integer

## Problem Description
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ - 1], then return 0.

## Examples
1. Positive number:
   ```
   Input: 123
   Output: 321
   ```

2. Negative number:
   ```
   Input: -123
   Output: -321
   ```

3. Number with trailing zeros:
   ```
   Input: 120
   Output: 21
   ```

4. Overflow case:
   ```
   Input: 1534236469
   Output: 0
   ```

5. Single digit:
   ```
   Input: 5
   Output: 5
   ```

## Solution Approaches

### 1. String-based Solution (O(n))
- Convert the number to a string
- Reverse the string
- Convert back to integer
- Handle sign and overflow conditions

### 2. Number-based Solution (O(log n))
- Handle sign separately
- Extract digits one by one
- Build reversed number
- Check for overflow before each multiplication

## Time Complexity
- String Solution: O(n)
- Number Solution: O(log n)

## Space Complexity
- String Solution: O(n)
- Number Solution: O(1)

## Usage
```python
from reverse_integer import Solution

solution = Solution()
x = 123

# Using string solution
result = solution.reverse_string(x)
print(result)  # Output: 321

# Using number solution (recommended)
result = solution.reverse_number(x)
print(result)  # Output: 321
```

## Common Applications
- Number manipulation
- Data validation
- Cryptography
- Game development
- Mathematical computations 