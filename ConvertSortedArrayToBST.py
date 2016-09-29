__author__ = 'yibeihuang'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)>1:
            length = len(nums)
        elif len(nums) == 1:
            root = TreeNode(nums[0])
            return root
        else:
            return None
        pos = int((length-1)/2)
        root = TreeNode(nums[pos])
        root.left = self.sortedArrayToBST(nums[0:pos])
        root.right = self.sortedArrayToBST(nums[pos+1:])
        return root

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

nums = [1,2,3,4,5]
so=Solution()
s=so.sortedArrayToBST(nums)
line = []
postorder(s)
print (line)