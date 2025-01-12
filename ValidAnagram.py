class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    # Anagrams are strings that contain the same characters with the same frequencies, but potentially in a different order.
    #   Example: "anagram" and "nagaram".
    # To check if two strings are anagrams:
    #   Count the frequency of each character in both strings.
    #   Compare the frequency counts.

        # Anagrams must have the same length
        if len(s) != len(t):
            return False
        
        # Create 2 hashmaps to count the frequency of each character in both strings
        count_s = {}
        count_t = {}
    
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        # Compare the two dictionaries
        return count_s == count_t

# Optimized Approach Using Sorting
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    # Sorting rearranges the characters in both strings in the same order.
    # If the sorted strings are identical, they are anagrams.
        return sorted(s) == sorted(t)

    # Using Dictionaries:
    #   Time Complexity: O(n) (counting frequencies for both strings).
    #   Space Complexity: O(1) (limited to 26 lowercase English letters or the number of unique characters).
    # Using Sorting:
    #   Time Complexity: O(n log n) (due to sorting).
    #   Space Complexity: O(n) (for the sorted array).

sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))  # Output: True
print(sol.isAnagram("rat", "car"))  # Output: False
print(sol.isAnagram("a", "aa"))  # Output: False
print(sol.isAnagram("你好", "好你"))  # Output: True
print(sol.isAnagram("", ""))  # Output: True
