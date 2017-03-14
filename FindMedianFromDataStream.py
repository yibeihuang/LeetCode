__author__ = 'yibeihuang'
from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small, self.large = [], []


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heappush(self.small, -num)
        heappush(self.large, -heappop(self.small))
        if len(self.small)<len(self.large):
            heappush(self.small, -heappop(self.large))



    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small)>len(self.large):
            return float(-self.small[0])
        else:return (-self.small[0]+self.large[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
param_2 = []
obj.addNum(-1)
param_2.append(obj.findMedian())
obj.addNum(-2)
param_2.append(obj.findMedian())
print(param_2)