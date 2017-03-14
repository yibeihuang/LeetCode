__author__ = 'yibeihuang'
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def minMeetingRooms(intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals==[]: return 0
        intervals.sort(key= lambda x: x.start)
        if len(intervals)>=1:
            endtime = intervals[0].end
        cnt = [endtime]
        for i in range(1,len(intervals)):
            for j in range(len(cnt)):
                if intervals[i].start>=cnt[j]:
                    cnt[j]=intervals[i].end
                    break
                if j==len(cnt)-1 and cnt[j]>intervals[i].start:cnt.append(intervals[i].end)
        return len(cnt)


intervals = [[2,4],[7,10]]
res = []
for ele in intervals:
    inter = Interval(ele[0],ele[1])
    res.append(inter)
print(minMeetingRooms(res))