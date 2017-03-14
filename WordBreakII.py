__author__ = 'yibeihuang'
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.rst = []
        if len(s)==0: return []
        self.wordBK(s, wordDict, 0, "")
        return self.rst

    def wordBK(self, s, wordDict, start, tmpstr):
        if start == len(s):
            self.rst.append(tmpstr[1:])
            return
        for j in range(start+1, len(s)+1):
            if self._isValid(start, j, wordDict, s):
                prevStr, prevStart = tmpstr, start
                tmpstr+='{}{}'.format(' ', s[start:j])
                start = j
                self.wordBK(s, wordDict, start, tmpstr)
                tmpstr, start = prevStr, prevStart


    def _isValid(self, i, j, wordDict, s):
        if i>=0 and i<j and j<=len(s) and s[i:j] in wordDict:
            return True
        return False

sol = Solution()
s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(sol.wordBreak(s,wordDict))