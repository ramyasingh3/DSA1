# Longest Palindromic Substring

## Problem Description
Given a string `s`, return the longest palindromic substring in `s`.

A palindrome is a string that reads the same backward as forward, e.g., "madam" or "racecar".

## Examples
```
Input: s = "babad"
Output: "bab" or "aba"
Explanation: Both "bab" and "aba" are valid answers.

Input: s = "cbbd"
Output: "bb"
Explanation: "bb" is the longest palindromic substring.

Input: s = "a"
Output: "a"
Explanation: The single character is a palindrome.
```

## Constraints
- 1 <= s.length <= 1000
- s consists only of lowercase and/or uppercase English letters

## Approach 1: Dynamic Programming
1. Create a 2D boolean array `dp` where `dp[i][j]` represents whether the substring `s[i:j+1]` is a palindrome
2. Initialize the diagonal elements (single characters) as true
3. Check for substrings of length 2
4. For substrings of length > 2, use the recurrence relation:
   - If s[i] == s[j] and dp[i+1][j-1] is true, then dp[i][j] is true
5. Keep track of the longest palindrome found

## Approach 2: Expand Around Center
1. For each character in the string, consider it as the center of a palindrome
2. Expand outward in both directions while the characters match
3. Handle both odd-length (single center) and even-length (two centers) palindromes
4. Keep track of the longest palindrome found

## Time and Space Complexity
### Approach 1 (Dynamic Programming)
- Time Complexity: O(n²)
  - We need to fill the n×n DP table
- Space Complexity: O(n²)
  - We need to store the n×n DP table

### Approach 2 (Expand Around Center)
- Time Complexity: O(n²)
  - For each character, we may expand up to n/2 times
- Space Complexity: O(1)
  - We only use a constant amount of extra space

## Key Points
- This is a classic string manipulation problem
- The DP approach is more intuitive but uses more space
- The expand around center approach is more space-efficient
- Both approaches handle edge cases (empty string, single character)
- The solution must consider both odd and even length palindromes

## Common Applications
- DNA sequence analysis
- Text processing
- Pattern matching
- Natural language processing
- Data compression
- Security (palindrome-based encryption)

## Example Walkthrough
For s = "babad":

### Dynamic Programming Approach:
1. Initialize dp table with single characters:
   ```
   b a b a d
   b T F F F F
   a   T F F F
   b     T F F
   a       T F
   d         T
   ```
2. Check length 2:
   ```
   b a b a d
   b T F T F F
   a   T F T F
   b     T F F
   a       T F
   d         T
   ```
3. Check length > 2:
   ```
   b a b a d
   b T F T F F
   a   T F T F
   b     T F F
   a       T F
   d         T
   ```
4. Result: "bab" or "aba"

### Expand Around Center Approach:
1. Center at 'b': expand to "b"
2. Center at 'a': expand to "aba"
3. Center at 'b': expand to "bab"
4. Center at 'a': expand to "a"
5. Center at 'd': expand to "d"
6. Result: "bab" or "aba"

## Solution Code
The solution is implemented in `longest_palindromic_substring.py`. 