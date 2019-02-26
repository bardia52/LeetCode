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
            if (rowUp <= rowDown) and (colL <= colR):
                res.extend(matrix[rowUp][colL:colR+1])
                rowUp += 1
            if (rowUp <= rowDown) and (colL <= colR):
                for row in range(rowUp,rowDown+1):
                    res.append(matrix[row][colR])
                colR -= 1
            if (rowUp <= rowDown) and (colL <= colR):
                res.extend(matrix[rowDown][colL:colR+1][::-1])
                rowDown -= 1
            if (rowUp <= rowDown) and (colL <= colR):
                for row in range(rowDown,rowUp-1,-1):
                    res.append(matrix[row][colL])
                colL += 1

        return res