def is_valid(s: str) -> bool:
    """
    Check if the input string contains valid parentheses.
    
    Args:
        s: Input string containing only '()[]{}'
        
    Returns:
        True if the parentheses are valid, False otherwise
    """
    # Create a mapping of closing to opening parentheses
    parentheses_map = {')': '(', ']': '[', '}': '{'}
    stack = []
    
    for char in s:
        # If it's a closing parenthesis
        if char in parentheses_map:
            # Pop the top element if stack is not empty, otherwise use a dummy value
            top_element = stack.pop() if stack else '#'
            
            # Check if the popped element matches the mapping
            if parentheses_map[char] != top_element:
                return False
        else:
            # Push opening parenthesis onto the stack
            stack.append(char)
    
    # If stack is empty, all parentheses were matched
    return not stack

def test_is_valid():
    """Test cases for the valid parentheses solution."""
    
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        # Edge cases
        ("(", False),
        (")", False),
        ("[", False),
        ("]", False),
        ("{", False),
        ("}", False),
        # Nested cases
        ("((()))", True),
        ("((())", False),
        ("(()))", False),
        # Mixed cases
        ("({[]})", True),
        ("({[}])", False),
        # Long strings
        ("()" * 1000, True),
        ("({[]})" * 500, True),
        ("({[})" * 1000, False)
    ]
    
    print("Testing Valid Parentheses Solution...")
    for s, expected in test_cases:
        result = is_valid(s)
        
        print(f"\nInput: {s}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_is_valid() 