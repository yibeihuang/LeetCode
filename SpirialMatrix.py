__author__ = 'yibeihuang'
def spiralOrder( matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # keep del matrix, flag to keep track of the directions 'EWSN'
        rst = []
        flag = 'E'
        while len(matrix)>0 and len(matrix[0])>0:
            if flag=='E':
                for x in matrix[0]:
                    rst.append(x)
                matrix.pop(0)
                flag = 'S'
            elif flag=='S':
                for i in matrix:
                    rst.append(i[-1])
                    i.pop()
                flag = 'W'
            elif flag=='W':
                j = len(matrix)-1
                for i in reversed(range(len(matrix[0]))):
                    rst.append(matrix[j][i])
                    matrix[j].pop()
                if matrix[j]==[]: matrix.pop()
                flag = 'N'
            elif flag=='N':
                for i in reversed(range(len(matrix))):
                    rst.append(matrix[i][0])
                    matrix[i].pop(0)
                flag = 'E'
        return rst

mm = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(spiralOrder(mm))