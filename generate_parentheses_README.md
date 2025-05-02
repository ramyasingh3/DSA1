# Generate Parentheses

## Problem Description
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Examples
```
Input: n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
Explanation: All combinations are valid parentheses.

Input: n = 1
Output: ["()"]
Explanation: Only one valid combination is possible.

Input: n = 2
Output: ["(())", "()()"]
Explanation: Two valid combinations are possible.
```

## Constraints
- 1 <= n <= 8

## Approach
1. Use backtracking to generate all valid combinations
2. Keep track of:
   - Current string being built
   - Number of opening parentheses used
   - Number of closing parentheses used
3. At each step:
   - Add an opening parenthesis if we haven't used all n pairs
   - Add a closing parenthesis if we have more opening than closing
4. When the string length reaches 2n, add it to the result

## Time and Space Complexity
- Time Complexity: O(4^n/sqrt(n))
- Space Complexity: O(4^n/sqrt(n))

## Solution
The solution uses backtracking with the following key insights:
1. We can only add a closing parenthesis if we have more opening than closing
2. We can add an opening parenthesis if we haven't used all n pairs
3. The final string must be of length 2n
4. Each combination must be valid (well-formed)

## Key Points
- The solution must generate all possible valid combinations
- We need to ensure parentheses are well-formed
- The order of generation doesn't matter
- We need to handle edge cases (n = 1)
- The solution uses backtracking for efficiency

## Common Applications
- Code generation
- Syntax tree construction
- Mathematical expression generation
- DNA sequence generation
- Combinatorial problem solving

## Example Walkthrough
For n = 2:
1. Start with empty string ""
2. Add "(" (open_count = 1)
3. Can add another "(" or ")"
4. If we add "(", get "(("
5. Must add ")" next, get "(()"
6. Must add ")" next, get "(())"
7. Or if we add ")" after first "(", get "()"
8. Can add "(" or ")" next
9. If we add "(", get "()("
10. Must add ")" next, get "()()" 