class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        # check empty
        if len(matrix) == 0:
            return []
        if matrix[0] == []:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        
        # if only 1 row or 1 column, just return
        if m == 1:
            return matrix[0]
        elif n == 1:
            return [x[0] for x in matrix]
        
        li = []
        for i in range(n-1):
            li.append(matrix[0][i])
        for i in range(m-1):
            li.append(matrix[i][-1])
        for i in range(n-1):
            li.append(matrix[-1][-1-i])
        for i in range(m-1):
            li.append(matrix[-1-i][0])
            
        return li + self.spiralOrder([x[1:-1] for x in matrix[1:-1]])