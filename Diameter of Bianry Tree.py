__author__ = 'yibeihuang'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        self._calcu(root)
        return self.diameter

    def _calcu(self, node):
        if not node:
            return 0
        l = self._calcu(node.left)
        r = self._calcu(node.right)
        self.diameter = max(self.diameter, (l+r))
        return max(l,r)+1

