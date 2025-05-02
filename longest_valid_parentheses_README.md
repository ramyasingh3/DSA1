# Longest Valid Parentheses

## Problem Description
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

## Examples
```
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Input: s = ""
Output: 0
Explanation: There is no valid parentheses substring.
```

## Constraints
- 0 <= s.length <= 3 * 10^4
- s[i] is '(', or ')'

## Approach
1. Use a stack to keep track of indices of parentheses
2. Initialize stack with -1 to handle edge cases
3. For each character:
   - If it's '(', push its index onto stack
   - If it's ')':
     - Pop the top element from stack
     - If stack becomes empty, push current index
     - Otherwise, calculate length of valid substring
4. Keep track of maximum length found

## Time and Space Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

## Solution
The solution uses a stack to keep track of indices. The key insights are:
1. We store indices in the stack instead of characters
2. We initialize stack with -1 to handle edge cases
3. When we find a valid pair, we calculate the length using the current index and the index at the top of stack
4. We update the maximum length whenever we find a longer valid substring

## Key Points
- We need to handle both valid and invalid substrings
- The solution must be efficient (O(n) time complexity)
- We need to handle edge cases (empty string, all invalid)
- The stack helps us keep track of valid substring boundaries
- We can have multiple valid substrings in the input

## Common Applications
- Syntax validation in compilers
- Code editor bracket matching
- Mathematical expression validation
- DNA sequence analysis
- Network protocol validation 