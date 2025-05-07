def is_palindrome(s: str) -> bool:
    filtered = ''.join(char.lower() for char in s if char.isalnum())
    return filtered == filtered[::-1]

# Example usage
if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("race a car"))                      # False
    print(is_palindrome("madam"))                           # True
