__author__ = 'yibeihuang'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        self.res = []
        self.maxCount, self.count = 0, 0
        self.currVal = 0
        self._inorder(root)
        return self.res

    def _inorder(self, node):
        if not node: return
        self._inorder(node.left)
        if node.val!=self.currVal:
            self.currVal = node.val
            self.count = 0
        self.count += 1
        if self.count == self.maxCount:
            self.res.append(self.currVal)
        if self.count > self.maxCount:
            self.maxCount = self.count
            self.res = [self.currVal]
        self._inorder(node.right)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
sol = Solution()
print(sol.findMode(root))


