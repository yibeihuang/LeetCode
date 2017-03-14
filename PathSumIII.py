__author__ = 'yibeihuang'
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
        :rtype: int
        """
        # self.cnt = 0
        # tmp = sum
        # self.sum = sum
        # self.CountpathSum(root, tmp)
        # return self.cnt
        if root==None: return 0
        return self.CountpathSum(root, sum)+self.pathSum(root.left, sum)+self.pathSum(root.right, sum)

    def CountpathSum(self, root, sum):
        # if root==None: return
        # if root.val == sum: self.cnt+=1
        # origin = self.sum
        # self.CountpathSum(root.left, sum-root.val)
        # self.CountpathSum(root.left, origin)
        # self.CountpathSum(root.right, sum-root.val)
        # self.CountpathSum(root.right, origin)
#         Wrong answer!!! a lot of repeats
        if root==None: return 0
        cnt = 0
        if root.val == sum: cnt=1
        return cnt + self.CountpathSum(root.left, sum-root.val)+self.CountpathSum(root.right, sum-root.val)


# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(-3)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(2)
# root.right.right = TreeNode(1)
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
root.right.right.right.right= TreeNode(5)

sol = Solution()
print(sol.pathSum(root, 3))

