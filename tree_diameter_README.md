# Binary Tree Diameter

## Problem Description
Given a binary tree, find its diameter. The diameter of a binary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

## Examples

### Example 1: Balanced Tree
```
     1
    / \
   2   3
  / \
 4   5

Diameter: 3
Explanation: The longest path is [4,2,1,3] with 3 edges.
```

### Example 2: Long Path Not Through Root
```
       1
      / \
     2   3
    /     \
   4       5
  /         \
 6           7

Diameter: 4
Explanation: The longest path is [6,4,2,3,5,7] with 4 edges.
```

### Example 3: Linear Tree (Skewed)
```
     1
    /
   2
  /
 3
/
4

Diameter: 3
Explanation: The longest path is [4,3,2,1] with 3 edges.
```

## Solution Approach

The solution uses a recursive approach with the following key points:

1. For each node, we calculate:
   - Height of left subtree
   - Height of right subtree
   - Potential diameter through this node (left_height + right_height)

2. Key insights:
   - The diameter at any node is the sum of heights of its left and right subtrees
   - We need to keep track of the maximum diameter seen so far
   - The height of a node is 1 + max(left_height, right_height)

3. Implementation details:
   - Use a class variable to track maximum diameter
   - Recursive height calculation also updates diameter
   - Base case: empty node has height 0

## Time Complexity
- O(N) where N is the number of nodes in the tree
- We visit each node exactly once

## Space Complexity
- O(H) where H is the height of the tree
- This space is used by the recursion stack
- In worst case (skewed tree), this becomes O(N)
- In balanced tree, this becomes O(log N)

## Usage
```python
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Create solution object
solution = Solution()

# Calculate diameter
result = solution.diameterOfBinaryTree(root)  # Returns 2
```

## Test Cases
The implementation includes three test cases:
1. Balanced tree with diameter through root
2. Tree with longest path not passing through root
3. Linear (skewed) tree

Each test case demonstrates different scenarios:
- Different tree structures
- Different path configurations
- Edge cases (like skewed trees)

## Running the Tests
```bash
python tree_diameter.py
```

## Implementation Details

### Node Structure
Each node in the binary tree contains:
- Value
- Left child reference
- Right child reference

### Helper Functions
1. `build_test_tree1()`, `build_test_tree2()`, `build_test_tree3()`
   - Create different tree structures for testing
   - Include visual representations in comments

2. `print_tree()`
   - Prints the tree structure visually
   - Shows parent-child relationships
   - Makes it easy to verify test cases 