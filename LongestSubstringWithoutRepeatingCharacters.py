class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
    # A substring is a contiguous part of the string.
    # To find the longest substring without repeating characters, we need to ensure that each character in the current substring is unique.
    # Use the sliding window approach with two pointers (left and right):
    #   The right pointer expands the window by adding characters.
    #   The left pointer shrinks the window when a duplicate character is encountered.

        # Use a set to keep track of characters in the current substring
        char_set = set()
        # Initialize two pointers and the maximum length
        left = 0
        max_length = 0
        
        # Iterate through the string with the right pointer
        for right in range(len(s)):
            # If the character is already in the set, remove characters from the left until it's no longer in the set
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the current character to the set
            char_set.add(s[right])
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length

# Time Complexity: O(n)
#     Each character is added to and removed from char_set at most once.
#     n is the length of the string.
# Space Complexity: O(min(n, a))
#     char_set stores unique characters in the current substring.
#     a is the size of the character set (e.g., 26 for lowercase English letters).
