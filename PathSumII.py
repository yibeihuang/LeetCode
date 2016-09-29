__author__ = 'yibeihuang'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(node, currsum, currlst):
            if node.left==None and node.right==None:
                if node.val==currsum:
                    rst.append(currlst)
            if node.left:
                dfs(node.left, currsum-node.val, currlst+[node.left.val])
            if node.right:
                dfs(node.right, currsum-node.val, currlst+[node.right.val])
        rst = []
        if root==None: return []
        dfs(root, sum, [root.val])
        return rst

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(3)
a.left = b
a.right = c
b.right = d
c.left = e

sol = Solution()
print(sol.pathSum(a, 11))