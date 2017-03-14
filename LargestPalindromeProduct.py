__author__ = 'yibeihuang'
import math
class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 9
        upperbound, lowerbound = 10**(n)-1, 10**(n-1)
        maxNum = upperbound*upperbound
        firsthalf = maxNum/(10**(n))
        # print firsthalf
        # findPalin = False
        while True:
            tmpPalin = self.createPalin(firsthalf)
            for i in range(upperbound, lowerbound-1,-1):
                if tmpPalin>maxNum: break
                if (tmpPalin/i)>upperbound : break
                if tmpPalin%i==0: return tmpPalin%1337
            firsthalf-=1

    def createPalin(self, half):
        half = str(half) + str(half)[::-1]
        return int(half)

sol = Solution()
n = 2
print(sol.largestPalindrome(n))