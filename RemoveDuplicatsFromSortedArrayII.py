__author__ = 'yibeihuang'
def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for ele in nums:
            if i<2 or ele>nums[i-2]:
                nums[i] = ele
                i+=1
        return i

nums = [1,1,1,1,1,3,3,3]
pos = removeDuplicates(nums)
print(nums[:pos])
