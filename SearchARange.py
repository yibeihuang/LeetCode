__author__ = 'yibeihuang'
def searchRange(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        p1, p2 = 0, len(nums)-1
        mid = (p1+p2)//2
        while (nums[p1]!=target or nums[p2]!=target) and p1<p2:
            mid = (p1+p2)//2
            if nums[mid] < target:
                p1 = mid+1
            elif nums[mid] > target:
                p2 = mid-1
            else:
                break
        if nums[mid]!=target: return [-1,-1]
        while nums[p1]!=target and p1<mid:
            p1+=1

        while nums[p2]!=target and p2>mid:
            p2-=1
        return [p1, p2]

nums = [0,0,1,2,3,3,3,4,5]
target = 3
print(searchRange(nums, target))