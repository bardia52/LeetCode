class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = len(matrix)
        if m==0:
            return res
        n = len(matrix[0])
        rowUp = 0
        rowDown = m-1
        colL = 0
        colR = n-1

        while (rowUp <= rowDown) and (colL <= colR):
            print rowUp, rowDown, colL, colR
            print "rowUp", rowUp, ": ", matrix[rowUp][colL:colR+1]
            res.extend(matrix[rowUp][colL:colR])
            for row in range(rowUp,rowDown+1):
                print "colR", colR, ": ", matrix[row][colR]
                res.append(matrix[row][colR])
            print "rowDown", rowDown, ": ", matrix[rowDown][colL+1:colR][::-1]
            res.extend(matrix[rowDown][colL+1:colR][::-1])
            for row in range(rowDown,rowUp,-1):
                print "colL", colL, ": ", matrix[row][colL]
                res.append(matrix[row][colL])
            rowUp += 1
            colR -= 1
            rowDown -= 1
            colL += 1
        print rowUp, rowDown, colL, colR
            
        return res