def max_product(nums):
    """
    Find the maximum product of any contiguous subarray in the given array.
    
    Args:
        nums (List[int]): Input array of integers
        
    Returns:
        int: Maximum product of any contiguous subarray
    """
    if not nums:
        return 0
        
    # Initialize variables
    max_product = min_product = result = nums[0]
    
    for num in nums[1:]:
        # If the current number is negative, swap max and min
        if num < 0:
            max_product, min_product = min_product, max_product
            
        # Update max and min products
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)
        
        # Update the overall result
        result = max(result, max_product)
    
    return result

# Test cases
def test_max_product():
    # Example 1
    nums1 = [2, 3, -2, 4]
    assert max_product(nums1) == 6
    
    # Example 2
    nums2 = [-2, 0, -1]
    assert max_product(nums2) == 0
    
    # Example 3
    nums3 = [-2, 3, -4]
    assert max_product(nums3) == 24
    
    # Additional test cases
    nums4 = [0, 2]
    assert max_product(nums4) == 2
    
    nums5 = [-2, -3, -4, -5]
    assert max_product(nums5) == 120
    
    nums6 = [1]
    assert max_product(nums6) == 1
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_max_product() 