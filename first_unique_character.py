class Solution:
    def first_uniq_char_counter(self, s: str) -> int:
        """
        Counter-based solution
        Time Complexity: O(n)
        Space Complexity: O(1) since we have fixed number of characters
        """
        from collections import Counter
        count = Counter(s)
        
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
                
        return -1

    def first_uniq_char_array(self, s: str) -> int:
        """
        Array-based solution
        Time Complexity: O(n)
        Space Complexity: O(1) since we have fixed size array
        """
        count = [0] * 26  # Assuming only lowercase English letters
        
        for char in s:
            count[ord(char) - ord('a')] += 1
            
        for i, char in enumerate(s):
            if count[ord(char) - ord('a')] == 1:
                return i
                
        return -1

    def first_uniq_char_dict(self, s: str) -> int:
        """
        Dictionary-based solution
        Time Complexity: O(n)
        Space Complexity: O(1) since we have fixed number of characters
        """
        char_dict = {}
        
        for char in s:
            char_dict[char] = char_dict.get(char, 0) + 1
            
        for i, char in enumerate(s):
            if char_dict[char] == 1:
                return i
                
        return -1

def test_solution():
    solution = Solution()
    
    # Test Case 1: Unique character exists
    print("Test Case 1: Unique character exists")
    s = "leetcode"
    result = solution.first_uniq_char_counter(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test Case 2: No unique character
    print("Test Case 2: No unique character")
    s = "aabb"
    result = solution.first_uniq_char_counter(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test Case 3: First character is unique
    print("Test Case 3: First character is unique")
    s = "loveleetcode"
    result = solution.first_uniq_char_counter(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test Case 4: Empty string
    print("Test Case 4: Empty string")
    s = ""
    result = solution.first_uniq_char_counter(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test Case 5: Single character
    print("Test Case 5: Single character")
    s = "a"
    result = solution.first_uniq_char_counter(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test all methods
    print("Testing all methods:")
    s = "leetcode"
    print(f"Input: {s}")
    print(f"Counter method: {solution.first_uniq_char_counter(s)}")
    print(f"Array method: {solution.first_uniq_char_array(s)}")
    print(f"Dictionary method: {solution.first_uniq_char_dict(s)}")

if __name__ == "__main__":
    test_solution() 