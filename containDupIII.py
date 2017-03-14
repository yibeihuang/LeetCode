__author__ = 'yibeihuang'
def containsNearbyAlmostDuplicate( nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        tmp = dict()
        if k<= 0 or t<0: return False
        for i in range(len(nums)):
            val = nums[i]/(t+1)
            if i>k: del tmp[nums[i-k-1]/(t+1)]
            if val in tmp or (val+1 in tmp and abs(nums[i]-tmp[val+1])<=t) or (val-1 in tmp and abs(nums[i]-tmp[val-1])<=t): return True
            tmp[val] = nums[i]

        return False

nums = [1,3,1]
k = 1
t = 1
print(containsNearbyAlmostDuplicate(nums,k,t))

