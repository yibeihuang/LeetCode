__author__ = 'yibeihuang'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder==[]: return None
        if len(inorder) == 1:
            root=TreeNode(inorder[0])
            return root
        if len(inorder) == 2:
            root=TreeNode(postorder[-1])
            if inorder.index(root.val)==0:
                root.right=TreeNode(inorder[1])
                return root
            else:
                root.left=TreeNode(inorder[0])
                return root
        root = TreeNode(postorder[-1])
        pos = inorder.index(root.val)
        leftInorder = inorder[0:pos]
        rightInorder = inorder[pos+1:]
        leftPostorder = postorder[0:pos]
        rightPostorder = postorder[pos+1:-1]
        root.left = self.buildTree(leftInorder, leftPostorder)
        root.right = self.buildTree(rightInorder, rightPostorder)
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

inorder = [3,2,1]
posorder = [3,2,1]

sol = Solution()
s = sol.buildTree(inorder, posorder)
print('=======')
print(s)
line = []
postorder(s)
print(line)