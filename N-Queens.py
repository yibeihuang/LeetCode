__author__ = 'yibeihuang'
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.Num = n
        self.rst = []
        board = [['.' for i in range(n)] for j in range(n)]
        # for i in range(n):
        #     self.solveNQ(board, i, 0)
        self.solveNQ(board, 0)
        return self.rst

    def solveNQ(self, board, col):
        if col == self.Num:
            self.rst.append(self._printBoard(board))
            return
        # if self._isSafe(board, row, col):
        #     board[row][col] = 'Q'
        #     for r in range(self.Num):
        #         if self.solveNQ(board, r, col+1): return True
        #     board[row][col] = '.'
        for r in range(self.Num):
            if self._isSafe(board, r, col):
                board[r][col] = 'Q'
                self.solveNQ(board, col+1)
                board[r][col] = '.'
        # return False

    def _printBoard(self, board):
        tmp = []
        for i in board:
            tmp.append(''.join(i))
        return tmp

    def _isSafe(self, board, i, j):
        if i>=len(board) or j>=len(board) or i<0 or j<0: return False
        for y in range(j):
            if board[i][y]=='Q': return False
        # lower diagonal
        x,y = i,j
        while x<self.Num and y>=0:
            if board[x][y] == 'Q': return False
            x+=1
            y-=1
        # upper diagonal
        x,y = i, j
        while x>=0 and y>=0:
            if board[x][y] == 'Q': return False
            x -= 1
            y -= 1
        return True

sol = Solution()
print(sol.solveNQueens(4))