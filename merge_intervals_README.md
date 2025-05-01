# Merge Intervals

## Problem Description
Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

## Examples
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Input: intervals = [[1,4],[0,4]]
Output: [[0,4]]
Explanation: Intervals [1,4] and [0,4] overlap, so they are merged into [0,4].
```

## Solution Approach
The solution uses sorting and a single pass through the intervals. Here's how it works:

1. Sort the intervals based on their start times
2. Initialize the result list and take the first interval as the current interval
3. For each subsequent interval:
   - If it overlaps with the current interval:
     - Merge them by updating the end time of the current interval
   - If it doesn't overlap:
     - Add the current interval to the result
     - Make the current interval the next interval
4. Add the last interval to the result

## Time and Space Complexity
- Time Complexity: O(n log n), where n is the number of intervals
  - Sorting takes O(n log n) time
  - The merge process takes O(n) time
- Space Complexity: O(n)
  - In the worst case, we need to store all intervals in the result list
  - The sorting algorithm may use O(n) extra space

## Implementation Details
The solution is implemented in `merge_intervals.py` with:
- Type hints for better code clarity
- Comprehensive test cases covering:
  - Basic overlapping cases
  - Edge cases (empty input, single interval)
  - Multiple overlapping intervals
  - Negative numbers
- Clear documentation and comments

## Common Applications
- Calendar scheduling
- Meeting room allocation
- Resource allocation
- Time series analysis
- Network bandwidth management
- Task scheduling
- Project timeline management 