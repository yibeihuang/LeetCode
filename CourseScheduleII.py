__author__ = 'yibeihuang'
import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.stack = []
        self.graph = collections.defaultdict(list)
        for (i,j) in prerequisites:
            self.graph[j].append(i)
            if i not in self.graph:self.graph[i]
        self.visited = set()
        for key in self.graph:
            if self.graph[key]==[]:continue
            if key not in self.visited:
                currvisit = set()
                if self._checkFinish(key, currvisit)==False:return []
        return self.stack[::-1]

    def _checkFinish(self, key, currvisit):
        if key in currvisit:return False
        self.visited.add(key)
        currvisit.add(key)
        for val in self.graph[key]:
            if val not in self.visited:
                if self._checkFinish(val, currvisit)==False: return False
        self.stack.append(key)
        currvisit.remove(key)

num = 4
pre = [[1,0],[2,0],[3,1],[3,2]]
sol = Solution()
print(sol.findOrder(num, pre))