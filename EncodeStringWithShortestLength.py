__author__ = 'yibeihuang'
def encode( s):
        """
        :type s: str
        :rtype: str
        """
        dp = [['' for i in range(len(s))] for j in range(len(s))]
        for l in range(len(s)):
            for i in range(0, len(s)-l):
                j = i+l
                if l<4:
                    dp[i][j]=s[i:j+1]
                else:
                    dp[i][j] = s[i:j+1]
                    for k in range(i+1,j):
                        if len(dp[i][k])+len(dp[k+1][j]) < len(dp[i][j]):
                            dp[i][j] = dp[i][k] + dp[k+1][j]
                    #  Loop for checking if string can itself found some pattern in it which could be repeated.
                    for k in range(1, l):
                        orig = s[i:j+1]
                        substr = s[i:i+k]
                        if len(orig)%len(substr)==0 and orig.replace(substr, '')=='':
                            tmp = str(len(orig)/len(substr))+'['+substr+']'
                            if len(tmp)<len(dp[i][j]):dp[i][j] = tmp
        return dp[0][len(s)-1]

s = "abbbabbbcabbbabbbc"
print(encode(s))