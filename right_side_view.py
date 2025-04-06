class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> list:
        """
        Given a binary tree, imagine yourself standing on the right side of it,
        return the values of the nodes you can see ordered from top to bottom.
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            List of values visible from the right side
        """
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            # Number of nodes at current level
            level_size = len(queue)
            
            # Process all nodes at current level
            for i in range(level_size):
                node = queue.pop(0)
                
                # If it's the last node of the level, add to result
                if i == level_size - 1:
                    result.append(node.value)
                
                # Add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

    def leftSideView(self, root: TreeNode) -> list:
        """
        Given a binary tree, imagine yourself standing on the left side of it,
        return the values of the nodes you can see ordered from top to bottom.
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            List of values visible from the left side
        """
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            # Number of nodes at current level
            level_size = len(queue)
            
            # Process all nodes at current level
            for i in range(level_size):
                node = queue.pop(0)
                
                # If it's the first node of the level, add to result
                if i == 0:
                    result.append(node.value)
                
                # Add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

def build_test_tree1():
    """
    Builds test tree 1:
         1
        / \
       2   3
        \   \
         5   4
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    return root

def build_test_tree2():
    """
    Builds test tree 2:
         1
        / \
       2   3
      /   /
     4   5
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    return root

def build_test_tree3():
    """
    Builds test tree 3:
         1
        /
       2
      /
     3
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
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
    
    print("Test Case 1: Tree with right-leaning structure")
    root1 = build_test_tree1()
    print("Tree structure:")
    print_tree(root1)
    print(f"Right side view: {solution.rightSideView(root1)}")  # Expected: [1, 3, 4]
    print(f"Left side view: {solution.leftSideView(root1)}")    # Expected: [1, 2, 5]
    
    print("\nTest Case 2: Tree with left-leaning structure")
    root2 = build_test_tree2()
    print("Tree structure:")
    print_tree(root2)
    print(f"Right side view: {solution.rightSideView(root2)}")  # Expected: [1, 3, 5]
    print(f"Left side view: {solution.leftSideView(root2)}")    # Expected: [1, 2, 4]
    
    print("\nTest Case 3: Left-skewed tree")
    root3 = build_test_tree3()
    print("Tree structure:")
    print_tree(root3)
    print(f"Right side view: {solution.rightSideView(root3)}")  # Expected: [1, 2, 3]
    print(f"Left side view: {solution.leftSideView(root3)}")    # Expected: [1, 2, 3] 