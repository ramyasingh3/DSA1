# Reverse Linked List

## Problem Description
Given the head of a singly linked list, reverse the list and return the reversed list.

### Examples
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []
```

## Approach
1. Initialize three pointers:
   - prev: points to the previous node (starts as None)
   - current: points to the current node (starts as head)
   - next: points to the next node
2. Iterate through the list:
   - Store the next node
   - Reverse the current node's pointer
   - Move prev and current one step forward
3. Return the new head (prev)

### Key Points
- In-place reversal
- O(1) space complexity
- Handles empty list
- Maintains list integrity

## Time Complexity
- O(n) where n is the length of the list
  - We traverse the list exactly once

## Space Complexity
- O(1) constant space
  - We only use pointers, no additional data structures 