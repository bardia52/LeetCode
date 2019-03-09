class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def neighbors(b,i,j,m,n):
            ret = 0
            # check above rows
            if i > 0:
                # above
                ret += b[i-1][j]
                # above left
                if j > 0: ret += b[i-1][j-1]
                # above right
                if j < n-1: ret += b[i-1][j+1]
            # check below rows
            if i < m-1:
                #  below
                ret += b[i+1][j]
                # below left
                if j > 0: ret += b[i+1][j-1]
                # below right
                if j < n-1: ret += b[i+1][j+1]
            # check sides
            # left
            if j > 0: ret += b[i][j-1]
            # right
            if j < n-1: ret += b[i][j+1]
            return ret

        m = len(board)
        if m==0: return
        n = len(board[0])
        temp = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                x = board[i][j]
                x_n = neighbors(board,i,j,m,n)
                if x:
                    if x_n < 2:
                        temp[i][j] = 0
                    elif x_n == 2 or x_n == 3:
                        temp[i][j] = 1
                    else:
                        temp[i][j] = 0
                else:
                    if x_n == 3:
                        temp[i][j] = 1
                    else:
                        temp[i][j] = 0
        for i in range(m):
            for j in range(n):
                board[i][j] = temp[i][j]
