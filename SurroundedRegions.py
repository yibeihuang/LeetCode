__author__ = 'yibeihuang'
def solve(board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board)==0 or len(board[0])==0: return
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O' and (i,j) not in visited:
                    stack = [(i,j)]
                    tmp = [(i,j)]
                    flag = 'X'
                    while stack:
                        i1,j1=stack.pop(0)
                        if i1==len(board)-1 or j1 ==len(board[0])-1 or i1==0 or j1==0:flag='O'
                        if i1<len(board)-1 and board[i1+1][j1]=='O':
                            stack.append((i1+1,j1))
                            tmp.append((i1+1,j1))
                        if j1<len(board[0])-1 and board[i1][j1+1]=='O':
                            stack.append((i1,j1+1))
                            tmp.append((i1,j1+1))
                    if flag=='X':
                        while tmp:
                            i1,j1=tmp.pop()
                            lst = list(board[i1])
                            lst[j1]='X'
                            board[i1] = ''.join(lst)


board = ["XOXOXO","OXOXOX","XOXOXO","OXOXOX"]
solve(board)
print(board)