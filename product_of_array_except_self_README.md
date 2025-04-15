# Product of Array Except Self

## Problem Description
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.

### Examples
1. Input: nums = [1,2,3,4]
   Output: [24,12,8,6]
   Explanation: 
   - answer[0] = 2 * 3 * 4 = 24
   - answer[1] = 1 * 3 * 4 = 12
   - answer[2] = 1 * 2 * 4 = 8
   - answer[3] = 1 * 2 * 3 = 6

2. Input: nums = [-1,1,0,-3,3]
   Output: [0,0,9,0,0]
   Explanation: 
   - answer[0] = 1 * 0 * -3 * 3 = 0
   - answer[1] = -1 * 0 * -3 * 3 = 0
   - answer[2] = -1 * 1 * -3 * 3 = 9
   - answer[3] = -1 * 1 * 0 * 3 = 0
   - answer[4] = -1 * 1 * 0 * -3 = 0

## Approach
The solution uses a two-pass approach:
1. First pass (left to right):
   - Calculate the product of all elements to the left of each element
   - Store these products in the answer array
2. Second pass (right to left):
   - Calculate the product of all elements to the right of each element
   - Multiply this with the existing value in the answer array
3. This approach avoids using division and maintains O(n) time complexity

## Time Complexity
- O(n) where n is the length of the array
- We make two passes through the array
- Each pass takes O(n) time

## Space Complexity
- O(1) if we don't count the output array
- O(n) if we count the output array
- We only use a constant amount of extra space for variables
- Overall: O(1) or O(n) depending on whether we count the output array 