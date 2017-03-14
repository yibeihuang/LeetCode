__author__ = 'yibeihuang'
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def postorderTraversal(root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        curr = root
        res = []
        stack = []
        stack2 = []
        while stack or curr or stack2:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                tmp = stack.pop()
                if tmp.right:
                    curr = tmp.right
                    stack2.append(tmp)
                else:
                    res.append(tmp.val)
                    if stack2:res.append(stack2.pop().val)
            else:res.append(stack2.pop().val)
        return res

root = TreeNode(3)
root.right = TreeNode(1)
root.right.left = TreeNode(2)
print(postorderTraversal(root))