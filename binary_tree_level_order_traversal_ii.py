from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_bottom(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform level order traversal of a binary tree from bottom to top.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        List of lists containing node values at each level, from bottom to top
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result[::-1]  # Reverse the result to get bottom-up order

def list_to_tree(lst: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Convert a list representation to a binary tree.
    The list is in level-order traversal (breadth-first) order.
    None values represent null nodes.
    """
    if not lst or lst[0] is None:
        return None
    
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    
    while queue and i < len(lst):
        node = queue.pop(0)
        
        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    
    return root

def test_level_order_bottom():
    """Test cases for the binary tree level order traversal II solution."""
    
    test_cases = [
        # Basic cases
        ([3, 9, 20, None, None, 15, 7], [[15, 7], [9, 20], [3]]),
        ([1], [[1]]),
        
        # Edge cases
        ([], []),
        ([1, 2, None], [[2], [1]]),
        ([1, None, 2], [[2], [1]]),
        
        # Complete binary tree
        ([1, 2, 3, 4, 5, 6, 7], [[4, 5, 6, 7], [2, 3], [1]]),
        
        # Left-skewed tree
        ([1, 2, None, 3, None, 4], [[4], [3], [2], [1]]),
        
        # Right-skewed tree
        ([1, None, 2, None, None, None, 3], [[3], [2], [1]]),
        
        # Complex cases
        ([1, 2, 3, None, 4, 5, None, 6, None, None, 7], [[6, 7], [4, 5], [2, 3], [1]]),
        
        # Large tree
        (list(range(1, 16)), [[8, 9, 10, 11, 12, 13, 14, 15], [4, 5, 6, 7], [2, 3], [1]]),
        
        # Edge cases with None values
        ([1, None, 2, None, None, 3, None], [[3], [2], [1]]),
        ([1, 2, None, 3, None, None, None], [[3], [2], [1]]),
        
        # Mixed values
        ([10, 5, 15, 3, 7, 12, 20], [[3, 7, 12, 20], [5, 15], [10]]),
        
        # All negative numbers
        ([-1, -2, -3, -4, -5], [[-4, -5], [-2, -3], [-1]]),
        
        # Single negative number
        ([-1], [[-1]])
    ]
    
    print("Testing Binary Tree Level Order Traversal II Solution...")
    for tree_list, expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Get level order traversal from bottom
        result = level_order_bottom(root)
        
        print(f"\nInput: {tree_list}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_level_order_bottom() 