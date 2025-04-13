"""
Problem: String Compression

Implement a method to perform basic string compression using the counts of repeated characters.
If the compressed string would not become smaller than the original string, return the original string.

Example:
Input: "aabcccccaaa"
Output: "a2b1c5a3"

Input: "ab"
Output: "ab" (since "a1b1" is longer)

The string contains only uppercase and lowercase letters (a-z, A-Z).
"""

def compress_string(s: str) -> str:
    if not s:
        return s
    
    # First pass: calculate compressed length
    compressed_length = 0
    count = 1
    prev_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == prev_char:
            count += 1
        else:
            compressed_length += len(str(count)) + 1
            count = 1
            prev_char = s[i]
    
    # Add length for last character group
    compressed_length += len(str(count)) + 1
    
    # If compressed string would be longer or equal, return original
    if compressed_length >= len(s):
        return s
    
    # Second pass: build compressed string
    result = []
    count = 1
    prev_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == prev_char:
            count += 1
        else:
            result.append(prev_char + str(count))
            count = 1
            prev_char = s[i]
    
    # Add last character group
    result.append(prev_char + str(count))
    
    compressed = ''.join(result)
    return compressed if len(compressed) < len(s) else s

def test_string_compression():
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("ab", "ab"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("AABBCC", "AABBCC"),
        ("aaAAaa", "a2A2a2"),
        ("", ""),
        ("a", "a"),
        ("abcdefg", "abcdefg"),
        ("aaaaaaaaa", "a9"),
        ("aaabbaaa", "a3b2a3"),
    ]
    
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = compress_string(input_str)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}:")
        print(f"Input: '{input_str}'")
        print(f"Expected: '{expected}'")
        print(f"Got: '{result}'")
        print(f"Result: {status}")
        print("-" * 50)

if __name__ == "__main__":
    test_string_compression()
