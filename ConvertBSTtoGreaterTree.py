__author__ = 'yibeihuang'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # right -> center -> left traverse, accumulate node value
        self.accum = 0
        self._inorder(root)
        return root

    def _inorder(self, node):
        if not node: return
        self._inorder(node.right)
        tmp = node.val
        node.val = node.val + self.accum
        self.accum = self.accum + tmp
        self._inorder(node.left)
        return

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

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)
sol = Solution()
node = sol.convertBST(root)
line = []
postorder(node)
print(line)