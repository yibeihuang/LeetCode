__author__ = 'yibeihuang'
def increasingTriplet(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = []
        if len(nums)<3: return False
        res.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i]==res[-1]: continue
            elif nums[i]>res[-1] and len(res)<3:
                res.append(nums[i])
                if len(res)==3:
                    return True
            else:
                while len(res)>0 and nums[i] <= res[-1]:
                    res.pop()
                res.append(nums[i])
        if len(res)==3:
            return True
        return False

nums=[1,2,0,3]
print(increasingTriplet(nums))