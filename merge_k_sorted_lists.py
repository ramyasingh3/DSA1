from heapq import heappush, heappop
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        # For heap comparison
        return self.val < other.val

def merge_k_lists_heap(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists using a min heap.
    Time Complexity: O(N log k) where N is total number of nodes and k is number of lists
    Space Complexity: O(k) for the heap
    """
    if not lists:
        return None
    
    # Create a min heap
    min_heap = []
    
    # Push the first node of each list into the heap
    for i, head in enumerate(lists):
        if head:
            heappush(min_heap, (head.val, i, head))
    
    # Create a dummy node to build the result list
    dummy = ListNode(0)
    current = dummy
    
    # Process nodes from the heap
    while min_heap:
        # Get the node with minimum value
        val, i, node = heappop(min_heap)
        
        # Add it to the result list
        current.next = node
        current = current.next
        
        # If there's a next node in the list, push it to the heap
        if node.next:
            heappush(min_heap, (node.next.val, i, node.next))
    
    return dummy.next

def merge_k_lists_divide_conquer(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists using divide and conquer approach.
    Time Complexity: O(N log k)
    Space Complexity: O(log k) for recursion stack
    """
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    
    def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        current.next = l1 if l1 else l2
        return dummy.next
    
    def merge_lists(left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return lists[left]
        if left + 1 == right:
            return merge_two_lists(lists[left], lists[right])
        
        mid = (left + right) // 2
        left_list = merge_lists(left, mid)
        right_list = merge_lists(mid + 1, right)
        return merge_two_lists(left_list, right_list)
    
    return merge_lists(0, len(lists) - 1)

def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Helper function to convert a linked list to a list of values."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def main():
    # Test cases
    test_cases = [
        # Test case 1
        [
            create_linked_list([1, 4, 5]),
            create_linked_list([1, 3, 4]),
            create_linked_list([2, 6])
        ],
        # Test case 2
        [
            create_linked_list([1, 2, 3]),
            create_linked_list([4, 5, 6]),
            create_linked_list([7, 8, 9])
        ],
        # Test case 3
        [
            create_linked_list([1]),
            create_linked_list([2]),
            create_linked_list([3])
        ],
        # Test case 4
        [
            create_linked_list([1, 2, 3]),
            None,
            create_linked_list([4, 5, 6])
        ],
        # Test case 5
        []
    ]
    
    print("Testing Heap-based solution:")
    for i, lists in enumerate(test_cases, 1):
        result = merge_k_lists_heap(lists)
        print(f"Test case {i}:")
        print("Input lists:")
        for lst in lists:
            print(linked_list_to_list(lst) if lst else None)
        print("Merged list:", linked_list_to_list(result))
        print()
    
    print("\nTesting Divide and Conquer solution:")
    for i, lists in enumerate(test_cases, 1):
        result = merge_k_lists_divide_conquer(lists)
        print(f"Test case {i}:")
        print("Input lists:")
        for lst in lists:
            print(linked_list_to_list(lst) if lst else None)
        print("Merged list:", linked_list_to_list(result))
        print()

if __name__ == "__main__":
    main() 