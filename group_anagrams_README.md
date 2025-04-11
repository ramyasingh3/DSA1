# Group Anagrams

## Problem Description
Given an array of strings `strs`, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples
1. Basic case:
   ```
   Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
   Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
   ```

2. Empty strings:
   ```
   Input: strs = ["", ""]
   Output: [["", ""]]
   ```

3. Single character strings:
   ```
   Input: strs = ["a", "a", "b", "c"]
   Output: [["a", "a"], ["b"], ["c"]]
   ```

## Solution Approaches

### 1. Sort-based Solution (O(n * k log k))
- Sorts each string and uses it as a key
- Time Complexity: O(n * k log k) where n is number of strings and k is max string length
- Space Complexity: O(n * k)
- Simple and intuitive
- Good for understanding anagram properties

### 2. Count-based Solution (O(n * k))
- Uses character counts as keys
- Time Complexity: O(n * k)
- Space Complexity: O(n * k)
- More efficient than sorting
- Good for learning frequency counting

### 3. Prime Number Solution (O(n * k))
- Uses prime number multiplication for unique keys
- Time Complexity: O(n * k)
- Space Complexity: O(n * k)
- Most efficient
- Good for learning mathematical properties

## Time Complexity
- Sort-based: O(n * k log k)
- Count-based: O(n * k)
- Prime-based: O(n * k)

## Space Complexity
- Sort-based: O(n * k)
- Count-based: O(n * k)
- Prime-based: O(n * k)

## Usage
```python
from group_anagrams import Solution

solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Using sort-based solution
result = solution.group_anagrams_sort(strs)
print(f"Grouped anagrams: {result}")

# Using count-based solution
result = solution.group_anagrams_count(strs)
print(f"Grouped anagrams: {result}")

# Using prime-based solution
result = solution.group_anagrams_prime(strs)
print(f"Grouped anagrams: {result}")
```

## Common Applications
- Text processing
- Word games
- Data organization
- Pattern matching
- Cryptography 