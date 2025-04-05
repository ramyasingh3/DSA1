class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        Calculate the diameter of a binary tree.
        The diameter is the length of the longest path between any two nodes in the tree.
        This path may or may not pass through the root.
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            The diameter of the tree
        """
        self.diameter = 0  # Global variable to store maximum diameter
        
        def height(node):
            if not node:
                return 0
            
            # Get heights of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update diameter if path through current node is longer
            # Diameter through current node = left_height + right_height
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return height of current node
            return max(left_height, right_height) + 1
        
        height(root)  # Calculate height and update diameter
        return self.diameter

def build_test_tree1():
    """
    Builds test tree 1:
         1
        / \
       2   3
      / \
     4   5
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root

def build_test_tree2():
    """
    Builds test tree 2:
           1
          / \
         2   3
        /     \
       4       5
      /         \
     6           7
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.right.right.right = TreeNode(7)
    return root

def build_test_tree3():
    """
    Builds test tree 3:
         1
        /
       2
      /
     3
    /
   4
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    return root

def print_tree(node, level=0, prefix="Root: "):
    """Helper function to print the tree structure"""
    if not node:
        return
    
    print("  " * level + prefix + str(node.value))
    if node.left or node.right:
        if node.left:
            print_tree(node.left, level + 1, "L--- ")
        if node.right:
            print_tree(node.right, level + 1, "R--- ")

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Balanced tree
    print("\nTest Case 1: Balanced tree")
    root1 = build_test_tree1()
    print("Tree structure:")
    print_tree(root1)
    print("Diameter:", solution.diameterOfBinaryTree(root1))  # Expected: 3
    
    # Test case 2: Long path not through root
    print("\nTest Case 2: Long path not through root")
    root2 = build_test_tree2()
    print("Tree structure:")
    print_tree(root2)
    print("Diameter:", solution.diameterOfBinaryTree(root2))  # Expected: 4
    
    # Test case 3: Linear tree (skewed)
    print("\nTest Case 3: Linear tree")
    root3 = build_test_tree3()
    print("Tree structure:")
    print_tree(root3)
    print("Diameter:", solution.diameterOfBinaryTree(root3))  # Expected: 3 