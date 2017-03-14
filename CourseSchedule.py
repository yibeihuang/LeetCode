__author__ = 'yibeihuang'
import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.graph = collections.defaultdict(list)
        for (i,j) in prerequisites:
            self.graph[i].append(j)
            if j not in self.graph:self.graph[j]
        self.visited = set()
        self.currvisit = set()
        for key in self.graph:
            if key not in self.visited:
                if self._checkFinish(key)==False:return False
        return True

    def _checkFinish(self, key):
        if key in self.currvisit:return False
        self.visited.add(key)
        self.currvisit.add(key)
        for val in self.graph[key]:
            if self._checkFinish(val)==False: return False
        self.currvisit.remove(key)
num = 2
courses = [[0,1],[1,0]]
sol = Solution()
print(sol.canFinish(num, courses))