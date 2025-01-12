class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

    # Anagrams Definition: Two strings are anagrams if they contain the exact same characters in any order. For example, "eat", "tea", and "ate" are anagrams.
    # Key Idea: By sorting the characters of a string, all anagrams will have the same sorted string as their key. For instance:
    #   "eat" → "aet"
    #   "tea" → "aet"
    #   "ate" → "aet"
    # Group Anagrams: Use a dictionary where:
    #     The key is the sorted string.
    #     The value is a list of all original strings that match the sorted key.

        # A dictionary to group anagrams, using sorted strings as keys
        anagram_map = {}
        
        # Iterate over each string in the list
        for string in strs:
            # Sort the characters of the string to get the key
            key = ''.join(sorted(string))
            
            # If the key is not in the dictionary, initialize an empty list
            if key not in anagram_map:
                anagram_map[key] = []
            
            # Append the original string to the corresponding list
            anagram_map[key].append(string)
        
        # Return the values of the dictionary as the grouped anagrams
        return list(anagram_map.values())

# Time Complexity:
#     Sorting each string takes O(k log k), where k is the length of the string.
#     If there are n strings in strs, the total time complexity is O(n * k log k).
# Space Complexity:
#     The dictionary anagram_map requires O(n * k) space to store all strings and keys.

sol = Solution()

print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

print(sol.groupAnagrams([""]))
# Output: [[""]]

print(sol.groupAnagrams(["a"]))
# Output: [["a"]]

print(sol.groupAnagrams(["abc", "bca", "cab", "xyz", "zyx"]))
# Output: [["abc", "bca", "cab"], ["xyz", "zyx"]]
