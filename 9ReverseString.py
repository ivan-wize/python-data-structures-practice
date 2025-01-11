class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Initialize two pointers: one at the start and one at the end of the list
        left, right = 0, len(s) - 1
        
        # Swap elements while the left pointer is less than the right pointer
        while left < right:
            # Swap characters at left and right
            s[left], s[right] = s[right], s[left]
            # Move the pointers towards the center
            left += 1
            right -= 1

# Explanation:
# Key Observations:
#     The string is given as a list of characters (s).
#     To reverse the string:
#         Swap the first character with the last, the second with the second-to-last, and so on.
#     Use a two-pointer approach:
#         One pointer starts at the beginning (left) and the other at the end (right).

# Approach:
#     Initialize Pointers:
#         left points to the start of the list.
#         right points to the end of the list.
#     Swap Elements:
#         Swap s[left] and s[right].
#         Increment left and decrement right to move towards the center.
#     Stop Condition:
#         Stop when left >= right.

# Time Complexity: O(n)
#     The algorithm processes each character in the string once.

# Space Complexity: O(1)
#     The algorithm uses only two pointers and performs swaps in-place.

sol = Solution()

# Test case 1
s = ["h", "e", "l", "l", "o"]
sol.reverseString(s)
print(s)  # Output: ["o", "l", "l", "e", "h"]

# Test case 2
s = ["H", "a", "n", "n", "a", "h"]
sol.reverseString(s)
print(s)  # Output: ["h", "a", "n", "n", "a", "H"]

# Test case 3
s = ["a"]
sol.reverseString(s)
print(s)  # Output: ["a"]

# Test case 4
s = ["a", "b"]
sol.reverseString(s)
print(s)  # Output: ["b", "a"]
