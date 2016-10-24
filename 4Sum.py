__author__ = 'yibeihuang'
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums)<4: return []
        rst = list()
        i = 0
        while i < (len(nums)-3):
            tmp = self.threeSum(nums[i+1:], target-nums[i])
            res = [[nums[i]] + j for j in tmp]
            for ele in res:
                rst.append(ele)
            while nums[i]==nums[i+1] and i<len(nums)-3: i+=1
            i += 1
        return rst

    def threeSum(self, nums, target):
        res = list()
        nums.sort()
        if len(nums)<3: return []
        i = 0
        while i < (len(nums)-2):
            p1 = p2 = 1
            while p1+i<len(nums)-p2:
                if nums[i+p1]+nums[len(nums)-p2] + nums[i]==target:
                    res.append([nums[i],nums[i+p1],nums[len(nums)-p2]])
                    while i+p1<len(nums)-p2 and nums[i+p1]==nums[i+p1+1]: p1+=1
                    while i+p1<len(nums)-p2 and nums[len(nums)-p2]==nums[len(nums)-p2-1]: p2+=1
                    p1+=1
                    p2+=1
                    continue
                elif nums[i+p1]+nums[len(nums)-p2]+nums[i]>target:
                    p2 += 1
                else:
                    p1 += 1
            while nums[i]==nums[i+1] and i<len(nums)-2: i+=1
            i += 1
        return res

sol = Solution()
ee = sol.fourSum([-3,-2,-1,0,0,1,2,3],0)
print(ee)