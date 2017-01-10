__author__ = 'yibeihuang'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None: return head
        length = 0
        tmp = head
        while tmp:
            length+=1
            tmp = tmp.next
        halflen = length/2
        p, cnt = head, 0
        prev = p
        while cnt<halflen:
            prev = p
            p=p.next
            cnt+=1
        prev.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(p)
        return self.merge(l1,l2)

    def merge(self, l1, l2):
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            if l1.val<=l2.val:
                p.next = l1
                l1 = l1.next
            elif l2.val<l1.val:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:p.next = l1
        else:p.next = l2
        return dummy.next


head = ListNode(2)
head.next = ListNode(1)
sol = Solution()
print(sol.sortList(head))
