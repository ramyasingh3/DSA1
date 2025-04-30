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

def is_anagram_sorting(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams using sorting.
    
    Args:
        s (str): First string
        t (str): Second string
        
    Returns:
        bool: True if strings are anagrams, False otherwise
    """
    # If lengths are different, they can't be anagrams
    if len(s) != len(t):
        return False
    
    # Sort both strings and compare
    return sorted(s) == sorted(t)

def is_anagram_hashmap(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams using a hash map.
    
    Args:
        s (str): First string
        t (str): Second string
        
    Returns:
        bool: True if strings are anagrams, False otherwise
    """
    # If lengths are different, they can't be anagrams
    if len(s) != len(t):
        return False
    
    # Create a dictionary to store character counts
    char_count = {}
    
    # Count characters in first string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Decrement counts for characters in second string
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return True

def is_anagram_array(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams using a character count array.
    This is the most efficient solution for lowercase English letters.
    
    Args:
        s (str): First string
        t (str): Second string
        
    Returns:
        bool: True if strings are anagrams, False otherwise
    """
    # If lengths are different, they can't be anagrams
    if len(s) != len(t):
        return False
    
    # Create a fixed-size array for character counts (assuming ASCII)
    char_count = [0] * 128
    
    # Count characters in first string
    for char in s:
        char_count[ord(char)] += 1
    
    # Decrement counts for characters in second string
    for char in t:
        char_count[ord(char)] -= 1
        if char_count[ord(char)] < 0:
            return False
    
    return True

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
        assert is_anagram_sorting(s, t) == expected, f"Sorting test failed for '{s}' and '{t}'"
        
        # Test hashmap approach
        assert is_anagram_hashmap(s, t) == expected, f"Hashmap test failed for '{s}' and '{t}'"
        
        # Test array approach
        assert is_anagram_array(s, t) == expected, f"Array test failed for '{s}' and '{t}'"
    
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
        print(f"Using sorting: {is_anagram_sorting(s, t)}")
        print(f"Using hashmap: {is_anagram_hashmap(s, t)}")
        print(f"Using array: {is_anagram_array(s, t)}") 