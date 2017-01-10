__author__ = 'yibeihuang'
class Solution:
    def reverseWords(self, s):
        # self.reverse(s)
        s[:]=s[:][::-1]
        i,p = 0,0
        while i<len(s):
            if s[i]!=' ' and i!=len(s)-1: i+=1
            else:
                s[p:i]=s[p:i][::-1]
                # self.reverse(s[p:i])
                p,i=i+1,i+1

    # def reverse(self,s):
    #     i,j=0,len(s)-1
    #     while i<j:
    #         s[i],s[j]=s[j],s[i]
    #         i+=1
    #         j-=1


s='the sky is blue'
s=list(s)
sol = Solution()
sol.reverseWords(s)
print(s)