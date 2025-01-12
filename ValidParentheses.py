class Solution(object):
    def isValid(self, s):
        """
        :type s: str  # Input: A string containing only '()', '[]', '{}'
        :rtype: bool  # Output: True if the string is valid, False otherwise
        """
        # Use a stack to keep track of opening brackets
        stack = []
        
        # Create a mapping of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, else use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # In the end, the stack should be empty if all brackets were matched properly
        return not stack

sol = Solution()
print(sol.isValid("()"))        # Output: True
print(sol.isValid("()[]{}"))    # Output: True
print(sol.isValid("(]"))        # Output: False
print(sol.isValid("([)]"))      # Output: False
print(sol.isValid("{[]}"))      # Output: True
print(sol.isValid("["))         # Output: False
print(sol.isValid(""))          # Output: True

# Explanation:
# Key Observations:
#     Brackets must be opened and closed in pairs ((), {}, []).
#     Brackets must be nested properly, i.e., "([])" is valid, but "([)]" is not.
#     A stack is ideal for solving this problem because it follows the Last In, First Out (LIFO) principle.

# Time Complexity:
#     O(n), where n is the length of the string.
#     Each character is processed once.
# Space Complexity:
#     O(n), for the stack in the worst case when all characters are opening brackets.
