class SubarraySumEqualsK:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        Find the total number of subarrays whose sum equals k.
        
        Args:
            nums: List of integers
            k: Target sum
            
        Returns:
            int: Number of subarrays that sum to k
        """
        count = 0
        prefix_sum = 0
        # Initialize with prefix_sum 0 having frequency 1
        prefix_sum_counts = {0: 1}
        
        for num in nums:
            prefix_sum += num
            # If (prefix_sum - k) exists in the map, add its frequency to count
            if (prefix_sum - k) in prefix_sum_counts:
                count += prefix_sum_counts[prefix_sum - k]
            # Update the frequency of current prefix_sum
            prefix_sum_counts[prefix_sum] = prefix_sum_counts.get(prefix_sum, 0) + 1
            
        return count

def test_subarray_sum():
    # Test cases
    test_cases = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1, -1, 0], 0, 3),
        ([1], 1, 1),
        ([1, 2, 3, 4, 5], 9, 2),
        ([1, 2, 1, 2, 1], 3, 4),
        ([], 0, 0),
    ]
    
    solver = SubarraySumEqualsK()
    
    for nums, k, expected in test_cases:
        result = solver.subarraySum(nums, k)
        print(f"Input: nums = {nums}, k = {k}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_subarray_sum() 