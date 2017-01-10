__author__ = 'yibeihuang'
def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    p1, p3, p2 = 0,0, len(nums)-1
    while p1<p2:
        if nums[p1]==0 and p1==p3:
            p1, p3= p1+1, p3+1
        elif nums[p1]==0 and p1>p3:
            tmp = nums[p3]
            nums[p3]=0
            nums[p1]=tmp
            p1, p3=p1+1, p3+1
        elif nums[p2]==2: p2-=1
        elif nums[p2]==0:
            tmp = nums[p3]
            nums[p3]=0
            nums[p2]=tmp
            p3 +=1
        elif nums[p1]==2:
            tmp = nums[p2]
            nums[p2] = nums[p1]
            nums[p1]=tmp
            p2 -= 1
        else: p1+=1
    return nums

nums = [2,0,0]
print(sortColors(nums))