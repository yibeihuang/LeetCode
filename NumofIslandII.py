__author__ = 'yibeihuang'
class Node(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        nodeset = dict()
        res = []
        for (i,j) in positions:
            cnt = 0
            node = self.makeset(Node(i,j))
            nodeset[(i,j)] = node
            for idx in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                if idx in nodeset:
                    x,y = idx
                    node1,node2 = nodeset[(i,j)], nodeset[(x,y)]
                    self.union(node1,node2)
            resdict = dict()
            for (i,j) in nodeset:
                parent = self.find(nodeset[(i,j)])
                if parent.data not in resdict:
                    resdict[parent.data]=1
                    cnt+=1
            res.append(cnt)
        return res

    def makeset(self, node):
        node.parent=node
        return node

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1==p2: return
        elif p1.rank>p2.rank:p2.parent=p1
        else:
            p1.parent = p2
            if p1.rank==p2.rank:p2.rank+=1

    def find(self, node):
        if node.parent==node:
            return node
        node.parent = self.find(node.parent)
        return node.parent



sol = Solution()
sol.numIslands2(3,3,[[0,0],[0,1],[1,2],[2,1]])