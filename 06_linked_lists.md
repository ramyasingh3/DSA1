# Linked Lists

## Q1. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list `k` at a time and return the modified list.

`k` is a positive integer and is less than or equal to the length of the list. If the number of nodes is not a multiple of `k`, leave the remaining nodes as-is.

**Example**
```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

**Constraints**
- Do not alter node values — only change links
- Extra memory allowed is `O(1)` besides recursion (prefer iterative)

---

## Q2. Detect and Find Start of Cycle

Given the head of a linked list that may contain a cycle, return the node where the cycle begins. If there is no cycle, return `null`.

**Example**
```
Input: head = [3,2,0,-4], pos = 1
Output: node with value 2
Explanation: Tail connects to the node at index 1.
```

**Requirement:** Use Floyd's tortoise and hare — `O(1)` space, no modifying the list.

---

## Q3. Merge k Sorted Lists

You are given an array of `k` linked-lists `lists`, each sorted in ascending order. Merge all into one sorted linked list and return it.

**Example**
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

**Constraints**
- `0 ≤ k ≤ 10^4`
- Total number of nodes across all lists: `≤ 10^4`
- `-10^4 ≤ Node.val ≤ 10^4`

**Hint:** Min-heap of size `k`, or divide-and-conquer pairwise merges.
