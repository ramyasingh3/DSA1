# Container With Most Water

## Problem Description
Given an integer array `height` of length `n`, where each element represents a vertical line at position `i` with height `height[i]`. Find two lines that together with the x-axis form a container that can hold the most water. Return the maximum amount of water a container can store.

### Examples
1. Input: height = [1,8,6,2,5,4,8,3,7]
   Output: 49
   Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

2. Input: height = [1,1]
   Output: 1
   Explanation: The two lines form a container with height 1 and width 1, resulting in an area of 1.

## Approach
The solution uses a two-pointer technique:
1. Initialize two pointers, one at the start (left) and one at the end (right) of the array.
2. Calculate the area between the two pointers: min(height[left], height[right]) * (right - left)
3. Move the pointer pointing to the shorter line inward, as moving the longer line cannot result in a larger area
4. Keep track of the maximum area found during the process
5. Continue until the pointers meet

## Time Complexity
- O(n) where n is the length of the array
- We only need to traverse the array once with two pointers
- Each element is visited at most once

## Space Complexity
- O(1)
- We only use a constant amount of extra space for variables
- No additional data structures are required 