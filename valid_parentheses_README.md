# Valid Parentheses

## Problem Description
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples
```
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
```

## Constraints
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'

## Approach 1: Stack-based Solution
1. Initialize an empty stack
2. For each character in the string:
   - If it's an opening bracket, push it onto the stack
   - If it's a closing bracket:
     - If stack is empty, return false
     - If top of stack doesn't match the closing bracket, return false
     - Pop the top of stack
3. Return true if stack is empty, false otherwise

## Approach 2: Counting Solution
1. Initialize a counter to 0
2. For each character in the string:
   - If it's an opening bracket, increment counter
   - If it's a closing bracket, decrement counter
   - If counter becomes negative, return false
3. Return true if counter is 0, false otherwise
Note: This approach only works for single type of brackets

## Approach 3: Regex Solution
1. Define a pattern matching valid pairs of brackets
2. Repeatedly remove valid pairs from the string
3. Return true if string becomes empty, false otherwise
Note: This approach is not recommended for production use

## Time and Space Complexity
### Approach 1 (Stack)
- Time Complexity: O(n)
  - We process each character once
- Space Complexity: O(n)
  - We need to store the stack

### Approach 2 (Counting)
- Time Complexity: O(n)
  - We process each character once
- Space Complexity: O(1)
  - We only use a single counter

### Approach 3 (Regex)
- Time Complexity: O(n²) in worst case
  - Each regex operation can take O(n) time
  - We may need to perform O(n) operations
- Space Complexity: O(n)
  - We need to store the modified string

## Key Points
- This is a classic stack-based problem
- The stack approach is the most general and efficient
- We need to handle edge cases (empty string, single bracket)
- The order of brackets matters
- We can extend the solution to generate all valid combinations
- The counting approach is simpler but limited
- The regex approach is elegant but inefficient

## Common Applications
- Code editors and IDEs
- Compiler design
- XML/HTML parsing
- JSON validation
- Mathematical expressions
- Configuration files
- Markup languages

## Example Walkthrough
For s = "([)]":

### Stack-based Approach:
1. Process '(':
   - Stack: ['(']
2. Process '[':
   - Stack: ['(', '[']
3. Process ')':
   - Top of stack is '[', doesn't match ')'
   - Return false

### Counting Approach (for single type):
1. Process '(':
   - Count: 1
2. Process ')':
   - Count: 0
3. Process '(':
   - Count: 1
4. Process ')':
   - Count: 0
5. Result: true (but incorrect for mixed types)

### Regex Approach:
1. Initial string: "([)]"
2. No valid pairs found
3. Result: false

## Generating All Valid Combinations
To generate all valid parentheses combinations for n pairs:
1. Use backtracking to build combinations
2. Keep track of open and close counts
3. Add opening bracket if open < n
4. Add closing bracket if close < open
5. Add to result when length = 2n

## Optimization Tips
1. Use early termination if possible
2. Pre-allocate stack space if size is known
3. Use bit manipulation for single type
4. Implement pruning in backtracking
5. Cache frequently used patterns
6. Use string builder for concatenation
7. Consider using a fixed-size array for stack 