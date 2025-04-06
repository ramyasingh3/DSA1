# Binary Tree Right Side View

## Problem Description
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom. This problem also includes a variant for the left side view.

## Examples

### Example 1: Right-leaning Tree
```
    1
   / \
  2   3
   \   \
    5   4
```
Right side view: [1, 3, 4]
Left side view: [1, 2, 5]

### Example 2: Left-leaning Tree
```
    1
   / \
  2   3
 /   /
4   5
```
Right side view: [1, 3, 5]
Left side view: [1, 2, 4]

### Example 3: Left-skewed Tree
```
    1
   /
  2
 /
3
```
Right side view: [1, 2, 3]
Left side view: [1, 2, 3]

## Solution Approach
The solution uses a breadth-first search (BFS) approach with the following key points:

1. **Level Order Traversal**:
   - Use a queue to process nodes level by level
   - Track the number of nodes at each level
   - For right side view: Capture the last node of each level
   - For left side view: Capture the first node of each level

2. **Key Steps**:
   - Initialize queue with root node
   - For each level:
     - Process all nodes at current level
     - Add the last/first node to result list
     - Add children to queue for next level

3. **Time Complexity**: O(N), where N is the number of nodes in the tree
   - Each node is visited exactly once

4. **Space Complexity**: O(W), where W is the maximum width of the tree
   - In worst case: O(N) for a complete binary tree
   - In best case: O(1) for a skewed tree

## Usage
```python
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Create Solution instance
solution = Solution()

# Get right and left side views
right_view = solution.rightSideView(root)
left_view = solution.leftSideView(root)

print(f"Right side view: {right_view}")
print(f"Left side view: {left_view}")
```

## Test Cases
The implementation includes three test cases:

1. **Right-leaning Tree**:
   - Tests right side view with right-leaning structure
   - Expected right view: [1, 3, 4]
   - Expected left view: [1, 2, 5]

2. **Left-leaning Tree**:
   - Tests right side view with left-leaning structure
   - Expected right view: [1, 3, 5]
   - Expected left view: [1, 2, 4]

3. **Left-skewed Tree**:
   - Tests right side view with left-skewed structure
   - Expected right view: [1, 2, 3]
   - Expected left view: [1, 2, 3]

## Running the Tests
```bash
python right_side_view.py
```

## Implementation Details
The implementation includes:
1. `TreeNode` class for creating binary tree nodes
2. `Solution` class with two methods:
   - `rightSideView`: Returns right side view of the tree
   - `leftSideView`: Returns left side view of the tree
3. Helper functions:
   - `print_tree`: Visualizes the tree structure
   - `build_test_tree*`: Creates test trees
4. Comprehensive test cases with visual output

## Common Applications
- Tree visualization
- UI rendering of hierarchical data
- Level-based tree analysis
- Tree structure debugging 