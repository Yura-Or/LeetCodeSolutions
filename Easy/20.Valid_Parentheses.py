"""
20. Valid Parentheses
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        char_dict = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in char_dict:
                stack.append(char)
            elif char in [')', ']', '}']:
                if len(stack) == 0:
                    return False
                elif char_dict[stack.pop(-1)] != char:
                    return False
            else:
                return False

        if len(stack) == 0:
            return True

        return False



