__author__ = 'yibeihuang'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while root or len(stack)>=1:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

#construct tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5);
root.left.left  = TreeNode(3);
root.left.right = TreeNode(4);
root.right.right = TreeNode(6);

sol = Solution()
print(sol.inorderTraversal(root))