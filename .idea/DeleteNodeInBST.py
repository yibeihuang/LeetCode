__author__ = 'yibeihuang'
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root==None: return
        if root.val == key:
            root = self.exchange(root)
        elif root.left and root.left.val == key:
            root.left = self.exchange(root.left)
        elif root.right and root.right.val == key:
            root.right = self.exchange(root.right)
        elif root.val>key:
            self.deleteNode(root.left,key)
        elif root.val<key:
            self.deleteNode(root.right, key)
        return root

    # def deleteRoot(self, root):
    #     tmp = root
    #     if tmp.left:
    #         tmp = tmp.left
    #         while tmp.right:
    #             prev = tmp
    #             tmp = tmp.right
    def exchange(self, node):
        tmp = node
        prev = None
        if tmp.left:
            tmp = tmp.left
            while tmp.right:
                prev = tmp
                tmp = tmp.right
            if prev:
                prev.right = None
                tmp.left, tmp.right = node.left, node.right
            else:
                tmp.left, tmp.right = None, node.right
        elif tmp.right:
            # prev = tmp
            tmp = tmp.right
            while tmp.left:
                prev = tmp
                tmp=tmp.left
            if prev:
                prev.left = None
                tmp.left, tmp.right = node.left, node.right
            else:
                tmp.left, tmp.right = node.left, None
        return tmp

# root = TreeNode(5)
# root.left = TreeNode(3)
# root.right = TreeNode(6)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(4)
# root.right.right = TreeNode(7)
root = TreeNode(1)
root.right = TreeNode(2)

def bfs(root):
    rst = []
    q = [root]
    while q:
        node = q.pop(0)
        if node=='null':
            rst.append(node)
            continue
        rst.append(node.val)
        if node.left==None and node.right==None: continue
        if node.left:
            q.append(node.left)
        elif node.left==None: q.append('null')
        if node.right:
            q.append(node.right)
        elif node.right==None: q.append('null')
    return rst

sol = Solution()
print(bfs(root))
sol.deleteNode(root,3)
print(bfs(root))


