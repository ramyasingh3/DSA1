# Roman to Integer

## Problem Description
Given a roman numeral, convert it to an integer. Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Roman numerals are usually written largest to smallest from left to right. However, there are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

## Examples
1. Simple case:
   ```
   Input: s = "III"
   Output: 3
   Explanation: III = 1 + 1 + 1 = 3
   ```

2. Subtraction case:
   ```
   Input: s = "IV"
   Output: 4
   Explanation: IV = 5 - 1 = 4
   ```

3. Complex case:
   ```
   Input: s = "MCMXCIV"
   Output: 1994
   Explanation: M = 1000, CM = 900, XC = 90, IV = 4
   ```

## Solution Approaches

### 1. Dictionary-based Solution (O(n))
- Uses a dictionary to map symbols to values
- Processes string from right to left
- Time Complexity: O(n)
- Space Complexity: O(1)
- More elegant and maintainable
- Better for understanding the logic

### 2. If-else based Solution (O(n))
- Uses if-else statements to handle each case
- Processes string from left to right
- Time Complexity: O(n)
- Space Complexity: O(1)
- More straightforward but verbose
- Good for learning the rules

## Time Complexity
- Dictionary-based: O(n)
- If-else based: O(n)

## Space Complexity
- Dictionary-based: O(1)
- If-else based: O(1)

## Usage
```python
from roman_to_integer import Solution

solution = Solution()
s = "MCMXCIV"

# Using dictionary-based solution
result = solution.roman_to_int_dict(s)
print(f"Integer value: {result}")

# Using if-else based solution
result = solution.roman_to_int_if(s)
print(f"Integer value: {result}")
```

## Common Applications
- Historical document processing
- Clock face design
- Book chapter numbering
- Movie release years
- Monument inscriptions 