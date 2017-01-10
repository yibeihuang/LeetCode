__author__ = 'yibeihuang'

class Solution(object):
    def dfs(self, currt, destination, path, visited):
            visited.add(currt)
            path.append(currt)
            if currt==destination: self.rst.append(''.join(path))
            else:
                if currt in self.theGraph:
                    for i in self.theGraph[currt]:
                        if i not in visited: self.dfs(i, destination, path, visited)
            visited.remove(currt)
            path.pop()

    def findPath(self, src, dst, graph):
        self.theGraph = graph
        self.rst = []
        visited = set()
        self.dfs(src, dst, [], visited)
        return self.rst


src = 'A'
dst = 'J'
graph = {'A': ['B', 'C'],
     'B': ['C', 'E', 'G'],
     'C': ['A', 'F'],
     'D': ['C', 'J'],
     'F': ['B', 'H'],
     'G': ['C', 'D'],
     'H': ['A', 'B', 'F', 'I'],
     'I': ['B']
}
sol = Solution()
print(sol.findPath(src,dst,graph))
