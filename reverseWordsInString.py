__author__ = 'yibeihuang'
## consider in the C++ way
# class Solution(object):
#     def reverseWords(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         while len(s)>0:
#             if s[0]==' ':
#                 s=s[1:]
#         while len(s)>0:
#             if s[-1]==' ':
#                 s=s[:-1]
#         if len(s) == 0: return ''
#         flag = 0
#         i = 0
#         while i<len(s): # delete unneccesary space
#             j = len(s)
#             if s[i]==' ' and flag ==0:
#                 flag = 1
#                 i += 1
#             if s[i] ==' ' and flag==1:
#                 s=s[:i]+s[i+1:]
#             if s[i]!=' ':
#                 flag = 0
#                 i += 1
#         s = self.subreverse(s)
#         s = s.split()
#         for i in range(len(s)):
#             s[i] = self.subreverse(s[i])
#         return ' '.join(s)
#
#     def subreverse(self, s):
#         length = len(s)
#         s = list(s)
#         for i in range(length//2):
#             j = length - i -1
#             tmp = s[i]
#             s[i] = s[j]
#             s[j] = tmp
#         return ''.join(s)

class Solution(object):
    # def reverseWords(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     return (' '.join(s.split()[::-1]))
    def reverseWords(self, s):
        lsts = list(s)
        lsts = self.ReverseW(lsts)
        s = ''.join(lsts)
        chunks = s.split(' ')
        for ele in chunks:
            ele = ''.join(self.ReverseW(list(ele)))
        s = ' '.join(chunks)

    def ReverseW(self, s):
        p1,p2 = 0, len(s)-1
        while p1<p2:
            s[p1],s[p2] = s[p2],s[p1]
            p1+=1
            p2-=1
        return s


s = 'a b'
sol = Solution()
sol.reverseWords(s)
print(s)