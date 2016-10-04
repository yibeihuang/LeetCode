__author__ = 'yibeihuang'

# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: Set[str]
#         :rtype: bool
#         """
#         length = 0
#         for key in wordDict: # get the length of the longest word in dict
#             if len(key) > length:
#                 length=len(key)
#         if len(s) == 0: return True
#         for i in range(length):
#             if s[:i+1] in wordDict:
#                 return self.wordBreak(s[i+1:], wordDict)
#         return False
#
# s = 'aaaaaaa'
# wordDict = {'aaaa', 'aaa'}
#
# print(Solution().wordBreak(s,wordDict))

# Dynamic Programming
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i-1,-1,-1):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break
        return dp[len(s)]