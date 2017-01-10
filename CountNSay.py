__author__ = 'yibeihuang'
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1: return str(1)
        i = 1
        newnum = 1
        while i<n:
            newnum = int(self.transForm(newnum))
            i += 1
        return str(newnum)

    def transForm(self,num):
        rst = ''
        count = 1
        prev = num%10
        num = num/10
        while num:
            tmp = num%10
            if tmp==prev:
                count+=1
            else:
                rst = '%s%s'%(str(count), str(prev)) +rst
                count = 1
            prev = tmp
            num = num/10
        rst = '%s%s'%(str(count), str(prev)) +rst
        return rst

sol = Solution()
print(sol.countAndSay(2))