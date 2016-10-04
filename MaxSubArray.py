__author__ = 'yibeihuang'
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sofar = max_now = nums[0]
        for i in range(1, len(nums)):
            max_now = max(nums[i], max_now+nums[i])
            max_sofar = max(max_sofar, max_now)
        return max_sofar