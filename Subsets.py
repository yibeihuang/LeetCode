__author__ = 'yibeihuang'
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.Sets(nums, [], 0)
        return self.res

    def Sets(self, nums, tmp, start):
        prev = tmp[:]
        self.res.append(prev)
        # if start==len(nums): return
        for i in range(start,len(nums)):
            tmp.append(nums[i])
            self.Sets(nums, tmp, i+1)
            tmp = prev[:]
        return

sol = Solution()
nums = [1,2,3]
print(sol.subsets(nums))