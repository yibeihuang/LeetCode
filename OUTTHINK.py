__author__ = 'yibeihuang'

class Solution(object):
    def findnum(self, num, p, q):
        rst = []
        for i in range(1,num+1):
            tmp = ''
            if i%p==0 or i%q==0:
                if str(p) in str(i) or str(q) in str(i):
                    tmp = 'OUTTHINK'
                else:
                    tmp = 'OUT'
            elif str(p) in str(i) or str(q) in str(i):
                tmp = 'THINK'
            else:
                tmp = str(i)
            rst.append(tmp)
        return ','.join(rst)

sol = Solution()
print(sol.findnum(7,2,3))