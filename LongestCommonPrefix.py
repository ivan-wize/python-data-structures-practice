class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]  # Input: A list of strings
        :rtype: str            # Output: A string representing the longest common prefix
        """
        # Edge case: If the input list is empty, return an empty string
        if not strs:
            return ""
        
        # Start by assuming the first string is the common prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for string in strs[1:]:
            # Reduce the prefix while it doesn't match the start of the current string
            while not string.startswith(prefix):
                # Gradually shorten the prefix by removing the last character
                prefix = prefix[:-1]
                
                # If the prefix becomes empty, there's no common prefix
                if not prefix:
                    return ""
        
        # Return the longest common prefix after processing all strings
        return prefix
    
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog","racecar","car"]))     # Output: ""
print(sol.longestCommonPrefix(["interspecies","interstellar","interstate"])) # Output: "inters"
print(sol.longestCommonPrefix([""]))                        # Output: ""
print(sol.longestCommonPrefix(["a"]))                       # Output: "a"
print(sol.longestCommonPrefix(["abc","abc","abc"]))         # Output: "abc"

# Time Complexity: O(n * m)
#     n: Number of strings in the input list.
#     m: Length of the longest string in the input.
#     Worst case: We may check all characters of all strings.

# Space Complexity: O(1)
#     We only use a constant amount of extra space for the prefix variable.
