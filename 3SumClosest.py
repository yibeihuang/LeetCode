__author__ = 'yibeihuang'
def threeSumSmaller( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        rst = []
        for i in range(len(nums)-2):
            lo = i+1
            hi = lo+1
            if nums[i]+nums[lo]+nums[hi]>=target: return len(rst)
            # if lo>1 and nums[lo]==nums[lo-1]: continue
            while lo<hi and hi<len(nums):
                while hi<len(nums) and nums[i]+nums[lo]+nums[hi]<target:
                    # if [nums[i],nums[lo],nums[hi]] not in rst: rst.append([nums[i],nums[lo],nums[hi]])
                    rst.append([nums[i],nums[lo],nums[hi]])
                    hi+=1
                lo+=1
                hi=lo+1
        return len(rst)

nums = [0,-4,-1,1,-1,2]
target = -5
print(threeSumSmaller(nums,target))
