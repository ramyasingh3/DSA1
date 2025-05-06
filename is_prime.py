def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Example usage
if __name__ == "__main__":
    print(is_prime(7))     # True
    print(is_prime(10))    # False
    print(is_prime(2))     # True
    print(is_prime(1))     # False
