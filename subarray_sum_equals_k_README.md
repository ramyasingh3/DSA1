# Subarray Sum Equals K

## Problem Description
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`. A subarray is a contiguous non-empty sequence of elements within an array.

### Examples
1. Input: nums = [1,1,1], k = 2
   Output: 2
   Explanation: The subarrays [1,1] and [1,1] sum to 2.

2. Input: nums = [1,2,3], k = 3
   Output: 2
   Explanation: The subarrays [1,2] and [3] sum to 3.

3. Input: nums = [1,-1,0], k = 0
   Output: 3
   Explanation: The subarrays [1,-1], [-1,0], and [0] sum to 0.

## Approach
The solution uses a prefix sum technique with a hash map:
1. Keep track of the running sum (prefix sum) as we iterate through the array.
2. Use a hash map to store the frequency of each prefix sum encountered.
3. For each element, check if (current_sum - k) exists in the hash map.
4. If it exists, add its frequency to the result count.
5. Update the hash map with the current prefix sum.

## Time Complexity
- O(n) where n is the length of the array
- We traverse the array once, and hash map operations are O(1)

## Space Complexity
- O(n) for the hash map storing prefix sums
- In the worst case, we might need to store all prefix sums
- Overall: O(n) 