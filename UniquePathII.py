__author__ = 'yibeihuang'
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for i in range(col+1)] for j in range(row+1)]
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]==1: return 0
        if row==1 or col==1: return 1
        dp[0][2] = 1
        dp[2][0] = 1
        for i in range(1, row+1):
            for j in range(1, col+1):
                if obstacleGrid[i-1][j-1] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                if obstacleGrid[i-1][j-1] == 1:
                    dp[i][j] = 0
        return dp[row][col]