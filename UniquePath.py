__author__ = 'yibeihuang'
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        if m==1 or n==1: return 1
        dp[0][2]=1
        dp[2][0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[m][n]