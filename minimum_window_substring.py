def min_window(s, t):
    """
    Find the minimum window in s which will contain all the characters in t.
    Time Complexity: O(n)
    Space Complexity: O(k) where k is the number of unique characters
    """
    if not s or not t or len(s) < len(t):
        return ""
    
    # Create frequency map for string t
    target_freq = {}
    for char in t:
        target_freq[char] = target_freq.get(char, 0) + 1
    
    # Initialize variables
    left = 0
    min_len = float('inf')
    min_start = 0
    matched = 0
    window_freq = {}
    
    # Slide the window
    for right in range(len(s)):
        # Add current character to window
        char = s[right]
        window_freq[char] = window_freq.get(char, 0) + 1
        
        # If current character matches target frequency
        if char in target_freq and window_freq[char] == target_freq[char]:
            matched += 1
        
        # Try to minimize window size
        while matched == len(target_freq):
            # Update minimum window
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
            
            # Remove leftmost character
            left_char = s[left]
            window_freq[left_char] -= 1
            
            # If removed character was part of target
            if left_char in target_freq and window_freq[left_char] < target_freq[left_char]:
                matched -= 1
            
            left += 1
    
    return s[min_start:min_start + min_len] if min_len != float('inf') else ""

def main():
    # Test cases
    test_cases = [
        ("ADOBECODEBANC", "ABC"),  # Expected: "BANC"
        ("a", "a"),                # Expected: "a"
        ("a", "aa"),               # Expected: ""
        ("aa", "aa"),              # Expected: "aa"
        ("abc", "ac"),             # Expected: "abc"
        ("aab", "aab"),            # Expected: "aab"
    ]
    
    for s, t in test_cases:
        result = min_window(s, t)
        print(f"Input: s = '{s}', t = '{t}'")
        print(f"Output: '{result}'")
        if result:
            print(f"Length of minimum window: {len(result)}\n")
        else:
            print("No valid window found\n")

if __name__ == "__main__":
    main() 