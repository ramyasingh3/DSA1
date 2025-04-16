from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists into one sorted list.
    
    Args:
        list1: First sorted linked list
        list2: Second sorted linked list
        
    Returns:
        Merged sorted linked list
    """
    # Create a dummy node to start the merged list
    dummy = ListNode()
    current = dummy
    
    # Traverse both lists
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach remaining elements
    current.next = list1 if list1 else list2
    
    return dummy.next

def list_to_linked_list(lst: list) -> Optional[ListNode]:
    """Convert a Python list to a linked list."""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> list:
    """Convert a linked list to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_merge_two_lists():
    """Test cases for the merge two lists solution."""
    
    test_cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([1], [], [1]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6])
    ]
    
    print("Testing Merge Two Sorted Lists Solution...")
    for list1, list2, expected in test_cases:
        # Convert lists to linked lists
        l1 = list_to_linked_list(list1)
        l2 = list_to_linked_list(list2)
        
        # Merge lists
        merged = merge_two_lists(l1, l2)
        
        # Convert back to list for comparison
        result = linked_list_to_list(merged)
        
        print(f"\nInput: list1 = {list1}, list2 = {list2}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_merge_two_lists() 