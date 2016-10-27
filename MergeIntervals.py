__author__ = 'yibeihuang'

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)==0: return []
        intervals.sort(key=lambda x: x.start)
        rst, tmp = [], intervals[0]
        if len(intervals)==1: return [[tmp.start, tmp.end]]
        i = 1
        while i < len(intervals):
            if intervals[i].start < tmp.end:
                tmp.end=max(tmp.end, intervals[i].end)
            else:
                rst.append(Interval(tmp.start, tmp.end))
                tmp = intervals[i]
            i+=1
        rst.append(tmp)
        return rst

ii = Interval(1,4)
jj = Interval(2,5)
kk = Interval(6,9)
intervals=[ii,jj,kk]
rst = merge(intervals)
out = []
for ele in rst:
    [i,j] = [ele.start,ele.end]
    out.append([i,j])
print (out)