__author__ = 'yibeihuang'
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None: return root
        prev = root
        rr = root.right
        curr = root.left
        while curr:
            nxt = curr.left
            tmp = curr.right
            curr.left, curr.right = rr, prev
            prev = curr
            curr, rr = nxt, tmp
        return prev

root = TreeNode(1)
root.left = TreeNode(2)
sol = Solution()
print(sol.upsideDownBinaryTree(root))