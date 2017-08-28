__author__ = 'yibeihuang'
def minDistance( word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # always insert word1
        if len(word1)>len(word2):
            tmp = word1
            word1 = word2
            word2 = tmp
        if len(word1)==0: return len(word2)
        dp = [[0 for i in range(len(word1)+1)] for j in range(len(word2)+1)]
        for i in range(len(word2)+1):
            for j in range(len(word1)+1):
                if i==0: dp[i][j] = j
                elif j==0: dp[i][j] = i
                elif word2[i-1]==word1[j-1]:dp[i][j]=dp[i-1][j-1]
                else:
                    # replace, insert , delete
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[len(word2)][len(word1)]

word1 = "ab"
word2 = "cd"
minDistance(word1,word2)