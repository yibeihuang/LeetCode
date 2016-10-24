__author__ = 'yibeihuang'

def getMoneyAmount(n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i][j] = min (i<=k<=j) { k + max(dp[i][k-1], dp[k+1][j]) }
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                val = float('inf')
                for k in range(i,j+1):
                    tmp = k+max(0 if k==i else dp[i][k-1], 0 if k==j else dp[k+1][j])
                    val = min(val, tmp)
                dp[i][j] = val

        return dp[1][n]

print(getMoneyAmount(4))