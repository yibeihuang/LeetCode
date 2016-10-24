__author__ = 'yibeihuang'

# def partition(nums, left, right):
#     pivot = nums[left]
#     l, r = left+1, right
#     while l<=r:
#         if nums[l]<pivot and nums[r]>pivot:
#             tmp = nums[l]
#             nums[l] = nums[r]
#             nums[r] = tmp
#             l += 1
#             r -= 1
#         if nums[l] >= pivot: l+=1
#         if nums[r] <= pivot: r-=1
#     tmp = nums[left]
#     nums[left] = nums[r]
#     nums[r] = tmp
#     return r
#
# def findKthLargest(nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         if len(nums)==1: return nums[0]
#         left, right = 0, len(nums)-1
#         while True:
#             pos = partition(nums,left, right)
#             if pos== k-1: return  nums[pos]
#             elif pos>k-1: right=pos-1
#             else: left=pos+1

def findKthLargest(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==1: return nums[0]
        pivot = nums[0]
        left,right = [],[]
        for i in range(1,len(nums)):
            if nums[i]>=pivot: left.append(nums[i])
            else: right.append(nums[i])
        if len(left)==k-1: return pivot
        elif len(left)<k-1: return findKthLargest(right, k-1-(len(left)))
        else: return findKthLargest(left,k)


nums = [1,2,3,4,5,6]
k = 1
rst = findKthLargest(nums,k)
print(rst)