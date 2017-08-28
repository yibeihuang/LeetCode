__author__ = 'yibeihuang'
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.s = s
        self.res = []
        if len(s)<4: return res
        self.bk([], 0, len(s))
        return self.res

    def bk(self, curr, start, end):
        if start==end:
            self.res.append('.'.join(curr))
        for i in range(start+1, end+1):
            if int(self.s[start:i])<=255 and len(curr)+end-i>=4:
                tmp = curr.append(self.s[start:i])
                self.bk(tmp, i, end)

sol = Solution()
print(sol.restoreIpAddresses("0000"))