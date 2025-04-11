# First Unique Character in a String

## Problem Description
Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

## Examples
1. Unique character exists:
   ```
   Input: s = "leetcode"
   Output: 0
   Explanation: 'l' is the first unique character.
   ```

2. No unique character:
   ```
   Input: s = "aabb"
   Output: -1
   Explanation: All characters are repeated.
   ```

3. First character is unique:
   ```
   Input: s = "loveleetcode"
   Output: 2
   Explanation: 'v' is the first unique character.
   ```

## Solution Approaches

### 1. Counter-based Solution (O(n))
- Uses Counter to track character frequencies
- Time Complexity: O(n)
- Space Complexity: O(1)
- Simple and efficient
- Uses built-in Counter class

### 2. Array-based Solution (O(n))
- Uses a fixed-size array to count characters
- Time Complexity: O(n)
- Space Complexity: O(1)
- Most efficient
- Good for learning character counting

### 3. Dictionary-based Solution (O(n))
- Uses a dictionary to track character frequencies
- Time Complexity: O(n)
- Space Complexity: O(1)
- More flexible
- Good for understanding hash maps

## Time Complexity
- Counter-based: O(n)
- Array-based: O(n)
- Dictionary-based: O(n)

## Space Complexity
- Counter-based: O(1)
- Array-based: O(1)
- Dictionary-based: O(1)

## Usage
```python
from first_unique_character import Solution

solution = Solution()
s = "leetcode"

# Using counter-based solution
result = solution.first_uniq_char_counter(s)
print(f"First unique character index: {result}")

# Using array-based solution
result = solution.first_uniq_char_array(s)
print(f"First unique character index: {result}")

# Using dictionary-based solution
result = solution.first_uniq_char_dict(s)
print(f"First unique character index: {result}")
```

## Common Applications
- Text processing
- Data validation
- Pattern matching
- String manipulation
- Character encoding 