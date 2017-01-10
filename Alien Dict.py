__author__ = 'yibeihuang'
# class Node(object):
#     def __init__(self, value):
#         self.val = value
#         self.nxt = None
#
# class Solution(object):
#     def alienOrder(self, words):
#         """
#         :type words: List[str]
#         :rtype: str
#         """
#         rst = []
#         self.graph, self.roots = dict(), dict()
#         self.buildGraph(words)
#         for i in self.roots:
#             start = self.roots[i]
#             rst.append(i)
#             break
#         i = self.roots[i]
#         while i.nxt:
#             rst.append(i.nxt.val)
#             i = i.nxt
#         return ''.join(rst)
#
#     def buildGraph(self, words):
#         for i in range(len(words)-1):
#             for j in range(min(len(words[i]),len(words[i+1]))):
#                 if words[i][j]==words[i+1][j]: continue
#                 if words[i][j] in self.graph:
#                     if words[i+1][j] in self.graph:
#                         self.graph[words[i][j]].nxt=self.graph[words[i+1][j]]
#                         if words[i+1][j] in self.roots: del self.roots[words[i+1][j]]
#                     else:
#                         self.graph[words[i+1][j]]=Node(words[i+1][j])
#                         self.graph[words[i][j]].nxt=self.graph[words[i+1][j]]
#                 else:
#                     node=Node(words[i][j])
#                     self.graph[words[i][j]]=node
#                     self.roots[words[i][j]]=node
#                     if words[i+1][j] in self.graph:
#                         self.graph[words[i][j]].nxt=self.graph[words[i+1][j]]
#                         if words[i+1][j] in self.roots: del self.roots[words[i+1][j]]
#                     else:
#                         self.graph[words[i+1][j]]=Node(words[i+1][j])
#                         self.graph[words[i][j]].nxt=self.graph[words[i+1][j]]
#
# sol = Solution()
# words=["wrt","wrf","er","ett","rftt"]
# print(sol.alienOrder(words))


def alienOrder( words):
    less = []
    for pair in zip(words, words[1:]):
        for a, b in zip(*pair):
            if a != b:
                less += a + b,
                break
    chars = set(''.join(words))
    order = []
    while less:
        free = chars - set(zip(*less)[1])
        if not free:
            return ''
        order += free
        less = filter(free.isdisjoint, less)
        chars -= free
    return ''.join(order + list(chars))

words=["wrt",
  "wrf",
  "er",
  "ett",
  "rftt"]

print(alienOrder(words))