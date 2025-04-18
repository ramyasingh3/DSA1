from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    """
    Find all root-to-leaf paths in a binary tree.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        List of strings representing all root-to-leaf paths
    """
    if not root:
        return []
    
    paths = []
    
    def dfs(node: TreeNode, current_path: str) -> None:
        if not node.left and not node.right:
            paths.append(current_path + str(node.val))
            return
        
        if node.left:
            dfs(node.left, current_path + str(node.val) + "->")
        if node.right:
            dfs(node.right, current_path + str(node.val) + "->")
    
    dfs(root, "")
    return paths

def list_to_tree(lst: list) -> Optional[TreeNode]:
    """Convert a list representation to a binary tree."""
    if not lst:
        return None
        
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    
    while queue and i < len(lst):
        node = queue.pop(0)
        
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    
    return root

def test_binary_tree_paths():
    """Test cases for the binary tree paths solution."""
    
    test_cases = [
        # Basic cases
        ([1, 2, 3, None, 5], ["1->2->5", "1->3"]),
        ([1], ["1"]),
        ([], []),
        # Complete binary tree
        ([1, 2, 3, 4, 5, 6, 7], ["1->2->4", "1->2->5", "1->3->6", "1->3->7"]),
        # Left skewed tree
        ([1, 2, None, 3, None, 4], ["1->2->3->4"]),
        # Right skewed tree
        ([1, None, 2, None, 3, None, 4], ["1->2->3->4"]),
        # Complex cases
        ([5, 3, 6, 2, 4, None, None, 1], ["5->3->2->1", "5->3->4", "5->6"]),
        # Large tree
        (list(range(1, 16)), [
            "1->2->4->8", "1->2->4->9", "1->2->5->10", "1->2->5->11",
            "1->3->6->12", "1->3->6->13", "1->3->7->14", "1->3->7->15"
        ]),
        # Edge cases
        ([1, None, None], ["1"]),
        ([1, 2, None], ["1->2"]),
        # Mixed values
        ([10, 5, 15, 3, 7, 12, 20], ["10->5->3", "10->5->7", "10->15->12", "10->15->20"])
    ]
    
    print("Testing Binary Tree Paths Solution...")
    for tree_list, expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Get all root-to-leaf paths
        result = binary_tree_paths(root)
        
        print(f"\nInput: {tree_list}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if sorted(result) == sorted(expected) else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_binary_tree_paths() 