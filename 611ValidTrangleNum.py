__author__ = 'yibeihuang'
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0: return 0
        res = 0
        nums.sort()
        for i in range(len(nums)-2):
            a = nums[i]
            for j in range(i+1, len(nums)-1):
                b, start, end = nums[j], j+1, len(nums)-1
                while end>j and nums[end]>=a+b: end -= 1
                while start<end and nums[start]<=b-a: start += 1
                res += end - start + 1
        return res

sol = Solution()
nums = [2,2,3,4]
print(sol.triangleNumber(nums))