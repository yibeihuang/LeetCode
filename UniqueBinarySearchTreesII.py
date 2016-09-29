class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        #if n==0: return []
        return self.gen(1, n)
 
    def gen(self, start, end):
        # return a list containing all root nodes of BSTs constructed from [start, end]
        res = []
        if start == end: return [TreeNode(start)]
        for rootVal in range(start, end + 1):
            if rootVal == start:
                leftList = [None]
            else: 
                leftList = self.gen(start, rootVal - 1)
            if rootVal == end:
                rightList = [None]
            else: rightList = self.gen(rootVal + 1, end)
            for i in leftList:
                for j in rightList:
                    root = TreeNode(rootVal)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res

def postorder(root):
    line.append(root.val)
    if root.left!=None:
        postorder(root.left)
    else:
        line.append(None)
    if root.right!=None:
        postorder(root.right)
    else:
        line.append(None)

n=3
so=Solution()
s=so.generateTrees(n)
result=[]
for i in s:
    line=[]
    postorder(i)
    result.append(line)

print (result)
    
