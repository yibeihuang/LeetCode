__author__ = 'yibeihuang'
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.total = 0
        for i in nums:
            self.calcuSum(target-i, nums)
        return self.total

    def calcuSum(self, target, nums):
        if target==0:
            self.total+=1
            return
        if target<0: return
        for i in nums:
            return self.calcuSum( target-i, nums)

sol = Solution()
num = [1,2,3]
target = 4
print(sol.combinationSum4(num, target))