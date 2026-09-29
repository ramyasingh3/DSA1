# Trees & BST

## Q1. Lowest Common Ancestor in a Binary Tree

Given a binary tree (not necessarily a BST) and two distinct nodes `p` and `q`, return their lowest common ancestor (LCA).

The LCA of two nodes is the deepest node that has both `p` and `q` as descendants (a node can be a descendant of itself).

**Example**
```
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

Input: p = 5, q = 1
Output: 3

Input: p = 5, q = 4
Output: 5
```

**Constraints**
- Number of nodes: `2 ≤ n ≤ 10^5`
- Node values are unique
- `p` and `q` both exist in the tree

---

## Q2. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid BST.

A valid BST means:
- Left subtree values are strictly less than the node's value
- Right subtree values are strictly greater than the node's value
- Both subtrees are also valid BSTs

**Example**
```
Input: [5,1,4,null,null,3,6]
Output: false
Explanation: 3 is in the right subtree of 5 but 3 < 5.
```

**Follow-up:** Solve with O(1) extra space (excluding recursion stack) using Morris traversal, or with an iterative inorder scan.

---

## Q3. Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge. A node appears at most once. The path does **not** need to pass through the root.

Return the maximum path sum of any non-empty path.

**Example**
```
Input: [-10,9,20,null,null,15,7]
Output: 42
Explanation: path 15 → 20 → 7
```

**Constraints**
- `1 ≤ n ≤ 3 * 10^4`
- `-1000 ≤ Node.val ≤ 1000`
