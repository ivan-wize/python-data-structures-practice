class Solution(object):
    def isValid(self, s):
        """
        :type s: str  # Input: A string containing only '()', '[]', '{}'
        :rtype: bool  # Output: True if the string is valid, False otherwise
        """

        # A stack is ideal for solving this problem because it follows the Last In, First Out (LIFO) principle.

        # Imagine we have a stack. It's like a pile of plates where we can add or remove from the top.
        stack = []

        # Create a hashmap of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

        # Iterate through each character in the input string
        for char in s:
            # If the character is a closing bracket, like ')', ']', or '}'
            if char in bracket_map:
                # Use pop method and try to remove the top item from the stack.
                # If the stack is empty, use a dummy value '#'.
                top_element = stack.pop() if stack else '#'

                # Now check if this top item matches the opening bracket for the current closing bracket.
                # If it doesn't match, the string is invalid.
                if bracket_map[char] != top_element:
                    return False
            else:
                # If the character is an opening bracket, like '(', '[', or '{'
                # Just add it to the stack. It's like putting a plate on the pile.
                stack.append(char)
        
        # At the end, if the stack is empty, it means all brackets matched perfectly.
        # If there's anything left in the stack, it means some brackets didn't close properly.
        return not stack

sol = Solution()
print(sol.isValid("()"))        # Output: True
print(sol.isValid("()[]{}"))    # Output: True
print(sol.isValid("(]"))        # Output: False
print(sol.isValid("([)]"))      # Output: False
print(sol.isValid("{[]}"))      # Output: True
print(sol.isValid("["))         # Output: False
print(sol.isValid(""))          # Output: True

# Time Complexity:
#     O(n), where n is the length of the string.
#     Each character is processed once.
# Space Complexity:
#     O(n), for the stack in the worst case when all characters are opening brackets.
