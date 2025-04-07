# Longest Common Prefix

## Problem Description
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

## Examples
1. Basic case:
   ```
   Input: ["flower", "flow", "flight"]
   Output: "fl"
   ```

2. No common prefix:
   ```
   Input: ["dog", "racecar", "car"]
   Output: ""
   ```

3. Empty list:
   ```
   Input: []
   Output: ""
   ```

4. Single string:
   ```
   Input: ["a"]
   Output: "a"
   ```

5. All strings same:
   ```
   Input: ["abc", "abc", "abc"]
   Output: "abc"
   ```

## Solution Approaches

### 1. Vertical Scanning (O(S))
- Compare characters from top to bottom on each column
- Return the prefix when a mismatch is found
- S is the sum of all characters in all strings

### 2. Horizontal Scanning (O(S))
- Start with the first string as the prefix
- Compare with each subsequent string
- Reduce the prefix until a match is found
- S is the sum of all characters in all strings

### 3. Divide and Conquer (O(S))
- Split the problem into smaller subproblems
- Find common prefix of left and right halves
- Combine results recursively
- S is the sum of all characters in all strings

## Time Complexity
- All solutions: O(S)
- S is the sum of all characters in all strings

## Space Complexity
- Vertical Scanning: O(1)
- Horizontal Scanning: O(1)
- Divide and Conquer: O(m log n)
  - m is the length of the longest string
  - n is the number of strings

## Usage
```python
from longest_common_prefix import Solution

solution = Solution()
strs = ["flower", "flow", "flight"]

# Using vertical scanning
result = solution.longest_common_prefix_vertical(strs)
print(result)  # Output: "fl"

# Using horizontal scanning
result = solution.longest_common_prefix_horizontal(strs)
print(result)  # Output: "fl"

# Using divide and conquer
result = solution.longest_common_prefix_divide(strs)
print(result)  # Output: "fl"
```

## Common Applications
- String matching
- Text processing
- File system operations
- DNA sequence analysis
- Data compression 