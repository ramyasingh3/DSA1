from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list.
    
    Args:
        head: Head of the linked list to reverse
        
    Returns:
        Head of the reversed linked list
    """
    prev = None
    current = head
    
    while current:
        # Store next node
        next_node = current.next
        # Reverse the link
        current.next = prev
        # Move pointers forward
        prev = current
        current = next_node
    
    return prev

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

def test_reverse_list():
    """Test cases for the reverse list solution."""
    
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [3, 2, 1]),
        ([1, 1, 2, 2], [2, 2, 1, 1])
    ]
    
    print("Testing Reverse Linked List Solution...")
    for input_list, expected in test_cases:
        # Convert list to linked list
        head = list_to_linked_list(input_list)
        
        # Reverse the list
        reversed_head = reverse_list(head)
        
        # Convert back to list for comparison
        result = linked_list_to_list(reversed_head)
        
        print(f"\nInput: {input_list}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_reverse_list() 