__author__ = 'yibeihuang'
def minTotalDistance( grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # median
        x = []
        y = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    x.append(i)
                    y.append(j)
        x.sort()
        y.sort()
        midx, sumx=x[len(x)/2],0
        midy, sumy=y[len(y)/2],0
        for ele in x:
            sumx+=abs(ele-midx)
        for ele in y:
            sumy += abs(ele-midy)
        return sumx+sumy

grid = [[0,0,0,1,0,1,0,0,0,1,1,0]]
print(minTotalDistance(grid))