__author__ = 'yibeihuang'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return False
        if root.left==None and root.right==None: return True
        if root.left and root.right:
            if root.left.val<root.val and root.right.val>root.val:
                return (self.isValidBST(root.left) and self.isValidBST(root.right))
            else:
                return False
        if root.left==None and root.right!=None:
            if root.right.val>root.val:
                return self.isValidBST(root.right)
            else:
                return False
        if root.right==None and root.left!=None:
            if root.left.val<root.val:
                return self.isValidBST(root.left)
            else:
                return False

#construct tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6);
root.left.left  = TreeNode(2);
root.left.right = TreeNode(4);
root.right.right = TreeNode(7);

sol = Solution()
print(sol.isValidBST(root))