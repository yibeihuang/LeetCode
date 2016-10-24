__author__ = 'yibeihuang'
# def decodeString(s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         rst = []
#         if s=="": return ""
#         stack=[]
#         for ele in s:
#             if ele==']':
#                 i = stack.pop()
#                 tmp=[]
#                 while i!='[':
#                     tmp=[i]+tmp
#                     i = stack.pop()
#                 count = []
#                 while stack and stack[-1].isdigit():
#                     count=[stack.pop()]+count
#                 count= int(''.join(count))
#                 string=''.join(tmp)
#                 tmp=[]
#                 while count>0:
#                     tmp.append(string)
#                     count -= 1
#                 stack.append(''.join(tmp))
#             else:
#                 stack.append(ele)
#         return ''.join(stack)

import re
def decodeString(s):
    while '[' in s:
        s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
    return s


s="3[le]2[a3[c]]"
print(decodeString(s))