__author__ = 'yibeihuang'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # def flatten(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: void Do not return anything, modify root in-place instead.
    #     """
    #     self.list = self.preorder(root)
    #     if len(self.list)==0: return []
    #     for i in range(len(self.list)):
    #         node = TreeNode(self.list[i])
    #         if list[i+1]:
    #             node.right=TreeNode(self.list[i+1])
    #
    # def preorder(self, root):
    #     self.list = []
    #     if root: self.list.append(root.val)
    #     else: return []
    #     self.preorder(root.left)
    #     self.preorder(root.right)
    #     return self.list
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None: return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            p = root.right
            root.right = tmp = root.left
            while tmp.right:
                tmp = tmp.right
            tmp.right = p
            root.left = None
        return root

def postorder(root):
    #print(root)
    line.append(root.val)
    if root.left!=None:
        postorder(root.left)
    else:
        line.append(None)
    if root.right!=None:
        postorder(root.right)
    else:
        line.append(None)

#construct tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5);
root.left.left  = TreeNode(3);
root.left.right = TreeNode(4);
root.right.right = TreeNode(6);

sol = Solution()
s = sol.flatten(root)
line = []
postorder(s)
print(line)
