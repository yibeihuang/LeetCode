__author__ = 'yibeihuang'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        node, length = head, 0

        while node:
            node=node.next
            length += 1
        return self.buildTree(head, 0, length-1)

    def buildTree(self, head, start, end):
        if start>end: return None
        if start == end: return TreeNode(head.val)
        mid = (start+end)>>1
        i, tmp = start, head
        while i<mid:
            tmp=tmp.next
            i += 1
        root = TreeNode(tmp.val)
        root.left = self.buildTree(head, start, mid-1)
        root.right = self.buildTree(tmp.next, mid+1, end)
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

#list
head = ListNode(1)
head.next = ListNode(2);
head.next.next = ListNode(3);
head.next.next.next = ListNode(4);

sol = Solution()
node = sol.sortedListToBST(head)
line = []
postorder(node)
print(line)