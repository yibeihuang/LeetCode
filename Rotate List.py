__author__ = 'yibeihuang'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None: return head
        length, tmp = 0, head
        while tmp:
            end = tmp
            tmp = tmp.next
            length += 1
        end.next = head
        tmp = head
        for i in range(length-k-1):
            tmp = tmp.next
        head = tmp.next
        tmp.next = None
        return head

def buildLinkedList(list):
    if list==None: return None
    head = ListNode(list[0])
    head.val = list[0]
    if len(list)==1: return head
    head.next = ListNode(list[1])
    for i in range(len(list)-1):
        ListNode(list[i]).val = list[i]
        ListNode(list[i]).next = ListNode(list[i+1])
    return head

lis = [1,2,3,4,5]
head = buildLinkedList(lis)
print(head.next.val)