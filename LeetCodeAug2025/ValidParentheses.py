# 20. Valid Parentheses
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.
#
# Examples:
#   Input: "()"       -> True
#   Input: "()[]{}"   -> True
#   Input: "(]"       -> False
#   Input: "([)]"     -> False
#   Input: "{[]}"     -> True

class Solution(object):
    def isValid(self, s):
        # Map closing brackets to their matching opening bracket
        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []  # use a stack to keep track of open brackets

        for char in s:
            if char in bracket_map:  # if it's a closing bracket
                # Pop the top element from stack if not empty, else set dummy '#'
                top_element = stack.pop() if stack else '#'
                # Check if the popped bracket matches the expected opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto stack
                stack.append(char)

        # If stack is empty, all brackets were matched
        return not stack
