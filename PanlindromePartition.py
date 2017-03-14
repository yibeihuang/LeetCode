__author__ = 'yibeihuang'
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.rst = []
        self.tmp = []
        self.PartitionUtil(s)
        return self.rst

    def PartitionUtil(self, s):
        if s=='':
            val = self.tmp[:]
            self.rst.append(val)
        for k in range(1,len(s)+1):
            if self.isPanlindrome(s[:k]):
                self.tmp.append(s[:k])
                self.PartitionUtil(s[k:])
                self.tmp.pop()

    def isPanlindrome(self, string):
        if len(string)==0: return False
        i, j = 0, len(string)-1
        while i<=j:
            if string[i]!=string[j]:return False
            i+=1
            j-=1
        return True

s = Solution()
print(s.partition("aab"))