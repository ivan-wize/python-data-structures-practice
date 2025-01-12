class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Anagrams must have the same length
        if len(s) != len(t):
            return False
        
        # Count the frequency of each character in both strings
        count_s = {}
        count_t = {}
        
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        # Compare the two dictionaries
        return count_s == count_t

# Explanation:
# Key Observations:
#     Anagrams are strings that contain the same characters with the same frequencies, but potentially in a different order.
#         Example: "anagram" and "nagaram".
#     To check if two strings are anagrams:
#         Count the frequency of each character in both strings.
#         Compare the frequency counts.

# Approach:
#     Length Check:
#         If s and t have different lengths, they cannot be anagrams.
#     Count Characters:
#         Use a dictionary to count the frequency of each character in both strings.
#     Compare Counts:
#         Compare the dictionaries containing character frequencies for both strings. If they match, the strings are anagrams.

# Optimized Approach Using Sorting
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

# Explanation:
#     Sorting rearranges the characters in both strings in the same order.
#     If the sorted strings are identical, they are anagrams.

# Complexity Analysis:
#     Using Dictionaries:
#         Time Complexity: O(n) (counting frequencies for both strings).
#         Space Complexity: O(1) (limited to 26 lowercase English letters or the number of unique characters).
#     Using Sorting:
#         Time Complexity: O(n log n) (due to sorting).
#         Space Complexity: O(n) (for the sorted array).

sol = Solution()

# Test case 1: Anagrams
print(sol.isAnagram("anagram", "nagaram"))  # Output: True

# Test case 2: Not Anagrams
print(sol.isAnagram("rat", "car"))  # Output: False

# Test case 3: Different lengths
print(sol.isAnagram("a", "aa"))  # Output: False

# Test case 4: Unicode characters
print(sol.isAnagram("你好", "好你"))  # Output: True

# Test case 5: Empty strings
print(sol.isAnagram("", ""))  # Output: True
