# Valid Parentheses

## Problem Description
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. A string is valid if:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order
3. Every close bracket has a corresponding open bracket of the same type

## Examples
1. Valid case:
   ```
   Input: "()"
   Output: true
   ```

2. Valid nested case:
   ```
   Input: "({[]})"
   Output: true
   ```

3. Invalid case:
   ```
   Input: "(]"
   Output: false
   ```

## Solution Approaches

### 1. Stack-based Solution (O(n))
- Use a stack to track opening brackets
- When encountering a closing bracket, check if it matches the top of stack
- Time Complexity: O(n)
- Space Complexity: O(n)
- Best for performance and clarity

### 2. String Replacement Solution (O(n^2))
- Repeatedly remove valid pairs until string is empty
- Time Complexity: O(n^2)
- Space Complexity: O(1)
- Best for understanding the problem

## Time Complexity
- Stack: O(n)
- Replace: O(n^2)

## Space Complexity
- Stack: O(n)
- Replace: O(1)

## Usage
```python
from valid_parentheses import Solution

solution = Solution()

# Using stack-based solution
print(solution.is_valid_stack("()"))  # Output: True
print(solution.is_valid_stack("(]"))  # Output: False

# Using replacement solution
print(solution.is_valid_replace("({[]})"))  # Output: True
print(solution.is_valid_replace("([)]"))    # Output: False
```

## Common Applications
- Syntax checking in compilers
- XML/HTML validation
- Code editor bracket matching
- Mathematical expression validation
- Configuration file validation 