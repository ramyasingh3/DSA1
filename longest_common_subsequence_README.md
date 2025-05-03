# Longest Common Subsequence (LCS)

## Problem Description
Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

## Examples
```
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no common subsequence.
```

## Constraints
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist only of lowercase English characters

## Approach 1: Dynamic Programming
1. Create a 2D array `dp` where `dp[i][j]` represents the length of LCS of `text1[0:i]` and `text2[0:j]`
2. Initialize the first row and column with 0
3. For each position (i,j):
   - If characters match: dp[i][j] = dp[i-1][j-1] + 1
   - If characters don't match: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
4. Return dp[m][n] where m and n are lengths of text1 and text2

## Approach 2: Recursion with Memoization
1. Define a recursive function that takes indices i and j
2. Base cases:
   - If i or j is 0, return 0
   - If characters match, return 1 + recursive call for (i-1, j-1)
   - If characters don't match, return max of recursive calls for (i-1, j) and (i, j-1)
3. Use memoization to avoid redundant calculations

## Time and Space Complexity
### Approach 1 (Dynamic Programming)
- Time Complexity: O(m*n)
  - We need to fill the m×n DP table
- Space Complexity: O(m*n)
  - We need to store the m×n DP table

### Approach 2 (Recursion with Memoization)
- Time Complexity: O(m*n)
  - Each state (i,j) is computed only once
- Space Complexity: O(m*n)
  - Space for memoization table
  - O(m+n) for recursion stack

## Key Points
- This is a classic dynamic programming problem
- The DP approach is more efficient than naive recursion
- The solution can be extended to find the actual LCS string
- The order of characters must be preserved
- Characters can be skipped but not reordered

## Common Applications
- DNA sequence alignment
- File difference detection
- Plagiarism detection
- Version control systems
- Spell checking
- Natural language processing

## Example Walkthrough
For text1 = "abcde" and text2 = "ace":

### Dynamic Programming Approach:
1. Initialize dp table:
   ```
     a b c d e
   a 0 0 0 0 0
   c 0 0 0 0 0
   e 0 0 0 0 0
   ```
2. Fill the table:
   ```
     a b c d e
   a 1 1 1 1 1
   c 1 1 2 2 2
   e 1 1 2 2 3
   ```
3. Result: 3 (LCS: "ace")

### Recursive Approach:
1. Compare 'e' and 'e': match, add 1
2. Compare 'd' and 'c': no match, take max
3. Compare 'c' and 'c': match, add 1
4. Compare 'b' and 'a': no match, take max
5. Compare 'a' and 'a': match, add 1
6. Result: 3 (LCS: "ace")

## Finding the Actual LCS String
To find the actual LCS string:
1. Start from dp[m][n]
2. If characters match, add to result and move diagonally
3. If characters don't match, move to the larger of dp[i-1][j] or dp[i][j-1]
4. Reverse the result to get the LCS string 