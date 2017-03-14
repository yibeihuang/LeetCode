__author__ = 'yibeihuang'
def rotate(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length/2):
            tmp = matrix[i]
            matrix[i] = matrix[length-i-1]
            matrix[length-i-1] = tmp
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

mm = [[1,2],[3,4]]
print(rotate(mm))