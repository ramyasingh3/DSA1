def threeSum(nums: list[int]) -> list[list[int]]:
    """
    Find all unique triplets in the array which gives the sum of zero.
    
    Args:
        nums: List of integers
        
    Returns:
        List of lists containing unique triplets that sum to zero
    """
    if len(nums) < 3:
        return []
        
    nums.sort()  # Sort the array to handle duplicates
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for i
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for right
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
                
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
                
    return result

# Example usage
if __name__ == "__main__":
    # Test case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"Input: {nums1}")
    print(f"Output: {threeSum(nums1)}")  # Expected: [[-1, -1, 2], [-1, 0, 1]]
    
    # Test case 2
    nums2 = []
    print(f"\nInput: {nums2}")
    print(f"Output: {threeSum(nums2)}")  # Expected: []
    
    # Test case 3
    nums3 = [0]
    print(f"\nInput: {nums3}")
    print(f"Output: {threeSum(nums3)}")  # Expected: [] 