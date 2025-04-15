class ProductOfArrayExceptSelf:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Calculate the product of array except self for each element.
        
        Args:
            nums: List of integers
            
        Returns:
            list[int]: List where each element is the product of all elements except itself
        """
        n = len(nums)
        answer = [1] * n
        
        # First pass: calculate left products
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
            
        # Second pass: calculate right products and multiply with left products
        right_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
            
        return answer

def test_product_except_self():
    # Test cases
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([2, 3], [3, 2]),
        ([0, 0], [0, 0]),
        ([1, 0], [0, 1]),
        ([], []),
    ]
    
    solver = ProductOfArrayExceptSelf()
    
    for nums, expected in test_cases:
        result = solver.productExceptSelf(nums)
        print(f"Input: nums = {nums}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_product_except_self() 