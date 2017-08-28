__author__ = 'yibeihuang'
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(M)==0: return []
        res = [[0 for i in range(len(M[0]))] for j in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                summ, cnt = M[i][j], 1
                if j-1 >= 0:
                    summ += M[i][j-1]
                    cnt += 1
                if j+1 < len(M[0]):
                    summ += M[i][j+1]
                    cnt += 1
                if i-1>=0:
                    summ += M[i-1][j]
                    cnt += 1
                    if j-1 >= 0:
                        summ += M[i-1][j-1]
                        cnt += 1
                    if j+1 < len(M[0]):
                        summ += M[i-1][j+1]
                        cnt += 1
                if i+1<len(M):
                    summ += M[i+1][j]
                    cnt += 1
                    if j-1 >= 0:
                        summ += M[i+1][j-1]
                        cnt += 1
                    if j+1 < len(M[0]):
                        summ += M[i+1][j+1]
                        cnt += 1
                res[i][j] = summ/cnt
        return res

sol = Solution()
inpt = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
print(sol.imageSmoother(inpt))