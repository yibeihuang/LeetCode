__author__ = 'yibeihuang'
# import re

class Solution(object):
    def filter(self, instr):
        if instr==None or len(instr)==0:
            return instr
        strlist = instr.split('|')
        if len(strlist)<=1: return instr
        processed = [None for i in range(len(strlist))]
        for i in range(len(strlist)):
            curr = self.recon(strlist[i])
            processed[i] = curr
            for j in range(i):
                if processed[j]==None or j==i: continue
                prev = processed[j]
                if prev == curr:
                    if len(strlist[i]) > len(strlist[j]): processed[j]=None
                    if len(strlist[i]) <= len(strlist[j]): processed[i]=None
                elif prev in curr: processed[j] = None
                elif curr in prev: processed[i] = None
        rst = []
        for i in range(len(processed)):
            if processed[i]==None or len(processed[i])==0: continue
            ele = ' '.join(strlist[i].split()) +'|'
            rst.append(ele)
        strr = ''.join(rst)
        return strr[:-1]

    def recon(self, singlestr):
        # singlestr = singlestr.strip()
        # re.sub('\s+',' ',singlestr)
        singlestr = ' '.join(singlestr.split())
        tmp = []
        for i in singlestr:
            if i ==' ':
                tmp.append(i)
            elif i.isalnum():
                tmp.append(i.lower())
        return ''.join(tmp)

s = """IBM cognitive computing|IBM \"cognitive\"
     computing is a revolution| ibm cognitive  computing|IBM Cognitive Computing' is a revolution?|
         dfhakd    jsfakjdf"""
sol = Solution()
rst = sol.filter(s)
print(rst)