from typing import List

class Solution:
    def longest_common_prefix_vertical(self, strs: List[str]) -> str:
        """
        Vertical scanning solution with O(S) time complexity.
        S is the sum of all characters in all strings.
        """
        if not strs:
            return ""
            
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
                    
        return strs[0]

    def longest_common_prefix_horizontal(self, strs: List[str]) -> str:
        """
        Horizontal scanning solution with O(S) time complexity.
        S is the sum of all characters in all strings.
        """
        if not strs:
            return ""
            
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

    def longest_common_prefix_divide(self, strs: List[str]) -> str:
        """
        Divide and conquer solution with O(S) time complexity.
        S is the sum of all characters in all strings.
        """
        def common_prefix(left: str, right: str) -> str:
            min_len = min(len(left), len(right))
            for i in range(min_len):
                if left[i] != right[i]:
                    return left[:i]
            return left[:min_len]
            
        def divide_and_conquer(strs: List[str], l: int, r: int) -> str:
            if l == r:
                return strs[l]
            mid = (l + r) // 2
            lcp_left = divide_and_conquer(strs, l, mid)
            lcp_right = divide_and_conquer(strs, mid + 1, r)
            return common_prefix(lcp_left, lcp_right)
            
        if not strs:
            return ""
        return divide_and_conquer(strs, 0, len(strs) - 1)

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case
    strs1 = ["flower", "flow", "flight"]
    print("Test Case 1:")
    print(f"Input: {strs1}")
    print(f"Vertical Solution: {solution.longest_common_prefix_vertical(strs1)}")
    print(f"Horizontal Solution: {solution.longest_common_prefix_horizontal(strs1)}")
    print(f"Divide Solution: {solution.longest_common_prefix_divide(strs1)}")
    print()
    
    # Test Case 2: No common prefix
    strs2 = ["dog", "racecar", "car"]
    print("Test Case 2:")
    print(f"Input: {strs2}")
    print(f"Vertical Solution: {solution.longest_common_prefix_vertical(strs2)}")
    print(f"Horizontal Solution: {solution.longest_common_prefix_horizontal(strs2)}")
    print(f"Divide Solution: {solution.longest_common_prefix_divide(strs2)}")
    print()
    
    # Test Case 3: Empty list
    strs3 = []
    print("Test Case 3:")
    print(f"Input: {strs3}")
    print(f"Vertical Solution: {solution.longest_common_prefix_vertical(strs3)}")
    print(f"Horizontal Solution: {solution.longest_common_prefix_horizontal(strs3)}")
    print(f"Divide Solution: {solution.longest_common_prefix_divide(strs3)}")
    print()
    
    # Test Case 4: Single string
    strs4 = ["a"]
    print("Test Case 4:")
    print(f"Input: {strs4}")
    print(f"Vertical Solution: {solution.longest_common_prefix_vertical(strs4)}")
    print(f"Horizontal Solution: {solution.longest_common_prefix_horizontal(strs4)}")
    print(f"Divide Solution: {solution.longest_common_prefix_divide(strs4)}")
    print()
    
    # Test Case 5: All strings same
    strs5 = ["abc", "abc", "abc"]
    print("Test Case 5:")
    print(f"Input: {strs5}")
    print(f"Vertical Solution: {solution.longest_common_prefix_vertical(strs5)}")
    print(f"Horizontal Solution: {solution.longest_common_prefix_horizontal(strs5)}")
    print(f"Divide Solution: {solution.longest_common_prefix_divide(strs5)}")

if __name__ == "__main__":
    test_solution() 