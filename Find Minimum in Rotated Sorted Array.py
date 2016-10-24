__author__ = 'yibeihuang'
def findMin( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1, p2 = 0, len(nums)-1
        while p1<p2 and nums[p1]>nums[p2]:
            mid = (p1+p2)/2
            if nums[mid]<nums[p1]:
                p2=mid
            else:
                p1=mid+1

        return nums[p1]



nums = [5,6,0,1,2,3]
print(findMin(nums))