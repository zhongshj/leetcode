class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # if [i, j] == 0, we can mark[i, 0] and [0, j] as 0, then no extra space needed. 
        # but we have to check zeros in first row and column before checking the rest

        m = len(matrix[0])
        n = len(matrix)
        first_row = False
        first_col = False
        
        # check the first row and column
        for i in matrix[0]:
            if i == 0:
                first_row = True
        for i in [x[0] for x in matrix]:
            if i == 0:
                first_col = True
        
        # check the rest of matrix
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # write zeros from results in first row and column
        for i in range(1, m):
            if matrix[0][i] == 0:
                for j in range(1, n):
                    matrix[j][i] = 0
        for i in range(1, n):
            if matrix[i][0] == 0:
                matrix[i] = [0 for j in range(m)]
        
        # write zeros for first row and column if needed
        if first_row:
            matrix[0] = [0 for j in range(m)]
        if first_col:
            for i in range(n):
                matrix[i][0] = 0

        return
