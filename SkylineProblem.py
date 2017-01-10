__author__ = 'yibeihuang'
# def getSkyline(buildings):
#         """
#         :type buildings: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         points=[]
#         for i in buildings:
#             left = [i[0],i[2]]
#             right = [i[1],-i[2]]
#             points.append(left)
#             points.append(right)
#         points.sort(key=lambda x: x[0])
#         rst,tmp = [],[]
#         while points:
#             if rst==[]:
#                 rst.append(points.pop(0))
#                 continue
#             else: tmp = points.pop(0)
#             if tmp[0]==rst[-1][0] and tmp[1]>rst[-1][1] and rst[-1][1]>0:rst[-1][1]=tmp[1]
#             elif tmp[0]==rst[-1][0] and tmp[1]>rst[-1][1] and rst[-1][1]==0: rst.pop()
#             elif tmp[0]>rst[-1][0] and tmp[1]>rst[-1][1]:
#                 rst.append(tmp)
#             elif tmp[0]>rst[-1][0] and tmp[1]<0: rst.append([tmp[0],0])
#             else: continue
#         # rst.append([tmp[0],0])
#         return rst
from heapq import *

def getSkyline(LRH):
    skyline = []
    i, n = 0, len(LRH)
    liveHR = []:
    while i < n or liveHR
        if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:
            x = LRH[i][0]
            while i < n and LRH[i][0] == x:
                heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                i += 1
        else:
            x = -liveHR[0][1]
            while liveHR and -liveHR[0][1] <= x:
                heappop(liveHR)
        height = len(liveHR) and -liveHR[0][0]
        if not skyline or height != skyline[-1][1]:
            skyline += [x, height],
    return skyline

buildings=[[1,6,3],[2,4,5],[3,5,4]]
print(getSkyline(buildings))