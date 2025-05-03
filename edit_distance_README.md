# Edit Distance (Levenshtein Distance)

## Problem Description
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

## Examples
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

## Constraints
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters

## Approach 1: Dynamic Programming
1. Create a 2D array `dp` where `dp[i][j]` represents the minimum number of operations to convert `word1[0:i]` to `word2[0:j]`
2. Initialize the first row and column:
   - dp[i][0] = i (delete all characters from word1)
   - dp[0][j] = j (insert all characters from word2)
3. For each position (i,j):
   - If characters match: dp[i][j] = dp[i-1][j-1]
   - If characters don't match: dp[i][j] = min(
     - dp[i-1][j-1] + 1 (replace)
     - dp[i-1][j] + 1 (delete)
     - dp[i][j-1] + 1 (insert)
   )
4. Return dp[m][n] where m and n are lengths of word1 and word2

## Approach 2: Recursion with Memoization
1. Define a recursive function that takes indices i and j
2. Base cases:
   - If i == 0: return j (insert all remaining characters)
   - If j == 0: return i (delete all remaining characters)
3. If characters match: return recursive call for (i-1, j-1)
4. If characters don't match: return min of:
   - Replace: recursive call for (i-1, j-1) + 1
   - Delete: recursive call for (i-1, j) + 1
   - Insert: recursive call for (i, j-1) + 1
5. Use memoization to avoid redundant calculations

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
- The solution can be extended to find the actual sequence of operations
- All three operations (insert, delete, replace) have equal cost
- The order of operations matters

## Common Applications
- Spell checking
- DNA sequence alignment
- Natural language processing
- Plagiarism detection
- File difference detection
- Speech recognition
- Machine translation

## Example Walkthrough
For word1 = "horse" and word2 = "ros":

### Dynamic Programming Approach:
1. Initialize dp table:
   ```
     r o s
   h 0 0 0
   o 0 0 0
   r 0 0 0
   s 0 0 0
   e 0 0 0
   ```
2. Fill the table:
   ```
     r o s
   h 1 2 3
   o 2 1 2
   r 1 2 3
   s 2 2 2
   e 3 3 3
   ```
3. Result: 3

### Recursive Approach:
1. Compare 'e' and 's': no match, take min of:
   - Replace: 1 + edit_distance("hors", "ro")
   - Delete: 1 + edit_distance("hors", "ros")
   - Insert: 1 + edit_distance("horse", "ro")
2. Continue recursively until base cases
3. Result: 3

## Finding the Actual Operations
To find the sequence of operations:
1. Start from dp[m][n]
2. If characters match, move diagonally
3. If characters don't match:
   - If dp[i][j] == dp[i-1][j-1] + 1: replace
   - If dp[i][j] == dp[i-1][j] + 1: delete
   - If dp[i][j] == dp[i][j-1] + 1: insert
4. Continue until reaching dp[0][0] 