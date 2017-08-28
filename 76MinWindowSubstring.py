__author__ = 'yibeihuang'
import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s)<len(t): return ""
        needs, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for (idx, ele) in enumerate(s, 1):
            if ele in needs and needs[ele]>0:
                missing -= 1
            if ele in needs: needs[ele] -= 1
            while i<idx and not missing:
                if not J or idx-i < J-I:
                    I, J = i, idx
                if s[i] not in t:
                    i += 1
                else:
                    needs[s[i]] += 1
                    if needs[s[i]] > 0:
                        missing += 1
                    i += 1
        return s[I:J]


sol = Solution()
s = "bbaac"
t = "aba"
print(sol.minWindow(s, t))