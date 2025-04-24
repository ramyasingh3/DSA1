class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    """
    Remove the nth node from the end of the list and return its head.
    
    Args:
        head (ListNode): Head of the linked list
        n (int): Position from the end to remove
        
    Returns:
        ListNode: Head of the modified linked list
    """
    # Create a dummy node that points to head
    dummy = ListNode(0, head)
    fast = slow = dummy
    
    # Move fast pointer n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next
    
    # Move both pointers until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next
    
    # Remove the nth node
    slow.next = slow.next.next
    
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
    head1 = create_linked_list([1,2,3,4,5])
    n1 = 2
    result1 = removeNthFromEnd(head1, n1)
    print(f"Input: head = [1,2,3,4,5], n = {n1}")
    print(f"Output: {linked_list_to_list(result1)}")  # Expected: [1,2,3,5]
    
    # Test case 2
    head2 = create_linked_list([1])
    n2 = 1
    result2 = removeNthFromEnd(head2, n2)
    print(f"\nInput: head = [1], n = {n2}")
    print(f"Output: {linked_list_to_list(result2)}")  # Expected: []
    
    # Test case 3
    head3 = create_linked_list([1,2])
    n3 = 1
    result3 = removeNthFromEnd(head3, n3)
    print(f"\nInput: head = [1,2], n = {n3}")
    print(f"Output: {linked_list_to_list(result3)}")  # Expected: [1] 