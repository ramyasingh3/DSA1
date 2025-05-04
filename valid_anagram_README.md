# Valid Anagram

## Problem Description
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples
```
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

Input: s = "", t = ""
Output: true

Input: s = "a", t = "a"
Output: true

Input: s = "ab", t = "ba"
Output: true
```

## Constraints
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters
- Follow-up: What if the inputs contain Unicode characters?

## Approach 1: Sorting
1. Sort both strings
2. Compare the sorted strings
3. If they are equal, the strings are anagrams

## Approach 2: Hashmap (Fixed-size Array)
1. Create a fixed-size array of size 26 (for lowercase English letters)
2. Count frequency of each character in s
3. Decrement count for each character in t
4. If any count becomes negative, return false
5. Return true if all counts are zero

## Approach 3: Counter
1. Use Python's Counter class
2. Compare the counters of both strings
3. If they are equal, the strings are anagrams

## Approach 4: Unicode Hashmap
1. Create a dictionary to store character frequencies
2. Count frequency of each character in s
3. Decrement count for each character in t
4. Remove characters with zero count
5. Return true if dictionary is empty

## Time and Space Complexity
### Approach 1 (Sorting)
- Time Complexity: O(n log n)
  - Sorting takes O(n log n) time
- Space Complexity: O(n)
  - We need to store the sorted strings

### Approach 2 (Hashmap)
- Time Complexity: O(n)
  - We process each character once
- Space Complexity: O(1)
  - We use a fixed-size array of size 26

### Approach 3 (Counter)
- Time Complexity: O(n)
  - We process each character once
- Space Complexity: O(1)
  - We use a fixed-size counter

### Approach 4 (Unicode)
- Time Complexity: O(n)
  - We process each character once
- Space Complexity: O(k)
  - k is the number of unique characters

## Key Points
- This is a classic string manipulation problem
- The hashmap approach is the most efficient for English letters
- We need to handle edge cases (empty strings, single characters)
- The order of characters doesn't matter
- We can extend the solution to handle Unicode characters
- The sorting approach is simpler but less efficient
- The counter approach is elegant but language-specific

## Common Applications
- Word games
- Text analysis
- Cryptography
- Data compression
- Pattern matching
- String processing
- Natural language processing

## Example Walkthrough
For s = "anagram", t = "nagaram":

### Hashmap Approach:
1. Create array: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
2. Count characters in s:
   - a: 3
   - n: 1
   - g: 1
   - r: 1
   - m: 1
3. Decrement counts for t:
   - n: 0
   - a: 2
   - g: 0
   - a: 1
   - r: 0
   - a: 0
   - m: 0
4. All counts are zero
Result: true

## Follow-up: Unicode Characters
To handle Unicode characters:
1. Use a dictionary instead of a fixed-size array
2. Store character frequencies as key-value pairs
3. Handle character deletion when count reaches zero
4. Check if dictionary is empty at the end

## Optimization Tips
1. Early return if lengths are different
2. Use a fixed-size array for English letters
3. Use a dictionary for Unicode characters
4. Implement parallel processing for large strings
5. Use bit manipulation for single character case
6. Cache frequently used character counts
7. Consider using a fixed-size array for small inputs 