class Solution:
    def is_palindrome_two_pointer(self, s: str) -> bool:
        """
        Two-pointer solution with O(n) time complexity.
        Uses two pointers moving from both ends.
        """
        # Convert to lowercase and remove non-alphanumeric characters
        filtered = [c.lower() for c in s if c.isalnum()]
        
        # Use two pointers to check palindrome
        left, right = 0, len(filtered) - 1
        while left < right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1
        return True

    def is_palindrome_reverse(self, s: str) -> bool:
        """
        Reverse string solution with O(n) time complexity.
        Creates a reversed copy and compares.
        """
        # Convert to lowercase and remove non-alphanumeric characters
        filtered = [c.lower() for c in s if c.isalnum()]
        
        # Compare with reversed version
        return filtered == filtered[::-1]

    def is_palindrome_recursive(self, s: str) -> bool:
        """
        Recursive solution with O(n) time complexity.
        Recursively checks if outer characters match.
        """
        def is_palindrome_helper(chars: list, start: int, end: int) -> bool:
            if start >= end:
                return True
            if chars[start] != chars[end]:
                return False
            return is_palindrome_helper(chars, start + 1, end - 1)

        # Convert to lowercase and remove non-alphanumeric characters
        filtered = [c.lower() for c in s if c.isalnum()]
        
        return is_palindrome_helper(filtered, 0, len(filtered) - 1)

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic palindrome
    s1 = "A man, a plan, a canal: Panama"
    print("Test Case 1:")
    print(f"Input: {s1}")
    print(f"Two Pointer: {solution.is_palindrome_two_pointer(s1)}")
    print(f"Reverse: {solution.is_palindrome_reverse(s1)}")
    print(f"Recursive: {solution.is_palindrome_recursive(s1)}")
    print()
    
    # Test Case 2: Not a palindrome
    s2 = "race a car"
    print("Test Case 2:")
    print(f"Input: {s2}")
    print(f"Two Pointer: {solution.is_palindrome_two_pointer(s2)}")
    print(f"Reverse: {solution.is_palindrome_reverse(s2)}")
    print(f"Recursive: {solution.is_palindrome_recursive(s2)}")
    print()
    
    # Test Case 3: Empty string
    s3 = ""
    print("Test Case 3:")
    print(f"Input: {s3}")
    print(f"Two Pointer: {solution.is_palindrome_two_pointer(s3)}")
    print(f"Reverse: {solution.is_palindrome_reverse(s3)}")
    print(f"Recursive: {solution.is_palindrome_recursive(s3)}")
    print()
    
    # Test Case 4: Single character
    s4 = "a"
    print("Test Case 4:")
    print(f"Input: {s4}")
    print(f"Two Pointer: {solution.is_palindrome_two_pointer(s4)}")
    print(f"Reverse: {solution.is_palindrome_reverse(s4)}")
    print(f"Recursive: {solution.is_palindrome_recursive(s4)}")
    print()
    
    # Test Case 5: Special characters only
    s5 = ".,:"
    print("Test Case 5:")
    print(f"Input: {s5}")
    print(f"Two Pointer: {solution.is_palindrome_two_pointer(s5)}")
    print(f"Reverse: {solution.is_palindrome_reverse(s5)}")
    print(f"Recursive: {solution.is_palindrome_recursive(s5)}")

if __name__ == "__main__":
    test_solution() 