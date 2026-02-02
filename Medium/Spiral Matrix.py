"""
Spiral Matrix
Medium
Topics
premium lock icon
Companies
Hint
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        solution = matrix[0]


        # [m, n]
        t = [len(matrix[0]) - 1, len(matrix) - 1]

        # [x, y]
        p = [len(matrix[0]) - 1, 0]

        steps = [1, 1, -1, -1]
        step = 1

        while t[step % 2]:
            mowe = steps[step % 4]
            index = step % 2
            target = t[index]
            for i in range(target):
                p[index] += mowe
                solution.append( matrix[p[1]][p[0]] )
            t[index] -= 1
            step += 1

        return solution


s = Solution()

assert s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
assert s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]