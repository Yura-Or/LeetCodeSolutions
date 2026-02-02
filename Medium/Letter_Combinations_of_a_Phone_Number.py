"""
17.
Letter
Combinations
of
a
Phone
Number
Medium
Topics
premium
lock
icon
Companies
Given
a
string
containing
digits
from

2 - 9
inclusive,
return all
possible
letter
combinations
that
the
number
could
represent.Return
the
answer in any
order.

A
mapping
of
digits
to
letters(just
like
on
the
telephone
buttons) is given
below.Note
that
1
does
not map
to
any
letters.

Example
1:

Input: digits = "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
Example
2:

Input: digits = "2"
Output: ["a", "b", "c"]

Constraints:

1 <= digits.length <= 4
digits[i] is a
digit in the
range['2', '9'].
"""

class Solution:
    digits: str
    solution: list[str]
    tmp_list: list[str] = []
    char_map: dict = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z'], }

    def letterCombinations(self, digits: str) -> list[str]:
        self.solution = []
        self.digits = digits
        self.rek(0)
        return self.solution

    def rek(self, i: int):

        if i != len(self.digits) - 1:
            for s in self.char_map[self.digits[i]]:
                self.tmp_list.append(s)
                self.rek(i+1)
                self.tmp_list.pop()
        else:
            for s in self.char_map[self.digits[i]]:
                self.tmp_list.append(s)
                self.solution.append("".join(self.tmp_list))
                self.tmp_list.pop()

solved = Solution()

assert ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'] == solved.letterCombinations("23")
