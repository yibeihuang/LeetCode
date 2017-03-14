__author__ = 'yibeihuang'
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[-1 for i in range(n)] for i in range(n)]
        i = 0
        curr = 1
        direction, row, col = 'E', 0, 0
        while curr<=n*n:
            if direction=='E':
                j,col = col,n-1
                while j<=col:
                    if res[row][j]==-1:
                        res[row][j]=curr
                        curr+=1
                        j+=1
                    else:
                        col = j-1
                        break
                row += 1
                direction = 'S'
            elif direction=='S':
                j,row = row, n-1
                while j<n:
                    if res[j][col]==-1:
                        res[j][col]=curr
                        curr+=1
                        j+=1
                    else:
                        row = j-1
                        break
                direction = 'W'
            elif direction=='W':
                for i in reversed(range(col)):
                    if res[row][i]==-1:
                        res[row][i] = curr
                        curr += 1
                    else:
                        col = i+1
                        break
                if col!=i+1:col=0

                direction = 'N'
            else:
                for i in reversed(range(row)):
                    if res[i][col]==-1:
                        res[i][col] = curr
                        curr += 1
                    else:
                        row = i+1
                        break
                col += 1
                direction = 'E'
        return res

n = 5
sol = Solution()
print(sol.generateMatrix(n))