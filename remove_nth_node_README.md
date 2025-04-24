# Remove Nth Node From End of List

## Problem Statement
Given the `head` of a linked list, remove the `n-th` node from the end of the list and return its head.

### Example 1:
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

### Example 2:
```
Input: head = [1], n = 1
Output: []
```

### Example 3:
```
Input: head = [1,2], n = 1
Output: [1]
```

## Approach
The solution uses a two-pointer technique:
1. Create a dummy node that points to the head (helps handle edge cases)
2. Initialize two pointers, fast and slow, both pointing to the dummy node
3. Move the fast pointer n+1 steps ahead
4. Move both pointers until fast reaches the end
5. The slow pointer will be at the node before the one to be removed
6. Remove the nth node by updating the next pointer
7. Return dummy.next (the new head)

## Time Complexity
- O(L), where L is the length of the linked list
- We traverse the list exactly once

## Space Complexity
- O(1)
- We only use constant extra space for the pointers
- The removal is done in-place 