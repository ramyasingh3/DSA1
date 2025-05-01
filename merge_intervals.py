def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals,
    and return an array of the non-overlapping intervals that cover all the intervals in the input.
    
    Args:
        intervals (list[list[int]]): List of intervals, where each interval is [start, end]
        
    Returns:
        list[list[int]]: List of merged intervals
    """
    if not intervals:
        return []
    
    # Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    current_interval = intervals[0]
    
    for next_interval in intervals[1:]:
        # If current interval overlaps with next interval
        if current_interval[1] >= next_interval[0]:
            # Merge intervals by taking the maximum end time
            current_interval[1] = max(current_interval[1], next_interval[1])
        else:
            # No overlap, add current interval to result and move to next
            merged.append(current_interval)
            current_interval = next_interval
    
    # Add the last interval
    merged.append(current_interval)
    
    return merged

def test_merge_intervals():
    """Test cases for merge intervals implementation"""
    test_cases = [
        # Basic cases
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        
        # Edge cases
        ([], []),
        ([[1, 4]], [[1, 4]]),
        
        # Overlapping cases
        ([[1, 4], [2, 3]], [[1, 4]]),
        ([[1, 4], [0, 4]], [[0, 4]]),
        
        # Multiple overlaps
        ([[1, 3], [2, 6], [8, 10], [15, 18], [16, 20]], [[1, 6], [8, 10], [15, 20]]),
        
        # Negative numbers
        ([[-4, -2], [-3, 0], [1, 3]], [[-4, 0], [1, 3]]),
    ]
    
    for input_intervals, expected in test_cases:
        result = merge_intervals(input_intervals)
        assert result == expected, f"Test failed for input {input_intervals}. Expected {expected}, got {result}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_merge_intervals()
    
    # Example usage
    example_intervals = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
        [[1, 4], [0, 4]],
        [[1, 3], [2, 6], [8, 10], [15, 18], [16, 20]],
    ]
    
    for intervals in example_intervals:
        result = merge_intervals(intervals)
        print(f"Input: {intervals}")
        print(f"Output: {result}\n") 