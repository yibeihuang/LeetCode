__author__ = 'yibeihuang'
# def lengthLongestPath(input):
#         """
#         :type input: str
#         :rtype: int
#         """
#         maxpath, stack = 0, []
#         count = 0
#         lines = input.split('\n')
#         while lines:
#             curr, i = lines.pop(0), 0
#             while curr[i]=='\t':
#                 i+=1
#             while i!= count:
#                 stack.pop()
#                 count -= 1
#             stack.append(curr.split('\t')[-1])
#             count += 1
#             if '.' in curr and curr.index('.')!=len(curr)-1:
#                 maxpath = max(maxpath, len(''.join(stack))+count-1)
#                 stack.pop()
#                 count -= 1
#         return maxpath
def lengthLongestPath(input):
    maxlen = 0
    pathlen = {0: 0}
    for line in input.splitlines():
        name = line.lstrip('\t')
        depth = len(line) - len(name)
        if '.' in name:
            maxlen = max(maxlen, pathlen[depth] + len(name))
        else:
            pathlen[depth + 1] = pathlen[depth] + len(name) + 1
    return maxlen

inputt = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(lengthLongestPath(inputt))