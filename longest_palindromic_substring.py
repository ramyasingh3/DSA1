def longest_palindrome(s):
    """
    Find the longest palindromic substring in the given string.
    
    Args:
        s (str): Input string
        
    Returns:
        str: Longest palindromic substring
    """
    if not s:
        return ""
        
    n = len(s)
    # Initialize DP table
    dp = [[False] * n for _ in range(n)]
    
    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True
    
    start = 0
    max_length = 1
    
    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check for substrings of length > 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length
    
    return s[start:start + max_length]

# Test cases
def test_longest_palindrome():
    # Example 1
    s1 = "babad"
    result1 = longest_palindrome(s1)
    assert result1 == "bab" or result1 == "aba"
    
    # Example 2
    s2 = "cbbd"
    assert longest_palindrome(s2) == "bb"
    
    # Example 3
    s3 = "a"
    assert longest_palindrome(s3) == "a"
    
    # Additional test cases
    s4 = "racecar"
    assert longest_palindrome(s4) == "racecar"
    
    s5 = "abacdfgdcaba"
    assert longest_palindrome(s5) == "aba"
    
    s6 = ""
    assert longest_palindrome(s6) == ""
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome() 