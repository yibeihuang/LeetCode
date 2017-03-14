__author__ = 'yibeihuang'
def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # compare, insert, move the rest of nums1
        p1, p2 = m-1, n-1
        total = m+n-1
        while total>=0:
            if p1>=0 and p2>=0 and nums1[p1]>=nums2[p2]:
                nums1[total] = nums1[p1]
                total-=1
                p1-=1
            elif p1>=0 and p2>=0 and nums1[p1]<nums2[p2]:
                nums1[total] = nums2[p2]
                total-=1
                p2-=1
            elif p1<0 and p2>=0:
                nums1[:total+1]=nums2[:p2+1]
                return
            elif p2<0 and p1>=0:
                nums1[:total+1]=nums1[:p1+1]
                return

nums1 = [1]
nums2 = []
merge(nums1,1,nums2,0)
print(nums1)