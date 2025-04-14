class Solution:
    def is_valid_stack(self, s: str) -> bool:
        """
        Stack-based solution with O(n) time complexity.
        Uses a stack to track opening brackets and matches them with closing brackets.
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                # If stack is empty or top element doesn't match
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
                
        return not stack

    def is_valid_replace(self, s: str) -> bool:
        """
        String replacement solution with O(n^2) time complexity.
        Repeatedly removes valid pairs until string is empty or no more pairs can be removed.
        """
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        return not s

def test_solution():
    solution = Solution()
    
    # Test Case 1: Valid parentheses
    s1 = "()"
    print(f"Test Case 1: {s1}")
    print(f"Stack: {solution.is_valid_stack(s1)}")
    print(f"Replace: {solution.is_valid_replace(s1)}")
    print()
    
    # Test Case 2: Valid nested parentheses
    s2 = "({[]})"
    print(f"Test Case 2: {s2}")
    print(f"Stack: {solution.is_valid_stack(s2)}")
    print(f"Replace: {solution.is_valid_replace(s2)}")
    print()
    
    # Test Case 3: Invalid parentheses
    s3 = "(]"
    print(f"Test Case 3: {s3}")
    print(f"Stack: {solution.is_valid_stack(s3)}")
    print(f"Replace: {solution.is_valid_replace(s3)}")
    print()
    
    # Test Case 4: Empty string
    s4 = ""
    print(f"Test Case 4: {s4}")
    print(f"Stack: {solution.is_valid_stack(s4)}")
    print(f"Replace: {solution.is_valid_replace(s4)}")
    print()
    
    # Test Case 5: Unmatched opening bracket
    s5 = "("
    print(f"Test Case 5: {s5}")
    print(f"Stack: {solution.is_valid_stack(s5)}")
    print(f"Replace: {solution.is_valid_replace(s5)}")

if __name__ == "__main__":
    test_solution() 