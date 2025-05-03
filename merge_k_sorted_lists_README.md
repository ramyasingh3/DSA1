# Merge K Sorted Lists

## Problem Description
You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

## Examples
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
Merging them into one sorted list:
1->1->2->3->4->4->5->6

Input: lists = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,4,5,6,7,8,9]
Explanation: The linked-lists are:
[
  1->2->3,
  4->5->6,
  7->8->9
]
Merging them into one sorted list:
1->2->3->4->5->6->7->8->9
```

## Constraints
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order
- The sum of lists[i].length will not exceed 10^4

## Approach 1: Min Heap
1. Create a min heap to store the first node of each list
2. For each list:
   - Push its first node into the heap if it exists
3. Create a dummy node to build the result list
4. While the heap is not empty:
   - Pop the node with minimum value
   - Add it to the result list
   - If the node has a next node, push it to the heap
5. Return the merged list

## Approach 2: Divide and Conquer
1. If there are 0 or 1 lists, return the appropriate result
2. Divide the lists into two halves
3. Recursively merge the two halves
4. Use the merge two sorted lists algorithm to combine the results
5. Return the final merged list

## Time and Space Complexity
### Approach 1 (Min Heap)
- Time Complexity: O(N log k)
  - N: total number of nodes
  - k: number of linked lists
  - log k: heap operations
- Space Complexity: O(k)
  - k: size of the heap

### Approach 2 (Divide and Conquer)
- Time Complexity: O(N log k)
  - N: total number of nodes
  - k: number of linked lists
  - log k: depth of recursion
- Space Complexity: O(log k)
  - log k: recursion stack depth

## Key Points
- This is a classic problem combining linked lists and heap/divide-and-conquer
- The heap approach is more intuitive but uses more space
- The divide-and-conquer approach is more space-efficient
- Both approaches handle edge cases (empty lists, null lists)
- The solution must maintain the sorted order

## Common Applications
- External sorting
- Database operations
- File merging
- Stream processing
- Distributed systems
- Big data processing

## Example Walkthrough
For lists = [[1,4,5],[1,3,4],[2,6]]:

### Min Heap Approach:
1. Initialize heap with [1,1,2]
2. Pop 1 from first list, push 4
3. Pop 1 from second list, push 3
4. Pop 2 from third list, push 6
5. Pop 3 from second list, push 4
6. Pop 4 from first list, push 5
7. Pop 4 from second list
8. Pop 5 from first list
9. Pop 6 from third list
10. Result: 1->1->2->3->4->4->5->6

### Divide and Conquer Approach:
1. Divide lists into [[1,4,5],[1,3,4]] and [[2,6]]
2. Merge first half: 1->1->3->4->4->5
3. Merge second half: 2->6
4. Merge results: 1->1->2->3->4->4->5->6 