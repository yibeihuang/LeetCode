__author__ = 'yibeihuang'
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return []
        row, col = len(nums), len(nums[0])
        if r*c != row*col: return nums
        i, j = 0, 0
        res = [[0 for k in range(c)] for p in range(r)]
        while i<r and j<c:
            if j<c:
                nm = i*c+j
                res[i][j] = nums[nm/col][nm%col]
                j += 1
                if j==c:
                    j = 0
                    i += 1
        return res

sol = Solution()
nums = [[1,2],[3,4],[5,6],[7,8]]
r, c = 2, 4
print(sol.matrixReshape(nums, r, c))