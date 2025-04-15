class ContainerWithMostWater:
    def maxArea(self, height: list[int]) -> int:
        """
        Find the maximum area of water that can be contained between two vertical lines.
        
        Args:
            height: List of integers representing the height of vertical lines
            
        Returns:
            int: Maximum area of water that can be contained
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate current area
            current_height = min(height[left], height[right])
            current_width = right - left
            current_area = current_height * current_width
            
            # Update max area if current area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

def test_container_with_most_water():
    # Test cases
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([1, 2, 4, 3], 4),
        ([], 0),
        ([1], 0),
    ]
    
    solver = ContainerWithMostWater()
    
    for height, expected in test_cases:
        result = solver.maxArea(height)
        print(f"Input: height = {height}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_container_with_most_water() 