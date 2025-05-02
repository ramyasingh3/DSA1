# Minimum Window Substring

## Problem Description
Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

## Examples
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window, but s only has one 'a'.
```

## Constraints
- 1 <= s.length, t.length <= 10^5
- s and t consist of uppercase and lowercase English letters

## Approach
1. Use sliding window technique with two pointers
2. Create frequency maps for both strings
3. Keep track of matched characters
4. Expand window by moving right pointer
5. Contract window by moving left pointer when all characters are matched
6. Update minimum window when a smaller valid window is found

## Time and Space Complexity
- Time Complexity: O(n) where n is the length of string s
- Space Complexity: O(k) where k is the number of unique characters

## Solution
The solution uses a sliding window approach with the following key insights:
1. We need to track frequency of characters in both strings
2. We can use a counter to track how many characters are matched
3. We can shrink the window when all characters are matched
4. We need to handle duplicate characters correctly
5. We need to update the minimum window when a smaller valid window is found

## Key Points
- The window must contain all characters from t
- The order of characters doesn't matter
- We need to handle duplicate characters
- The solution must be efficient (O(n) time complexity)
- We need to handle edge cases (empty strings, no valid window)

## Common Applications
- DNA sequence analysis
- Text search and indexing
- Pattern matching
- String processing
- Bioinformatics

## Example Walkthrough
For s = "ADOBECODEBANC", t = "ABC":
1. Start with empty window
2. Expand window until we find all characters
3. When all characters are found, try to minimize window
4. Keep track of minimum window found
5. Continue until we reach the end of string
6. Return the minimum window found 