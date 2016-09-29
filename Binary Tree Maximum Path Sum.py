__author__ = 'yibeihuang'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    res = -100000
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        self.countMaxSum(root)
        return self.res

    def countMaxSum(self, root):
        if root==None: return 0

        leftSum = self.countMaxSum(root.left)
        rightSum = self.countMaxSum(root.right)

        rootSum = max(max(leftSum+root.val, rightSum+root.val), root.val)
        rootSum = max(rootSum, leftSum+root.val+rightSum)
        self.res = max(self.res, rootSum)
        return rootSum

# Driver program
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(10);
root.left.left  = TreeNode(20);
root.left.right = TreeNode(1);
root.right.right = TreeNode(-25);
root.right.right.left = TreeNode(3);
root.right.right.right = TreeNode(4);
sol = Solution()
print ("Max path sum is " , sol.maxPathSum(root))