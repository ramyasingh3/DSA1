def char_frequency(s: str) -> dict[str, int]:
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Example usage
if __name__ == "__main__":
    print(char_frequency("hello"))        # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(char_frequency("aabbccc"))      # {'a': 2, 'b': 2, 'c': 3}
    print(char_frequency("123321"))       # {'1': 2, '2': 2, '3': 2}

