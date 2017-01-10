__author__ = 'yibeihuang'

import sys

class Solution(object):
    def buildGraph(self):
        firstline = 0
        self.theGraph = dict()
        for line in sys.stdin:
            if firstline==0:
                self.src, self.dst = line.split(' ')[0], line.split(' ')[1]
                firstline = 1
            else:
                node = line.split(':')[0]
                successor = line.split(':')[1]
                if node in self.theGraph:
                    for i in successor.split(' ')[1:]:
                        self.theGraph[node].add(i)
                else:
                    self.theGraph[node]=set()
                    for i in successor.split(' ')[1:]: self.theGraph[node].add(i)

    def dfs(self, curr, destination, path, visited):
        visited.add(curr)
        prepath = path
        path.append(curr)
        if curr==destination: self.rst.append(''.join(path))
        else:
            for i in self.theGraph[curr]:
                if i not in visited: self.dfs(i, destination, path,visited)
        path = prepath
        visited.remove(curr)
    def findPath(self):
        self.buildGraph()
        self.rst = []
        visited = set()
        self.dfs(self.src, self.dst, [], visited)

sol = Solution()
sol.findPath()