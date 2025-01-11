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

# Explanation:
# Input: ["flower", "flow", "flight"]

#     Step 1 (Edge case check):
#         If the input is empty ([]), return "".
#         (Not applicable here.)

#     Step 2 (Initialize prefix):
#         Start with the first string as the initial prefix:
#     prefix = "flower"

# Step 3 (Iterate through remaining strings):
#     Compare the prefix with the second string "flow".
#     Check if "flow" starts with "flower" → No, so shorten prefix to "flowe".
#     Keep shortening until "flow" starts with "flow" → Yes.

# Step 4 (Compare with next string):
#     Compare "flow" with "flight".
#     Shorten prefix step-by-step ("flow" → "flo" → "fl") until "flight" starts with "fl" → Yes.

# Step 5 (Return the result):
#     The final prefix is "fl", which is returned as the output.

# Time Complexity: O(n * m)
#     n: Number of strings in the input list.
#     m: Length of the longest string in the input.
#     Worst case: We may check all characters of all strings.

# Space Complexity: O(1)
#     We only use a constant amount of extra space for the prefix variable.
