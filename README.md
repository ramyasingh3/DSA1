# Lowest Common Ancestor in Binary Search Tree

## Problem Description
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in the tree that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).

## Example
```
Given the following binary search tree:
        6
      /   \
     2     8
    / \   / \
   0   4 7   9
      / \
     3   5

Input: p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Input: p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself.
```

## Solution Approach
The solution takes advantage of the BST property where all values in the left subtree are smaller than the current node, and all values in the right subtree are larger.

1. Start from the root node
2. If both values are greater than current node, move to right subtree
3. If both values are smaller than current node, move to left subtree
4. If one value is smaller and other is greater (or equal), current node is the LCA

## Time Complexity
- O(h) where h is the height of the tree
- In a balanced BST, this becomes O(log n) where n is the number of nodes
- In worst case (skewed tree), it becomes O(n)

## Space Complexity
- O(h) for the recursive call stack
- In a balanced BST, this becomes O(log n)
- In worst case (skewed tree), it becomes O(n)

## Usage
```python
# Create a BST
root = build_bst()  # Creates a sample BST for testing

# Find LCA of two nodes
result = lowest_common_ancestor(root, 2, 8)  # Returns 6
```

## Running the Tests
```bash
python lowest_common_ancestor.py
```

This will run the test cases included in the file and print the results. 