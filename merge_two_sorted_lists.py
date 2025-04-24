from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merge two sorted linked lists and return it as a sorted list.
    
    Args:
        list1 (ListNode): Head of the first sorted linked list
        list2 (ListNode): Head of the second sorted linked list
        
    Returns:
        ListNode: Head of the merged sorted linked list
    """
    # Create a dummy node to serve as the starting point
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
    
    # Append the remaining nodes from the non-empty list
    current.next = list1 if list1 else list2
    
    return dummy.next

def create_linked_list(values):
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Helper function to convert a linked list to a list"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    list1 = create_linked_list([1,2,4])
    list2 = create_linked_list([1,3,4])
    merged = mergeTwoLists(list1, list2)
    print(f"Input: list1 = [1,2,4], list2 = [1,3,4]")
    print(f"Output: {linked_list_to_list(merged)}")  # Expected: [1,1,2,3,4,4]
    
    # Test case 2
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = mergeTwoLists(list1, list2)
    print(f"\nInput: list1 = [], list2 = []")
    print(f"Output: {linked_list_to_list(merged)}")  # Expected: []
    
    # Test case 3
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = mergeTwoLists(list1, list2)
    print(f"\nInput: list1 = [], list2 = [0]")
    print(f"Output: {linked_list_to_list(merged)}")  # Expected: [0] 