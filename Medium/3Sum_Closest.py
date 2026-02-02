"""
3Sum Closest
Medium
Topics
premium lock icon
Companies
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            # 1. Пропускаем дубликаты для i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            # --- Сверхбыстрые проверки (Pruning) ---

            # Минимально возможная сумма с текущим nums[i]
            min_sum = nums[i] + nums[left] + nums[left + 1]
            if min_sum > target:
                # Если даже минимальная сумма больше target,
                # то любая другая сумма с этим i будет еще дальше от target.
                if abs(min_sum - target) < abs(closest_sum - target):
                    closest_sum = min_sum
                # Дальше i перебирать нет смысла, так как числа только растут
                break

                # Максимально возможная сумма с текущим nums[i]
            max_sum = nums[i] + nums[right - 1] + nums[right]
            if max_sum < target:
                # Если даже максимальная сумма меньше target,
                # обновляем ближайшую и переходим к следующему i
                if abs(max_sum - target) < abs(closest_sum - target):
                    closest_sum = max_sum
                continue
            # ---------------------------------------

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == target:
                    return target

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                    # Пропуск дубликатов для left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    # Пропуск дубликатов для right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return closest_sum





sollved = Solution()

assert 2 == sollved.threeSumClosest([-1,2,1,-4], 1)
assert 2 == sollved.threeSumClosest([-1,2,1,4], 0)
assert 3 == sollved.threeSumClosest([1,1,1,1], 3)
assert 15 == sollved.threeSumClosest([1,1,1,5,5,5,5,5,5], 14)