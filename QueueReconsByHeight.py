__author__ = 'yibeihuang'
# class Solution(object):
#     def reconstructQueue(self, people):
#         """
#         :type people: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         people.sort(key= lambda x: x[0])
#         res = [0 for i in range(len(people))]
#         for p in people[:-1]:
#             idx = p[1]
#             i = 0
#             j = 0
#             while j<len(res):
#                 if res[j] == 0 and i==idx:
#                     res[j] = p
#                     break
#                 elif res[j]==0 and i!=idx:
#                     i += 1
#                     j += 1
#                     continue
#                 elif res[j]!=0:
#                     j += 1
#                     continue
#         for r in range(len(res)):
#             if res[r] == 0: res[r] = people[-1]
#         return res
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda x: x[1])
        people.sort(key= lambda x: x[0], reverse=True)
        res = []
        for p in people:
            res.insert(p[1], p)
        return res

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(Solution().reconstructQueue(people))