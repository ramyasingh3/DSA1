def merge_sorted_arrays_two_pointers(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merge two sorted arrays using two pointers approach.
    Time Complexity: O(m + n)
    Space Complexity: O(1)
    """
    # Initialize pointers for nums1, nums2, and the merged array
    p1 = m - 1  # Pointer for nums1
    p2 = n - 1  # Pointer for nums2
    p = m + n - 1  # Pointer for the merged array
    
    # While there are elements to compare
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

def merge_sorted_arrays_extra_space(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merge two sorted arrays using extra space.
    Time Complexity: O(m + n)
    Space Complexity: O(m + n)
    """
    # Create a copy of nums1
    nums1_copy = nums1[:m]
    
    # Initialize pointers
    p1 = 0  # Pointer for nums1_copy
    p2 = 0  # Pointer for nums2
    p = 0   # Pointer for nums1
    
    # Compare elements and merge
    while p1 < m and p2 < n:
        if nums1_copy[p1] <= nums2[p2]:
            nums1[p] = nums1_copy[p1]
            p1 += 1
        else:
            nums1[p] = nums2[p2]
            p2 += 1
        p += 1
    
    # Copy remaining elements
    if p1 < m:
        nums1[p:] = nums1_copy[p1:]
    if p2 < n:
        nums1[p:] = nums2[p2:]

def merge_sorted_arrays_sort(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merge two sorted arrays using built-in sort (not recommended for interviews).
    Time Complexity: O((m + n) * log(m + n))
    Space Complexity: O(1)
    """
    # Copy nums2 into nums1
    nums1[m:] = nums2[:n]
    # Sort the entire array
    nums1.sort()

def merge_k_sorted_arrays(arrays: list[list[int]]) -> list[int]:
    """
    Merge k sorted arrays using a min heap.
    Time Complexity: O(n * log k) where n is total number of elements
    Space Complexity: O(n + k)
    """
    import heapq
    
    # Create a min heap
    heap = []
    result = []
    
    # Push first element of each array into heap
    for i, arr in enumerate(arrays):
        if arr:  # If array is not empty
            heapq.heappush(heap, (arr[0], i, 0))
    
    # While heap is not empty
    while heap:
        # Pop smallest element
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # If there are more elements in the array
        if elem_idx + 1 < len(arrays[arr_idx]):
            heapq.heappush(heap, (arrays[arr_idx][elem_idx + 1], arr_idx, elem_idx + 1))
    
    return result

def main():
    # Test cases for merging two sorted arrays
    test_cases = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),  # Expected: [1, 2, 2, 3, 5, 6]
        ([1], 1, [], 0),                        # Expected: [1]
        ([0], 0, [1], 1),                       # Expected: [1]
        ([2, 0], 1, [1], 1),                    # Expected: [1, 2]
        ([1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3),  # Expected: [1, 2, 3, 4, 5, 6]
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3),  # Expected: [1, 2, 3, 4, 5, 6]
    ]
    
    print("Testing Two Pointers solution:")
    for nums1, m, nums2, n in test_cases:
        nums1_copy = nums1.copy()
        merge_sorted_arrays_two_pointers(nums1_copy, m, nums2, n)
        print(f"nums1: {nums1[:m]}, nums2: {nums2}")
        print(f"Merged: {nums1_copy}")
        print()
    
    print("\nTesting Extra Space solution:")
    for nums1, m, nums2, n in test_cases:
        nums1_copy = nums1.copy()
        merge_sorted_arrays_extra_space(nums1_copy, m, nums2, n)
        print(f"nums1: {nums1[:m]}, nums2: {nums2}")
        print(f"Merged: {nums1_copy}")
        print()
    
    print("\nTesting Sort solution:")
    for nums1, m, nums2, n in test_cases:
        nums1_copy = nums1.copy()
        merge_sorted_arrays_sort(nums1_copy, m, nums2, n)
        print(f"nums1: {nums1[:m]}, nums2: {nums2}")
        print(f"Merged: {nums1_copy}")
        print()
    
    # Test cases for merging k sorted arrays
    k_sorted_arrays = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [0, 10, 11]
    ]
    
    print("\nTesting K Sorted Arrays solution:")
    print("Input arrays:")
    for arr in k_sorted_arrays:
        print(f"  {arr}")
    result = merge_k_sorted_arrays(k_sorted_arrays)
    print(f"Merged result: {result}")

if __name__ == "__main__":
    main() 