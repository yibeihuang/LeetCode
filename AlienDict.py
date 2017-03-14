__author__ = 'yibeihuang'
import collections
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        self.graph = collections.defaultdict(list)
        self.buildGraph(words)
        self.topologySort()

    def buildGraph(self, words):
        for pair in zip(words,words[1:]):
            for a,b in zip(*pair):
                if a!=b:
                    self.graph[a].append(b)
                    break
        for pair in zip(words,words[1:]):
            for a,b in zip(*pair):
                if a not in self.graph:self.graph[a]
                if b not in self.graph:self.graph[b]

    def topologySort(self):
        self.visited = set()
        self.stack = []
        for key in self.graph:
            if key not in self.visited:
                self._tsUtil(key)
        res = ""
        while self.stack:
            res+=self.stack.pop()
        return res

    def _tsUtil(self, key):
        self.visited.add(key)
        for i in self.graph[key]:
            if i not in self.visited:
                self._tsUtil(i)
        self.stack.append(key)

words = ["wrt","wrf","er","ett","rftt"]
sol = Solution()
print(sol.alienOrder(words))