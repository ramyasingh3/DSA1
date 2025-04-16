# Merge Two Sorted Lists

## Problem Description
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

### Examples
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
```

## Approach
1. Create a dummy node to serve as the starting point
2. Use a pointer to build the new list
3. Compare nodes from both lists and append the smaller one
4. Continue until one list is exhausted
5. Append the remaining nodes from the non-empty list

### Key Points
- In-place merging
- No extra space needed (except for pointers)
- Handles empty lists
- Maintains sorted order

## Time Complexity
- O(n + m) where n and m are lengths of the two lists
  - We traverse each list exactly once

## Space Complexity
- O(1) constant space
  - We only use pointers, no additional data structures 