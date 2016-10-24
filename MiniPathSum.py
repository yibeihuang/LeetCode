__author__ = 'yibeihuang'

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid==None: return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i!=0 and j!=0: dp[i][j] = min((dp[i-1][j]+grid[i][j]), (dp[i][j-1]+grid[i][j]))
                if i==0 and j!=0: dp[i][j] = dp[i][j-1] + grid[i][j]
                if i!=0 and j==0: dp[i][j] = dp[i-1][j] + grid[i][j]
                if i==0 and j==0: dp[i][j] = grid[i][j]
        return dp[-1][-1]