class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return self.get_mat(n, 1)
        
    def get_mat(self, n, start):
        if n == 0:
            return []
        if n == 1:
            return [[start]]
        if n == 2:
            return [[start, start+1],[start+3, start+2]]
        
        center_mat = self.get_mat(n-2, 4*n-4+start)
        
        # combine inside & outside
        mat = []
        mat.append([x+start for x in range(n)])     # first row
        for i in range(n-2):    # first and last column
            mat.append([4*n-5+start-i] + center_mat[i] + [n+start+i])
        mat.append([3*(n-1)+start-x for x in range(n)])     # last row
        
        return mat