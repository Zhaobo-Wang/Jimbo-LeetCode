'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        countLetters = {}
        output = 0
        for i in range(len(s)):
            letter = s[i]
            if letter not in countLetters:
                countLetters[letter] = 1
            else:
                countLetters[letter] += 1
        for value in countLetters.values():
            # 1 -> 0   2 -> 2    3 -> 2    4 -> 4     5-> 4
            output += int(value/2) * 2
            if output % 2 == 0 and value % 2 == 1:
                output += 1
        return output
