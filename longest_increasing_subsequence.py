def length_of_lis(nums: list[int]) -> int:
    """
    Find the length of the longest strictly increasing subsequence.
    
    Args:
        nums (list[int]): List of integers
        
    Returns:
        int: Length of the longest increasing subsequence
    """
    if not nums:
        return 0
        
    n = len(nums)
    dp = [1] * n  # dp[i] represents the length of LIS ending at index i
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def main():
    # Test cases
    test_cases = [
        [10, 9, 2, 5, 3, 7, 101, 18],  # Expected: 4 (subsequence: [2,5,7,101])
        [0, 1, 0, 3, 2, 3],            # Expected: 4 (subsequence: [0,1,2,3])
        [7, 7, 7, 7, 7, 7, 7],         # Expected: 1 (subsequence: [7])
        [],                            # Expected: 0
        [1],                           # Expected: 1
    ]
    
    for nums in test_cases:
        result = length_of_lis(nums)
        print(f"Input: nums = {nums}")
        print(f"Output: {result}\n")

if __name__ == "__main__":
    main() 