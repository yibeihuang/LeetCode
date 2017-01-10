__author__ = 'yibeihuang'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:return ""
        q,rst = [root],[]
        while q:
            curr_node = q.pop(0)
            if curr_node=='null':
                rst.append('null')
                continue
            rst.append(str(curr_node.val))
            if curr_node.left: q.append(curr_node.left)
            else: q.append('null')
            if curr_node.right: q.append(curr_node.right)
            else: q.append('null')
        return ','.join(rst)

def deserialize(data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "": return None
        lst = data.split(',')
        if len(lst)>0: root = TreeNode(lst.pop(0))
        q = [root]
        while q:
            prev_node = q.pop(0)
            if lst:
                curr = lst.pop(0)
                if curr!='null':
                    curr_node=TreeNode(curr)
                    q.append(curr_node)
                    prev_node.left=curr_node
            if lst:
                curr = lst.pop(0)
                if curr!='null':
                    curr_node=TreeNode(curr)
                    q.append(curr_node)
                    prev_node.right=curr_node
        return root

def preorder(root):
    if root:
        line.append(root.val)
        if root.left!=None:
            preorder(root.left)
        else: line.append('null')
        if root.right!=None:
            preorder(root.right)
        else: line.append('null')

root = TreeNode(1)
# root.left = TreeNode(2)
root.right = TreeNode(2);
# root.left.left  = TreeNode(20);
# root.left.right = TreeNode(1);
# root.right.right = TreeNode(-25);
# root.right.right.left = TreeNode(3);
# root.right.right.right = TreeNode(4);

data = serialize(root)
print(data+"\n")
line=[]
preorder(deserialize(data))
print(line)