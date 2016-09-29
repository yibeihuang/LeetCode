__author__ = 'yibeihuang'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def discoverNode(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            self.discoverNode(root.left)
            if self.prev and self.prev.val > root.val:
                if self.p1 == None: self.p1 = self.prev
                self.p2 = root
            self.prev = root
            self.discoverNode(root.right)

    def recoverTree(self, root):
        self.p1 = self.p2 = None
        self.prev = None
        self.discoverNode(root)
        self.p1.val, self.p2.val = self.p2.val, self.p1.val
        return root

def postorder(root):
    #line = []
    line.append(root.val)
    if root.left!=None:
        postorder(root.left)
    else:
        line.append(None)
    if root.right!=None:
        postorder(root.right)
    else:
        line.append(None)
    #print(line)

a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(1)
d = TreeNode(5)
e = TreeNode(6)
f = TreeNode(3)
g = TreeNode(7)
a.left = b
b.left = c
b.right = d
a.right = e
e.left = f
e.right = g

sol = Solution()
rst = sol.recoverTree(a)
line = []
postorder(rst)
print(line)