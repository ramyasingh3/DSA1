# Valid Palindrome

## Problem Description
Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases. A string is a palindrome when it reads the same backward as forward.

## Examples
1. Basic palindrome:
   ```
   Input: "A man, a plan, a canal: Panama"
   Output: true
   Explanation: "amanaplanacanalpanama" is a palindrome
   ```

2. Not a palindrome:
   ```
   Input: "race a car"
   Output: false
   Explanation: "raceacar" is not a palindrome
   ```

3. Empty string:
   ```
   Input: ""
   Output: true
   Explanation: An empty string is considered a palindrome
   ```

## Solution Approaches

### 1. Two Pointer (O(n))
- Use two pointers moving from both ends
- Skip non-alphanumeric characters
- Time Complexity: O(n)
- Space Complexity: O(n)
- Best overall solution

### 2. Reverse String (O(n))
- Create filtered string and compare with its reverse
- Time Complexity: O(n)
- Space Complexity: O(n)
- Most concise solution

### 3. Recursive (O(n))
- Recursively check outer characters
- Time Complexity: O(n)
- Space Complexity: O(n)
- Good for understanding recursion

## Time Complexity
All solutions: O(n), where n is the length of the string

## Space Complexity
All solutions: O(n), for storing the filtered string

## Usage
```python
from valid_palindrome import Solution

solution = Solution()
s = "A man, a plan, a canal: Panama"

# Using two pointer approach
result = solution.is_palindrome_two_pointer(s)
print(result)  # Output: True

# Using reverse string approach
result = solution.is_palindrome_reverse(s)
print(result)  # Output: True

# Using recursive approach
result = solution.is_palindrome_recursive(s)
print(result)  # Output: True
```

## Common Applications
- Text processing
- Natural language processing
- DNA sequence analysis
- Word games and puzzles
- Algorithm interviews 