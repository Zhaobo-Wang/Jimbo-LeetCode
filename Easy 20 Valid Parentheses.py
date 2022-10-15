'''
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
'''


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        dict = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in dict.keys():
                stack.append(i)  # 把右面的括号保存到stack
            else:
                if stack == []:
                    return False
                right_parentheses_char = stack.pop()  # pop出来右括号
                if i != dict[right_parentheses_char]:
                    return False
        return stack == []
