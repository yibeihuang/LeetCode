__author__ = 'yibeihuang'
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = [0 for i in range(len(nums) - k + 1)]
        pos = 0
        window = []
        for i in range(len(nums)):
            # remove out of range elements
            while window and window[0]<i-k+1:
                window.pop(0)
            # remove small elements
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
            if i>=k-1:
                res[pos] = nums[window[0]]
                pos += 1
        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
sol = Solution()
print(sol.maxSlidingWindow(nums, k))
