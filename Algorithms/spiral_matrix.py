class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        rowUp = 0
        rowDown = m-1
        colL = 0
        colR = n-1
        res = []
        res.append(matrix[rowUp][colL:colR+1])
        rowUp += 1
        for row in range(rowUp,rowDown):
            print matrix[row][colR]
            res.append(matrix[row][colR])
        colR -= 1
        
        return res