__author__ = 'yibeihuang'
def getModifiedArray(length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        rst = [0 for i in range(length)]
        for (start, end, inc) in updates:
                rst[start] += inc
                if end<len(rst)-1:rst[end+1] += -inc
        tmp = 0
        for i in range(len(rst)):
            rst[i] = rst[i]+tmp
            tmp = rst[i]
        return rst

length = 5
updates = [[1,3,2],[2,4,3],[0,2,-2]]
print(getModifiedArray(length,updates))