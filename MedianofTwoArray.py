__author__ = 'yibeihuang'
def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1)>len(nums2): nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        imin, imax = 0, m
        while imin<=imax:
            i = (imin+imax)/2
            j = (m+n+1)/2-i
            if i>0 and nums1[i-1]>nums2[j]:
                imax = i-1
            elif i<m and nums1[i]<nums2[j-1]:
                imin = i+1
            else:
                if i==0:maxLeft = nums2[j-1]
                elif j==0: maxLeft = nums1[i-1]
                else:maxLeft=max(nums1[i-1],nums2[j-1])
                if (m+n)%2==1:return maxLeft
                if i==m:minRight = nums2[j]
                elif j==n:minRight = nums1[i]
                else:minRight = min(nums1[i],nums2[j])

                return (maxLeft+minRight)/2.0

nums1 = [1]
nums2 = [1]
print(findMedianSortedArrays(nums1,nums2))