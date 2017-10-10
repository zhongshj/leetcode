class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # recursively rotate from outer layer to inner layer, d is the depth
        self.rotate_mid(matrix, 0)
        
    def rotate_mid(self, matrix, d):
        if len(matrix)-2*d < 2:
            return matrix
        if len(matrix)-2*d == 2:
            matrix[d][d+1], matrix[d+1][d+1], matrix[d+1][d], matrix[d][d] = matrix[d][d], matrix[d][d+1], matrix[d+1][d+1], matrix[d+1][d]
            return matrix
        
        for i in range(d, len(matrix)-d-1):
            matrix[i][-1-d], matrix[-1-d][-1-i], matrix[-1-i][d], matrix[d][i] = matrix[d][i], matrix[i][-1-d], matrix[-1-d][-1-i], matrix[-1-i][d]
                    
        matrix = self.rotate_mid(matrix, d+1)
        