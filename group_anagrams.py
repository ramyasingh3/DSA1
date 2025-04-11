from collections import defaultdict
from typing import List

class Solution:
    def group_anagrams_sort(self, strs: List[str]) -> List[List[str]]:
        """
        Sort-based solution
        Time Complexity: O(n * k log k) where n is number of strings and k is max string length
        Space Complexity: O(n * k)
        """
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())

    def group_anagrams_count(self, strs: List[str]) -> List[List[str]]:
        """
        Count-based solution
        Time Complexity: O(n * k) where n is number of strings and k is max string length
        Space Complexity: O(n * k)
        """
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            groups[key].append(s)
        return list(groups.values())

    def group_anagrams_prime(self, strs: List[str]) -> List[List[str]]:
        """
        Prime number multiplication solution
        Time Complexity: O(n * k) where n is number of strings and k is max string length
        Space Complexity: O(n * k)
        """
        # First 26 prime numbers
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        groups = defaultdict(list)
        for s in strs:
            key = 1
            for c in s:
                key *= primes[ord(c) - ord('a')]
            groups[key].append(s)
        return list(groups.values())

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case
    print("Test Case 1: Basic case")
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solution.group_anagrams_sort(strs)
    print(f"Input: {strs}")
    print(f"Output: {result}")
    print()
    
    # Test Case 2: Empty strings
    print("Test Case 2: Empty strings")
    strs = ["", ""]
    result = solution.group_anagrams_sort(strs)
    print(f"Input: {strs}")
    print(f"Output: {result}")
    print()
    
    # Test Case 3: Single character strings
    print("Test Case 3: Single character strings")
    strs = ["a", "a", "b", "c"]
    result = solution.group_anagrams_sort(strs)
    print(f"Input: {strs}")
    print(f"Output: {result}")
    print()
    
    # Test Case 4: No anagrams
    print("Test Case 4: No anagrams")
    strs = ["abc", "def", "ghi"]
    result = solution.group_anagrams_sort(strs)
    print(f"Input: {strs}")
    print(f"Output: {result}")
    print()
    
    # Test Case 5: All anagrams
    print("Test Case 5: All anagrams")
    strs = ["abc", "bca", "cab"]
    result = solution.group_anagrams_sort(strs)
    print(f"Input: {strs}")
    print(f"Output: {result}")
    print()
    
    # Test all methods
    print("Testing all methods:")
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Input: {strs}")
    print(f"Sort method: {solution.group_anagrams_sort(strs)}")
    print(f"Count method: {solution.group_anagrams_count(strs)}")
    print(f"Prime method: {solution.group_anagrams_prime(strs)}")

if __name__ == "__main__":
    test_solution() 