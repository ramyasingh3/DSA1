"""
Valid Parentheses Implementation

This file contains multiple implementations to check if a string of parentheses is valid.

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) for stack-based solution
"""

def is_valid_parentheses(s):
    """
    Check if the input string has valid parentheses.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Dictionary to store matching pairs
    brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    # Stack to keep track of opening brackets
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        # If it's an opening bracket, push to stack
        if char in '({[':
            stack.append(char)
        # If it's a closing bracket
        elif char in ')}]':
            # If stack is empty or top of stack doesn't match
            if not stack or stack.pop() != brackets[char]:
                return False
    
    # Stack should be empty if all brackets are matched
    return len(stack) == 0

def is_valid_counting(s: str) -> bool:
    """
    Check if the string has valid parentheses using counting (only works for single type of brackets).
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    count = 0
    
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    
    return count == 0

def is_valid_recursive(s: str) -> bool:
    """
    Check if parentheses are valid using recursive approach.
    This is less efficient than the stack approach but demonstrates
    a different way of thinking about the problem.
    
    Args:
        s (str): String containing parentheses
        
    Returns:
        bool: True if parentheses are valid, False otherwise
    """
    def remove_valid_pairs(s: str) -> str:
        """Remove valid pairs of parentheses recursively"""
        if not s:
            return ""
        
        # Find the first valid pair
        for i in range(len(s) - 1):
            if (s[i] == '(' and s[i + 1] == ')') or \
               (s[i] == '{' and s[i + 1] == '}') or \
               (s[i] == '[' and s[i + 1] == ']'):
                # Remove the pair and continue with the rest
                return remove_valid_pairs(s[:i] + s[i + 2:])
        
        return s
    
    # Keep removing valid pairs until no more can be removed
    result = remove_valid_pairs(s)
    return len(result) == 0

def is_valid_regex(s: str) -> bool:
    """
    Check if the string has valid parentheses using regex (not recommended for production).
    Time Complexity: O(n²) in worst case
    Space Complexity: O(n)
    """
    import re
    pattern = r'\(\)|\[\]|\{\}'
    
    while re.search(pattern, s):
        s = re.sub(pattern, '', s)
    
    return len(s) == 0

def get_all_valid_parentheses(n: int) -> list[str]:
    """
    Generate all valid parentheses combinations for n pairs.
    Time Complexity: O(4^n / sqrt(n))
    Space Complexity: O(4^n / sqrt(n))
    """
    def backtrack(current: str, open_count: int, close_count: int):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    result = []
    backtrack('', 0, 0)
    return result

def test_valid_parentheses():
    """Test cases for valid parentheses implementations"""
    test_cases = [
        ("()", True),           # Simple valid case
        ("()[]{}", True),       # Multiple valid pairs
        ("(]", False),          # Invalid pair
        ("([)]", False),        # Wrong order
        ("{[]}", True),         # Nested valid
        ("", True),             # Empty string
        ("(((", False),         # Unclosed
        (")))", False),         # Unopened
        ("(())", True),         # Nested same type
        ("([{}])", True),       # Complex nested
    ]
    
    for s, expected in test_cases:
        # Test stack approach
        assert is_valid_parentheses(s) == expected, f"Stack test failed for '{s}'"
        
        # Test counting approach (only for single type)
        if all(c in '()' for c in s):
            assert is_valid_counting(s) == expected, f"Counting test failed for '{s}'"
        
        # Test recursive approach
        assert is_valid_recursive(s) == expected, f"Recursive test failed for '{s}'"
    
    print("All test cases passed!")

def main():
    # Test cases for valid parentheses
    test_cases = [
        "()",           # Expected: True
        "()[]{}",      # Expected: True
        "(]",          # Expected: False
        "([)]",        # Expected: False
        "{[]}",        # Expected: True
        "",            # Expected: True
        "(((",         # Expected: False
        ")))",         # Expected: False
        "({[]})",      # Expected: True
        "({[}])",      # Expected: False
        "((()))",      # Expected: True
        "(()))",       # Expected: False
    ]
    
    print("Testing Stack-based solution:")
    for s in test_cases:
        result = is_valid_parentheses(s)
        print(f"String: '{s}'")
        print(f"Is valid: {result}")
        print()
    
    print("\nTesting Counting solution (for single type of brackets):")
    single_bracket_tests = [
        "()",           # Expected: True
        "(()",          # Expected: False
        "())",          # Expected: False
        "((()))",       # Expected: True
        "",             # Expected: True
        "(",            # Expected: False
        ")",            # Expected: False
    ]
    for s in single_bracket_tests:
        result = is_valid_counting(s)
        print(f"String: '{s}'")
        print(f"Is valid: {result}")
        print()
    
    print("\nTesting Regex solution:")
    for s in test_cases:
        result = is_valid_regex(s)
        print(f"String: '{s}'")
        print(f"Is valid: {result}")
        print()
    
    print("\nGenerating all valid parentheses combinations:")
    for n in range(1, 5):
        combinations = get_all_valid_parentheses(n)
        print(f"\nFor n = {n}:")
        print(f"Number of combinations: {len(combinations)}")
        print("Combinations:")
        for combo in combinations:
            print(f"  {combo}")

if __name__ == "__main__":
    # Run test cases
    test_valid_parentheses()
    
    # Example usage
    main() 