class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    if list1:
        current.next = list1
    else:
        current.next = list2
    
    return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(nums: list[int]) -> ListNode:
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Example usage
if __name__ == "__main__":
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    
    merged_list = merge_two_sorted_lists(list1, list2)
    while merged_list:
        print(merged_list.val, end=" -> ")
        merged_list = merged_list.next
    # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 
