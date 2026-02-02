

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:


        if not nums1:
            return self.median(nums2)
        if not nums2:
            return self.median(nums1)

        l1, l2, r1, r2 = 0, 0, len(nums1) - 1, len(nums2) - 1
        flag = False
        n1, n2 = nums1, nums2
        len1, len2 = len(nums1), len(nums2)
        l = 0
        r = 0

        while (len1 + len2) > 30:
            if len1 < len2:
                flag = True
                n1, n2 = n2, n1
                l1, l2, r1, r2 = l2, l1, r2, r1

            ind1l = l1 + (r1 - l1) // 2
            ind1r = ind1l + 1

            ind2r = self.binarySearch(n2, l2, r2, n1[ind1l])
            ind2l = ind2r - 1

            left = l + ind1l - l1 + ind2l - l2
            right = r + r1 - ind1r + r2 - ind2r

            if left > right:
                r += r1 - ind1l + r2 - ind2l
                r1 = ind1l
                r2 = ind2l
            elif left < right:
                l += ind1r - l1 + ind2r - l2
                l1 = ind1r
                l2 = ind2r
            else:
                return (max(n1[ind1l], n2[ind2l]) + min(n1[ind1r], n2[ind2r])) / 2

            len1 = r1 - l1 + 1
            len2 = r2 - l2 + 1

            if flag:
                flag = False
                n1, n2 = n2, n1
                l1, l2, r1, r2 = l2, l1, r2, r1
                len1, len2 = len2, len1

        tmpnum = n1[l1:r1 + 1]
        tmpnum.extend(n2[l2:r2 + 1])
        tmpnum = sorted(tmpnum)

        shift = (r - l) / 2
        index = (len(tmpnum) - 1) / 2 + shift

        if index == int(index):
            return tmpnum[int(index)]
        else:
            return (tmpnum[int(index)] + tmpnum[int(index) + 1]) / 2


    def median(self, nums: list[int]) -> float:
        if len(nums) < 2:
            return nums[0]
        if len(nums) % 2 == 0:
            ind = (len(nums) - 1) // 2
            return (nums[ind] + nums[ind + 1]) / 2
        else:
            return nums[(len(nums) - 1) // 2]

    def binarySearch(self, nums: list[int], l: int, r: int, find: float ) -> int:
        # вернет индекс первого большего
        if l == r:
            if nums[l] > find:
                return l
            else:
                return l + 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= find:
                l = mid
                if nums[l + 1] >= find:
                    return l + 1
                continue
            elif nums[mid] > find:
                r = mid

        return l


