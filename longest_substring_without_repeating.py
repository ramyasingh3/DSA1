def lengthOfLongestSubstring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest substring without repeating characters
    """
    if not s:
        return 0
        
    char_pos = {}  # Store the last position of each character
    start = 0      # Start of current window
    max_length = 0 # Maximum length found so far
    
    for end, char in enumerate(s):
        # If we find a repeating character, update the start pointer
        if char in char_pos and char_pos[char] >= start:
            start = char_pos[char] + 1
        else:
            max_length = max(max_length, end - start + 1)
            
        char_pos[char] = end
        
    return max_length

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "abcabcbb"
    print(f"Input: {s1}")
    print(f"Output: {lengthOfLongestSubstring(s1)}")  # Expected: 3 ("abc")
    
    # Test case 2
    s2 = "bbbbb"
    print(f"\nInput: {s2}")
    print(f"Output: {lengthOfLongestSubstring(s2)}")  # Expected: 1 ("b")
    
    # Test case 3
    s3 = "pwwkew"
    print(f"\nInput: {s3}")
    print(f"Output: {lengthOfLongestSubstring(s3)}")  # Expected: 3 ("wke") 