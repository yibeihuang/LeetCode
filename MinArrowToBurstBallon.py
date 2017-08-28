__author__ = 'yibeihuang'
from heapq import *
def findMinArrowShots(points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:x[0])
        res = []
        if points==None or len(points)==0: return 0
        heappush(res,[-points[0][0],-points[0][1]])
        for i in range(1, len(points)):
            if points[i][0]>-res[0][1]:heappush(res, [-points[i][0],-points[i][1]])
            else:
                tmp = heappop(res)
                tmp[0]=min(tmp[0],-points[i][0])
                tmp[1]=max(tmp[1],-points[i][1])
                heappush(res, tmp)
            # for j in range(len(res)):
            #     if points[i][0]<=res[j][1]:
            #         res[j][0]=max(res[j][0],points[i][0])
            #         res[j][1]=min(res[j][1],points[i][1])
            #         break
            #     if j==len(res)-1 and points[i][0]>res[j][1]:
            #         res.append(points[i])
        return len(res)

points = [[10,16],[2,8],[1,6],[7,12]]
print(findMinArrowShots(points))