"""
Valid Anagram Implementation

This file contains multiple implementations to check if two strings are valid anagrams.

Problem Statement:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.

Time Complexity: O(n) where n is the length of the strings
Space Complexity: O(1) for the optimal solution (using character count array)
"""

def is_anagram_sort(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams using sorting.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    return sorted(s) == sorted(t)

def is_anagram_hashmap(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams using a hashmap.
    Time Complexity: O(n)
    Space Complexity: O(1) since we only use a fixed-size array
    """
    if len(s) != len(t):
        return False
    
    # Create a fixed-size array to count character frequencies
    char_count = [0] * 26
    
    # Count characters in s
    for char in s:
        char_count[ord(char) - ord('a')] += 1
    
    # Decrement counts for characters in t
    for char in t:
        char_count[ord(char) - ord('a')] -= 1
        # If count becomes negative, t has more of this character
        if char_count[ord(char) - ord('a')] < 0:
            return False
    
    return True

def is_anagram_counter(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams using Counter.
    Time Complexity: O(n)
    Space Complexity: O(1) since we only use a fixed-size counter
    """
    from collections import Counter
    return Counter(s) == Counter(t)

def is_anagram_unicode(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams using a dictionary for Unicode characters.
    Time Complexity: O(n)
    Space Complexity: O(k) where k is the number of unique characters
    """
    if len(s) != len(t):
        return False
    
    # Create a dictionary to count character frequencies
    char_count = {}
    
    # Count characters in s
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Decrement counts for characters in t
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]
    
    return len(char_count) == 0

def test_valid_anagram():
    """Test cases for valid anagram implementations"""
    test_cases = [
        ("anagram", "nagaram", True),    # Valid anagram
        ("rat", "car", False),           # Not an anagram
        ("", "", True),                  # Empty strings
        ("a", "a", True),                # Single character
        ("a", "b", False),               # Different single characters
        ("hello", "olleh", True),        # Reversed string
        ("hello", "world", False),       # Different strings
        ("aab", "aba", True),            # Same characters, different order
        ("aab", "abb", False),           # Different character counts
    ]
    
    for s, t, expected in test_cases:
        # Test sorting approach
        assert is_anagram_sort(s, t) == expected, f"Sorting test failed for '{s}' and '{t}'"
        
        # Test hashmap approach
        assert is_anagram_hashmap(s, t) == expected, f"Hashmap test failed for '{s}' and '{t}'"
        
        # Test counter approach
        assert is_anagram_counter(s, t) == expected, f"Counter test failed for '{s}' and '{t}'"
        
        # Test unicode approach
        assert is_anagram_unicode(s, t) == expected, f"Unicode test failed for '{s}' and '{t}'"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_valid_anagram()
    
    # Example usage
    test_strings = [
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("", ""),
        ("hello", "olleh"),
        ("aab", "aba")
    ]
    
    print("\nTesting various string pairs:")
    for s, t in test_strings:
        print(f"\nStrings: '{s}' and '{t}'")
        print(f"Using sorting: {is_anagram_sort(s, t)}")
        print(f"Using hashmap: {is_anagram_hashmap(s, t)}")
        print(f"Using counter: {is_anagram_counter(s, t)}")
        print(f"Using unicode: {is_anagram_unicode(s, t)}") 