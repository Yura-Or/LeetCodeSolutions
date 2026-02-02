"""
51.
N - Queens
Hard
Topics
premium
lock
icon
Companies
The n - queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n - queens puzzle.You may return the answer in any order.

Each solution contains a distinct board configuration of the n - queens ' placement, where ' Q ' and '. ' both indicate
a queen and an empty space, respectively.

Example
1:

Input: n = 4
Output: [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
Explanation: There
exist
two
distinct
solutions
to
the
4 - queens
puzzle as shown
above
Example
2:

Input: n = 1
Output: [["Q"]]
"""
import math

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        if n == 1:
            return [["Q"]]

        self.solution = []
        self.board = [-1] * n
        self.n = n

        for i in range(math.ceil(n / 2)):
            self.board[i] = 0
            self.dfs( 1 )
            self.board[i] = -1



        return self.solution

    def dfs (self, deep: int):
        if deep == self.n:
            # solution + relers solution
            d = dict()
            s = []
            sr = []
            for i in range(self.n):
                tmp = ["."] * self.n
                tmp_revers = ["."] * self.n
                tmp[i] = "Q"
                tmp_revers[self.n - i - 1] = "Q"
                d[self.board[i]] = (tmp, tmp_revers)
            for i in range(self.n):
                s.append("".join(d[i][0]))
                sr.append("".join(d[i][1]))

            self.solution.append(s)

            if self.n % 2 == 1 and self.board[int(self.n / 2)] == 0:
                return

            self.solution.append(sr)
            return

        skips = []

        for i in range(self.n):
            if self.board[i] == -1:
                continue
            skips.append(i + (deep - self.board[i]))
            skips.append(i - (deep - self.board[i]))

        for i in range(self.n):
            if self.board[i] != -1 or i in skips:
                continue
            self.board[i] = deep
            self.dfs(deep + 1)
            self.board[i] = -1


s = Solution()
assert s.solveNQueens(1) == [["Q"]]
assert s.solveNQueens(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]