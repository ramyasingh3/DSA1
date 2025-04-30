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

def is_valid_stack(s: str) -> bool:
    """
    Check if parentheses are valid using a stack.
    This is the optimal solution with O(n) time complexity.
    
    Args:
        s (str): String containing parentheses
        
    Returns:
        bool: True if parentheses are valid, False otherwise
    """
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        # If it's an opening bracket, push to stack
        if char in '({[':
            stack.append(char)
        # If it's a closing bracket
        elif char in ')}]':
            # If stack is empty or top of stack doesn't match
            if not stack or stack.pop() != bracket_map[char]:
                return False
    
    # Stack should be empty if all brackets are properly matched
    return len(stack) == 0

def is_valid_counting(s: str) -> bool:
    """
    Check if parentheses are valid using counting approach.
    Note: This approach only works for single type of parentheses.
    For multiple types, we need to track the order as well.
    
    Args:
        s (str): String containing parentheses
        
    Returns:
        bool: True if parentheses are valid, False otherwise
    """
    count = 0
    
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:  # More closing brackets than opening
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
        assert is_valid_stack(s) == expected, f"Stack test failed for '{s}'"
        
        # Test counting approach (only for single type)
        if all(c in '()' for c in s):
            assert is_valid_counting(s) == expected, f"Counting test failed for '{s}'"
        
        # Test recursive approach
        assert is_valid_recursive(s) == expected, f"Recursive test failed for '{s}'"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_valid_parentheses()
    
    # Example usage
    test_strings = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
        "(((",
        "([{}])"
    ]
    
    print("\nTesting various strings:")
    for s in test_strings:
        print(f"\nString: '{s}'")
        print(f"Using stack: {is_valid_stack(s)}")
        if all(c in '()' for c in s):
            print(f"Using counting: {is_valid_counting(s)}")
        print(f"Using recursive: {is_valid_recursive(s)}") 