class Solution:
    def is_palindrome_string(self, x: int) -> bool:
        """
        Convert to string and compare with reverse.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        s = str(x)
        return s == s[::-1]

    def is_palindrome_half(self, x: int) -> bool:
        """
        Compare first half with second half.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
            
        return x == reversed_half or x == reversed_half // 10

    def is_palindrome_reverse(self, x: int) -> bool:
        """
        Reverse the entire number and compare.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if x < 0:
            return False
            
        original = x
        reversed_num = 0
        
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
            
        return original == reversed_num

def test_solution():
    solution = Solution()
    
    # Test Case 1: Positive palindrome
    x = 121
    print("Test Case 1:")
    print(f"Input: {x}")
    print(f"String Method: {solution.is_palindrome_string(x)}")
    print(f"Half Method: {solution.is_palindrome_half(x)}")
    print(f"Reverse Method: {solution.is_palindrome_reverse(x)}")
    print()
    
    # Test Case 2: Negative number
    x = -121
    print("Test Case 2:")
    print(f"Input: {x}")
    print(f"String Method: {solution.is_palindrome_string(x)}")
    print(f"Half Method: {solution.is_palindrome_half(x)}")
    print(f"Reverse Method: {solution.is_palindrome_reverse(x)}")
    print()
    
    # Test Case 3: Non-palindrome
    x = 10
    print("Test Case 3:")
    print(f"Input: {x}")
    print(f"String Method: {solution.is_palindrome_string(x)}")
    print(f"Half Method: {solution.is_palindrome_half(x)}")
    print(f"Reverse Method: {solution.is_palindrome_reverse(x)}")
    print()
    
    # Test Case 4: Single digit
    x = 5
    print("Test Case 4:")
    print(f"Input: {x}")
    print(f"String Method: {solution.is_palindrome_string(x)}")
    print(f"Half Method: {solution.is_palindrome_half(x)}")
    print(f"Reverse Method: {solution.is_palindrome_reverse(x)}")
    print()
    
    # Test Case 5: Large palindrome
    x = 123454321
    print("Test Case 5:")
    print(f"Input: {x}")
    print(f"String Method: {solution.is_palindrome_string(x)}")
    print(f"Half Method: {solution.is_palindrome_half(x)}")
    print(f"Reverse Method: {solution.is_palindrome_reverse(x)}")

if __name__ == "__main__":
    test_solution() 