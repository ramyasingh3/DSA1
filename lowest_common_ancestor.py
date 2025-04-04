class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def lowest_common_ancestor(root, p, q):
    """
    Find the lowest common ancestor of two nodes in a Binary Search Tree.
    
    Args:
        root: The root node of the BST
        p: The value of the first node
        q: The value of the second node
    
    Returns:
        The value of the lowest common ancestor node
    """
    # If root is None, return None
    if not root:
        return None
    
    # Get current node's value
    current_val = root.value
    
    # If both p and q are greater than current value,
    # LCA must be in the right subtree
    if p > current_val and q > current_val:
        return lowest_common_ancestor(root.right, p, q)
    
    # If both p and q are smaller than current value,
    # LCA must be in the left subtree
    elif p < current_val and q < current_val:
        return lowest_common_ancestor(root.left, p, q)
    
    # If one value is smaller and other is greater,
    # or if one of the values equals current value,
    # current node is the LCA
    else:
        return current_val

def build_bst():
    """Helper function to build a sample BST for testing"""
    # Create the following BST:
    #        6
    #      /   \
    #     2     8
    #    / \   / \
    #   0   4 7   9
    #      / \
    #     3   5
    
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    
    return root

# Test cases
if __name__ == "__main__":
    # Build the sample BST
    root = build_bst()
    
    # Test case 1: LCA of 2 and 8
    print("LCA of 2 and 8:", lowest_common_ancestor(root, 2, 8))  # Should print 6
    
    # Test case 2: LCA of 2 and 4
    print("LCA of 2 and 4:", lowest_common_ancestor(root, 2, 4))  # Should print 2
    
    # Test case 3: LCA of 3 and 5
    print("LCA of 3 and 5:", lowest_common_ancestor(root, 3, 5))  # Should print 4
    
    # Test case 4: LCA of 7 and 9
    print("LCA of 7 and 9:", lowest_common_ancestor(root, 7, 9))  # Should print 8 