__author__ = 'yibeihuang'
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        p = 0
        curr = nums[p:p+k]
        summ = tmp = sum(nums[p:p+k])
        while p<len(nums)-k:
            tmp = tmp-curr[0]+nums[p+k]
            if tmp>summ:
                summ = tmp
            curr.pop(0)
            curr.append(nums[p+k])
            p += 1
        return summ/float(k)

sol = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(sol.findMaxAverage(nums, k))