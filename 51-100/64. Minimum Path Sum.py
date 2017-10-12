class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        n = len(grid)
        
        # grid matrix can be used as dp matrix here
        # first row and column
        for i in range(1, m):
            grid[0][i] = grid[0][i-1]+grid[0][i]
        for i in range(1, n):
            grid[i][0] = grid[i-1][0]+grid[i][0]
            
        # fill dp matrix
        for i in range(1, min(m, n)):
            for j in range(i, m):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1])+grid[i][j]
            for j in range(i+1, n):
                grid[j][i] = min(grid[j-1][i], grid[j][i-1])+grid[j][i]
                
        return grid[-1][-1]