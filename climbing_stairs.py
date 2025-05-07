def climb_stairs(n: int) -> int:
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Example usage
if __name__ == "__main__":
    print(climb_stairs(3))  # Output: 3
    print(climb_stairs(4))  # Output: 5
