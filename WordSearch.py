__author__ = 'yibeihuang'
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # visited set (those indexses that failed), remaining set, current subword
        if len(board)==0 or len(board[0])==0: return False
        for i in range(len(board)):board[i] = list(board[i])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.checkExist(board, word, i, j): return True
        return False

    def checkExist(self, board, word, i, j):
        if i<0 or j<0 or i==len(board) or j>=len(board[0]): return False
        if len(word)==1 and board[i][j]==word[0]: return True
        if board[i][j]!=word[0]: return False
        tmp = board[i][j]
        board[i][j]='*'
        rst= self.checkExist(board,  word[1:], i+1, j) or self.checkExist(board, word[1:], i, j+1) \
            or self.checkExist(board,  word[1:], i-1, j) or self.checkExist(board, word[1:], i, j-1)
        board[i][j]=tmp
        return rst


board = ["a"]
word = "a"
sol = Solution()
print(sol.exist(board, word))