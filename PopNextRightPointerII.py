__author__ = 'yibeihuang'
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            if root.left and root.right:
                root.left.next = root.right
            curr = root
            if curr.right: prev = curr.right
            else: prev = curr.left
            while curr.next:
                if prev and curr.next.left:
                    prev.next = curr.next.left
                    prev = prev.next
                elif prev and curr.next.right:
                    prev.next = curr.next.right
                    prev = prev.next
                curr = curr.next
            self.connect(root.left)
            self.connect(root.right)

# # Definition for a  binary tree node
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
# #         self.next = None
#
# class Solution:
#     # @param root, a tree node
#     # @return nothing
#     def connect(self, root):
#         if root:
#             p = root; q = None; nextNode = None
#             while p:
#                 if p.left:
#                     if q: q.next = p.left
#                     q = p.left
#                     if nextNode == None: nextNode = q
#                 if p.right:
#                     if q: q.next = p.right
#                     q = p.right
#                     if nextNode == None: nextNode = q
#                 p = p.next
#             self.connect(nextNode)


#{2,1,3,0,7,9,1,2,#,1,0,#,#,8,8,#,#,#,#,7}
## bulid a binary tree out of this list