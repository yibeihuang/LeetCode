__author__ = 'yibeihuang'
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst, currLst = [], []
        self.getPermute(rst, nums, currLst)
        return rst

    def getPermute(self, rst, nums, currLst):
        if nums==[]:
            rst.append(currLst)
            return rst
        for i in range(len(nums)):
            newlst = nums[:i]+nums[i+1:]
            self.getPermute(rst, newlst, currLst+[nums[i]])

sol = Solution()
nums = [1,2,3]
print(sol.permute(nums))