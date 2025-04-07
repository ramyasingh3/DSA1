class Solution:
    def reverse_string(self, x: int) -> int:
        """
        String-based solution with O(n) time complexity.
        """
        sign = -1 if x < 0 else 1
        reversed_str = str(abs(x))[::-1]
        reversed_num = sign * int(reversed_str)
        
        # Check for 32-bit integer overflow
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num

    def reverse_number(self, x: int) -> int:
        """
        Number-based solution with O(log n) time complexity.
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0
        
        while x > 0:
            digit = x % 10
            # Check for overflow before multiplying
            if reversed_num > (2**31 - 1 - digit) // 10:
                return 0
            reversed_num = reversed_num * 10 + digit
            x //= 10
            
        return sign * reversed_num

def test_solution():
    solution = Solution()
    
    # Test Case 1: Positive number
    x1 = 123
    print("Test Case 1:")
    print(f"Input: {x1}")
    print(f"String Solution: {solution.reverse_string(x1)}")
    print(f"Number Solution: {solution.reverse_number(x1)}")
    print()
    
    # Test Case 2: Negative number
    x2 = -123
    print("Test Case 2:")
    print(f"Input: {x2}")
    print(f"String Solution: {solution.reverse_string(x2)}")
    print(f"Number Solution: {solution.reverse_number(x2)}")
    print()
    
    # Test Case 3: Number with trailing zeros
    x3 = 120
    print("Test Case 3:")
    print(f"Input: {x3}")
    print(f"String Solution: {solution.reverse_string(x3)}")
    print(f"Number Solution: {solution.reverse_number(x3)}")
    print()
    
    # Test Case 4: Overflow case
    x4 = 1534236469
    print("Test Case 4:")
    print(f"Input: {x4}")
    print(f"String Solution: {solution.reverse_string(x4)}")
    print(f"Number Solution: {solution.reverse_number(x4)}")
    print()
    
    # Test Case 5: Single digit
    x5 = 5
    print("Test Case 5:")
    print(f"Input: {x5}")
    print(f"String Solution: {solution.reverse_string(x5)}")
    print(f"Number Solution: {solution.reverse_number(x5)}")

if __name__ == "__main__":
    test_solution() 