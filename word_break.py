def wordBreak(s: str, wordDict: list[str]) -> bool:
    """
    Determine if a string can be segmented into a space-separated sequence of dictionary words.
    
    Args:
        s: Input string to be segmented
        wordDict: List of valid words
        
    Returns:
        True if the string can be segmented, False otherwise
    """
    n = len(s)
    dp = [False] * (n + 1)  # dp[i] represents if s[0:i] can be segmented
    dp[0] = True  # Empty string is always valid
    
    for i in range(1, n + 1):
        for j in range(i):
            # Check if substring s[j:i] is in wordDict and previous part is valid
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
                
    return dp[n]

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    print(f"Input: s = {s1}, wordDict = {wordDict1}")
    print(f"Output: {wordBreak(s1, wordDict1)}")  # Expected: True
    
    # Test case 2
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    print(f"\nInput: s = {s2}, wordDict = {wordDict2}")
    print(f"Output: {wordBreak(s2, wordDict2)}")  # Expected: True
    
    # Test case 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    print(f"\nInput: s = {s3}, wordDict = {wordDict3}")
    print(f"Output: {wordBreak(s3, wordDict3)}")  # Expected: False 