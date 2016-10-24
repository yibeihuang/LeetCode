__author__ = 'yibeihuang'

def maximalSquare(matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        maxval = 0
        for i in range(len(dp[0])):
            dp[0][i]= int(matrix[0][i])
            maxval = max(maxval, dp[0][i])
        for j in range(len(dp)):
            dp[j][0] = int(matrix[j][0])
            maxval = max(maxval, dp[j][0])
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if matrix[i][j] == 1:
                    dim = min([dp[i-1][j-1],dp[i-1][j],dp[i][j-1]])
                    dp[i][j] = (math.sqrt(dim)+1)**2
                else:
                    dp[i][j] = 0
                maxval = max(maxval, dp[i][j])
        return maxval

matrix = ["10100","10111","11111","10010"]
print(maximalSquare(matrix))