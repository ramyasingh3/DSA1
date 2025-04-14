# Longest Palindromic Substring

## Problem Description
Given a string `s`, return the longest palindromic substring in `s`.

A palindrome is a string that reads the same backward as forward.

## Examples

### Example 1:
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

### Example 2:
```
Input: s = "cbbd"
Output: "bb"
```

### Example 3:
```
Input: s = "a"
Output: "a"
```

## Approach
The solution uses dynamic programming to solve this problem efficiently. Here's how it works:

1. Create a 2D DP table where `dp[i][j]` represents whether the substring `s[i...j]` is a palindrome
2. Initialize the base cases:
   - All single characters are palindromes (`dp[i][i] = true`)
   - Two identical adjacent characters form a palindrome (`dp[i][i+1] = true` if `s[i] == s[i+1]`)
3. For substrings of length > 2:
   - A substring is a palindrome if the first and last characters are equal and the substring between them is a palindrome
   - `dp[i][j] = (s[i] == s[j]) && dp[i+1][j-1]`
4. Keep track of the longest palindrome found during the process

## Time Complexity
- O(n²), where n is the length of the input string
- We need to fill the DP table which has n² cells

## Space Complexity
- O(n²)
- We maintain a 2D DP table of size n x n

## Solution Code
The solution is implemented in `longest_palindromic_substring.py`. 