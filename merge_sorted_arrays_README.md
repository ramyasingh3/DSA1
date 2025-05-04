# Merge Sorted Arrays

## Problem Description
You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to 0 and should be ignored.

## Examples
```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6].

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
```

## Constraints
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10^9 <= nums1[i], nums2[j] <= 10^9

## Approach 1: Two Pointers (In-place)
1. Initialize three pointers:
   - p1: points to the last element in nums1
   - p2: points to the last element in nums2
   - p: points to the last position in the merged array
2. Compare elements from both arrays and place the larger one at position p
3. Decrement the corresponding pointer
4. Continue until all elements are processed

## Approach 2: Extra Space
1. Create a copy of the first m elements of nums1
2. Initialize three pointers:
   - p1: points to the current element in nums1_copy
   - p2: points to the current element in nums2
   - p: points to the current position in nums1
3. Compare elements and place the smaller one in nums1
4. Copy any remaining elements

## Approach 3: Built-in Sort
1. Copy all elements from nums2 into nums1
2. Sort the entire array
Note: This approach is not recommended for interviews

## Time and Space Complexity
### Approach 1 (Two Pointers)
- Time Complexity: O(m + n)
  - We process each element once
- Space Complexity: O(1)
  - We only use a few pointers

### Approach 2 (Extra Space)
- Time Complexity: O(m + n)
  - We process each element once
- Space Complexity: O(m)
  - We need to store a copy of nums1

### Approach 3 (Sort)
- Time Complexity: O((m + n) * log(m + n))
  - We need to sort the entire array
- Space Complexity: O(1)
  - We only use a few variables

## Key Points
- This is a classic array manipulation problem
- The two pointers approach is the most efficient
- We need to handle edge cases (empty arrays)
- The order of elements matters
- We can extend the solution to merge k sorted arrays
- The extra space approach is simpler but less efficient
- The sort approach is not recommended for interviews

## Common Applications
- Merge sort algorithm
- Database operations
- File merging
- Data processing
- Memory management
- Cache management
- Stream processing

## Example Walkthrough
For nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3:

### Two Pointers Approach:
1. Initialize pointers:
   - p1 = 2 (points to 3)
   - p2 = 2 (points to 6)
   - p = 5 (points to last 0)
2. Compare 3 and 6:
   - Place 6 at position 5
   - Decrement p2 and p
3. Compare 3 and 5:
   - Place 5 at position 4
   - Decrement p2 and p
4. Compare 3 and 2:
   - Place 3 at position 3
   - Decrement p1 and p
5. Compare 2 and 2:
   - Place 2 at position 2
   - Decrement p2 and p
6. Compare 2 and 2:
   - Place 2 at position 1
   - Decrement p1 and p
7. Compare 1 and 2:
   - Place 2 at position 0
   - Decrement p2 and p
8. Copy remaining 1
Result: [1,2,2,3,5,6]

## Merging K Sorted Arrays
To merge k sorted arrays:
1. Use a min heap to store the first element of each array
2. Pop the smallest element and add it to the result
3. Push the next element from the same array into the heap
4. Repeat until all elements are processed

## Optimization Tips
1. Use early termination if possible
2. Pre-allocate space for the result
3. Use in-place merging when possible
4. Implement parallel processing for large arrays
5. Use binary search for finding insertion points
6. Cache frequently accessed elements
7. Consider using a fixed-size array for small inputs 