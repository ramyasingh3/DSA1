def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Find the length of the longest common subsequence between two strings.
    
    Args:
        text1 (str): First input string
        text2 (str): Second input string
        
    Returns:
        int: Length of the longest common subsequence
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

def main():
    # Test cases
    test_cases = [
        ("abcde", "ace"),  # Expected: 3 (ace)
        ("abc", "abc"),    # Expected: 3 (abc)
        ("abc", "def"),    # Expected: 0 (no common subsequence)
        ("", ""),          # Expected: 0 (empty strings)
    ]
    
    for text1, text2 in test_cases:
        result = longest_common_subsequence(text1, text2)
        print(f"Input: text1 = '{text1}', text2 = '{text2}'")
        print(f"Output: {result}\n")

if __name__ == "__main__":
    main() 