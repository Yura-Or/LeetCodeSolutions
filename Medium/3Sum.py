"""
3Sum
Attempted
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)

        res_append = res.append

        for i in range(n - 2):
            a = nums[i]
            if a > 0: break
            if i > 0 and a == nums[i - 1]: continue

            l, r = i + 1, n - 1

            if a + nums[l] + nums[l + 1] > 0:
                continue
            if a + nums[r] + nums[r - 1] < 0:
                continue

            while l < r:
                b, c = nums[l], nums[r]
                s = a + b + c
                if s == 0:
                    res_append([a, b, c])
                    while l < r and nums[l] == b:
                        l += 1
                    while l < r and nums[r] == c:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return res



s = Solution()
print(s.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))
assert [[-1,-1,2],[-1,0,1]] == s.threeSum([-1,0,1,2,-1,-4])
assert s.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]) == [[-10,5,5],[-5,0,5],[-4,2,2],[-3,-2,5],[-3,1,2],[-2,0,2]]
