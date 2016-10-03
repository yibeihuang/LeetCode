__author__ = 'yibeihuang'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.calculate(0, root)
        return self.sum

    def calculate(self, tmp, root):
        if root==None: return 0
        tmp = tmp*10+ root.val
        if root.right==None and root.left==None:
            self.sum += tmp
            return tmp
        self.calculate(tmp, root.left)
        self.calculate(tmp, root.right)
        # return self.calculate(tmp, root.left)+self.calculate(tmp, root.right)

#construct tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5);
root.left.left  = TreeNode(3);
root.left.right = TreeNode(4);
root.right.right = TreeNode(6);
root.left.left.right = TreeNode(7)

sol = Solution()
print(sol.sumNumbers(root))