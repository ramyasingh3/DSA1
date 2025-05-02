# Valid Parentheses

## Problem Description
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order
3. Every close bracket has a corresponding open bracket of the same type

## Examples
```
Input: s = "()"
Output: true
Explanation: The string contains a valid pair of parentheses.

Input: s = "()[]{}"
Output: true
Explanation: The string contains valid pairs of all three types of brackets.

Input: s = "(]"
Output: false
Explanation: The string contains an invalid pair of brackets.

Input: s = "([)]"
Output: false
Explanation: The brackets are not closed in the correct order.
```

## Constraints
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'

## Approach
1. Use a stack to keep track of opening brackets
2. When we encounter an opening bracket, push it onto the stack
3. When we encounter a closing bracket:
   - If the stack is empty, return false (no matching opening bracket)
   - If the top of stack doesn't match the closing bracket, return false
   - If it matches, pop the opening bracket from the stack
4. At the end, the stack should be empty (all brackets matched)

## Time and Space Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

## Solution
The solution uses a stack data structure to keep track of opening brackets. The key insights are:
1. We only need to store opening brackets in the stack
2. When we see a closing bracket, it must match the most recent opening bracket
3. We can use a dictionary to map closing brackets to their corresponding opening brackets

## Key Points
- The order of brackets matters
- Each closing bracket must match its most recent opening bracket
- The stack helps us maintain the order of brackets
- We need to handle edge cases (empty string, single bracket)
- The solution is efficient with O(n) time and space complexity

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