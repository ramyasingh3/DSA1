def min_distance_dp(word1: str, word2: str) -> int:
    """
    Find the minimum number of operations required to convert word1 to word2 using dynamic programming.
    Operations: insert, delete, or replace a character.
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    m, n = len(word1), len(word2)
    # dp[i][j] represents the minimum number of operations to convert word1[0:i] to word2[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j - 1] + 1,  # replace
                    dp[i - 1][j] + 1,      # delete
                    dp[i][j - 1] + 1       # insert
                )
    
    return dp[m][n]

def min_distance_recursive(word1: str, word2: str) -> int:
    """
    Find the minimum number of operations required to convert word1 to word2 using recursion with memoization.
    Time Complexity: O(m*n)
    Space Complexity: O(m*n) for memoization
    """
    m, n = len(word1), len(word2)
    memo = {}
    
    def edit_distance(i: int, j: int) -> int:
        if i == 0:
            return j
        if j == 0:
            return i
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if word1[i - 1] == word2[j - 1]:
            memo[(i, j)] = edit_distance(i - 1, j - 1)
        else:
            memo[(i, j)] = min(
                edit_distance(i - 1, j - 1) + 1,  # replace
                edit_distance(i - 1, j) + 1,      # delete
                edit_distance(i, j - 1) + 1       # insert
            )
        
        return memo[(i, j)]
    
    return edit_distance(m, n)

def get_edit_operations(word1: str, word2: str) -> list:
    """
    Find the sequence of operations required to convert word1 to word2.
    Returns a list of operations: ('replace', i, c), ('delete', i), or ('insert', i, c)
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j - 1] + 1,  # replace
                    dp[i - 1][j] + 1,      # delete
                    dp[i][j - 1] + 1       # insert
                )
    
    # Reconstruct the operations
    operations = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and word1[i - 1] == word2[j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            operations.append(('replace', i - 1, word2[j - 1]))
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            operations.append(('delete', i - 1))
            i -= 1
        else:
            operations.append(('insert', i, word2[j - 1]))
            j -= 1
    
    return list(reversed(operations))

def main():
    # Test cases
    test_cases = [
        ("horse", "ros"),        # Expected: 3
        ("intention", "execution"), # Expected: 5
        ("", ""),               # Expected: 0
        ("a", "b"),             # Expected: 1
        ("abc", "abc"),         # Expected: 0
        ("abc", "def"),         # Expected: 3
        ("kitten", "sitting"),  # Expected: 3
        ("sunday", "saturday"), # Expected: 3
    ]
    
    print("Testing Dynamic Programming solution:")
    for word1, word2 in test_cases:
        distance = min_distance_dp(word1, word2)
        operations = get_edit_operations(word1, word2)
        print(f"Word1: {word1}")
        print(f"Word2: {word2}")
        print(f"Edit distance: {distance}")
        print("Operations:")
        for op in operations:
            print(f"  {op}")
        print()
    
    print("\nTesting Recursive solution:")
    for word1, word2 in test_cases:
        distance = min_distance_recursive(word1, word2)
        print(f"Word1: {word1}")
        print(f"Word2: {word2}")
        print(f"Edit distance: {distance}")
        print()

if __name__ == "__main__":
    main() 