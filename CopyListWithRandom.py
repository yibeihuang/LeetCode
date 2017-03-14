__author__ = 'yibeihuang'
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head==None: return
        copyHead = RandomListNode(head.label)
        q = [head]
        lookup = dict()
        lookup[head] = copyHead
        while q:
            currnode = q.pop(0)
            tmp = lookup[currnode]
            if currnode.next:
                if currnode.next not in lookup:
                    tmp.next = RandomListNode(currnode.next.label)
                    lookup[currnode.next] = tmp.next
                    q.append(currnode.next)
                else:tmp.next = lookup[currnode.next]
            if currnode.random:
                if currnode.random not in lookup:
                    tmp.random = RandomListNode(currnode.random.label)
                    lookup[currnode.random] = tmp.random
                    q.append(currnode.random)
                else:tmp.random = lookup[currnode.random]
        return copyHead


head = RandomListNode(-1)
head.next = RandomListNode(-1)
head.random = RandomListNode(2)
head.next.random = head
print(Solution().copyRandomList(head))