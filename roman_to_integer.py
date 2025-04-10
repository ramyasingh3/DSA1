class Solution:
    def roman_to_int_dict(self, s: str) -> int:
        """
        Dictionary-based solution
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        prev_value = 0
        
        for char in reversed(s):
            current_value = roman_map[char]
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value
            prev_value = current_value
            
        return result

    def roman_to_int_if(self, s: str) -> int:
        """
        If-else based solution
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        result = 0
        i = 0
        n = len(s)
        
        while i < n:
            if i < n - 1:
                if s[i] == 'I' and s[i+1] == 'V':
                    result += 4
                    i += 2
                    continue
                if s[i] == 'I' and s[i+1] == 'X':
                    result += 9
                    i += 2
                    continue
                if s[i] == 'X' and s[i+1] == 'L':
                    result += 40
                    i += 2
                    continue
                if s[i] == 'X' and s[i+1] == 'C':
                    result += 90
                    i += 2
                    continue
                if s[i] == 'C' and s[i+1] == 'D':
                    result += 400
                    i += 2
                    continue
                if s[i] == 'C' and s[i+1] == 'M':
                    result += 900
                    i += 2
                    continue
            
            if s[i] == 'I':
                result += 1
            elif s[i] == 'V':
                result += 5
            elif s[i] == 'X':
                result += 10
            elif s[i] == 'L':
                result += 50
            elif s[i] == 'C':
                result += 100
            elif s[i] == 'D':
                result += 500
            elif s[i] == 'M':
                result += 1000
                
            i += 1
            
        return result

def test_solution():
    solution = Solution()
    
    # Test Case 1: Simple case
    print("Test Case 1: Simple case")
    s = "III"
    result = solution.roman_to_int_dict(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test Case 2: Subtraction case
    print("Test Case 2: Subtraction case")
    s = "IV"
    result = solution.roman_to_int_dict(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test Case 3: Complex case
    print("Test Case 3: Complex case")
    s = "IX"
    result = solution.roman_to_int_dict(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test Case 4: Large number
    print("Test Case 4: Large number")
    s = "LVIII"
    result = solution.roman_to_int_dict(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test Case 5: Maximum case
    print("Test Case 5: Maximum case")
    s = "MCMXCIV"
    result = solution.roman_to_int_dict(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test both methods
    print("Testing both methods:")
    s = "MCMXCIV"
    print(f"Input: {s}")
    print(f"Dictionary method: {solution.roman_to_int_dict(s)}")
    print(f"If-else method: {solution.roman_to_int_if(s)}")

if __name__ == "__main__":
    test_solution() 