__author__ = 'yibeihuang'
def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        nums.sort()
        if len(nums)<3: return []
        for i in range(len(nums)-2):
            p1 = p2 = 1
            while p1+i<len(nums)-p2:
                if nums[i+p1]+nums[len(nums)-p2] + nums[i]==0:
                    res.append([nums[i],nums[i+p1],nums[len(nums)-p2]])
                    break
                elif nums[i+p1]+nums[len(nums)-p2]+nums[i]>0:
                    p2 += 1
                else:
                    p1 += 1
        return res

nums = [-1,0,1,2,-1,-4]

print(threeSum(nums))