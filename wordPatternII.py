__author__ = 'yibeihuang'
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # self.setzip, self.setPat, self.setStr = set(), set(pattern), set()
        return self.backTrack(pattern, 0, 0, str, set(), set(), set())

    def backTrack(self, pattern, pstart, sstart, str, setZip, setPat, setStr):
        if  pstart==len(pattern):
            return sstart==len(str)
            # return len(set(zip(pattern, strLst))==len(set(pattern))==len(set(strLst)) and len(pattern)==len(strLst)
        for i in range(sstart+1, len(str)+1):
            tmp1, tmp2, tmp3 = setStr.copy(), setPat.copy(), setZip.copy()
            tmp1.add(str[sstart:i])
            tmp2.add(pattern[pstart])
            tmp3.add((str[sstart:i], pattern[pstart]))
            if len(tmp1)==len(tmp2)==len(tmp3):
                if self.backTrack(pattern, pstart+1, i, str, tmp3, tmp2, tmp1):
                    return True
        return False



sol = Solution()
pattern = "aba"
str = "121"
print(sol.wordPatternMatch(pattern, str))