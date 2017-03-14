__author__ = 'yibeihuang'
def canJump(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1: return True
        step = nums[0]
        if step==0: return False
        for i in range(1,step+1):
            tmpLst = nums[i:]
            if canJump(tmpLst): return True
        return False

nums = [1,0,2]
print(canJump(nums))