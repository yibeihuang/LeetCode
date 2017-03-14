__author__ = 'yibeihuang'
import collections
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.graph = collections.defaultdict(set)
        self.rst = dict()
        minht = float("inf")
        for i,j in edges:
            self.graph[i].add(j)
            self.graph[j].add(i)
        for k in self.graph:
            self.queue = [k,'flag']
            self.visited = set()
            height = 0
            while self.queue:
                node = self.queue.pop(0)
                if node=='flag':
                    height+=1
                    if self.queue:self.queue.append('flag')
                    continue
                self.visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in self.visited:
                        self.queue.append(neighbor)

            self.rst[k]=height
            minht = min(minht, height)
        res = []
        for k in self.rst:
            if self.rst[k]==minht:res.append(k)
        return res


sol = Solution()
print(sol.findMinHeightTrees(4,[[1,0],[1,2],[1,3]]))