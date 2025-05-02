def generate_parentheses(n):
    """
    Generate all combinations of n pairs of valid parentheses.
    Time Complexity: O(4^n/sqrt(n))
    Space Complexity: O(4^n/sqrt(n))
    """
    def backtrack(current, open_count, close_count, result):
        # If we've used all pairs, add the current combination to result
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # If we can add an opening parenthesis
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count, result)
        
        # If we can add a closing parenthesis
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1, result)
    
    result = []
    backtrack('', 0, 0, result)
    return result

def main():
    # Test cases
    test_cases = [1, 2, 3]
    
    for n in test_cases:
        result = generate_parentheses(n)
        print(f"Input: n = {n}")
        print(f"Output: {result}")
        print(f"Number of combinations: {len(result)}")
        print("All combinations are valid parentheses\n")

if __name__ == "__main__":
    main() 