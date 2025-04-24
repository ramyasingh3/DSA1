# Merge Two Sorted Lists

## Problem Statement
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

### Example 1:
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

### Example 2:
```
Input: list1 = [], list2 = []
Output: []
```

### Example 3:
```
Input: list1 = [], list2 = [0]
Output: [0]
```

## Approach
The solution uses a dummy node and two pointers:
1. Create a dummy node to serve as the starting point of the merged list
2. Use a current pointer to build the merged list
3. Compare the values of the current nodes in both lists:
   - Append the smaller value to the merged list
   - Move the pointer of the list from which we took the value
4. Continue until one of the lists is exhausted
5. Append the remaining nodes from the non-empty list
6. Return the head of the merged list (dummy.next)

## Time Complexity
- O(n + m), where n and m are the lengths of the two lists
- We process each node exactly once

## Space Complexity
- O(1)
- We only use a constant amount of extra space for the dummy node and pointers
- The merged list is created by rearranging the existing nodes 