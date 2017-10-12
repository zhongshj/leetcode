class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # e
        n = len(obstacleGrid)
        if n == 1:
            for i in obstacleGrid[0]:
                print(i)
                if i > 0:
                    return 0
            return 1
        m = len(obstacleGrid[0])
        if m == 1:
            for i in obstacleGrid:
                print(i[0])
                if i[0] > 0:
                    return 0
            return 1
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        # mark obstacle as -1
        obstacleGrid = [[-x for x in sub_li] for sub_li in obstacleGrid]
        
        # initialize first row and column
        for i in range(m):
            if obstacleGrid[0][i] == -1:
                break
            obstacleGrid[0][i] = 1       
        for j in range(1, n):
            if obstacleGrid[j][0] == -1:
                break
            obstacleGrid[j][0] = 1
            
        # fill matrix
        for idx in range(1, min(m, n)):
            for i in range(idx, m):
                if obstacleGrid[idx][i] == -1:
                    continue
                obstacleGrid[idx][i] = max(obstacleGrid[idx-1][i], 0) + max(obstacleGrid[idx][i-1], 0)
                
            for j in range(idx, n):
                if obstacleGrid[j][idx] == -1:
                    continue
                obstacleGrid[j][idx] = max(obstacleGrid[j-1][idx], 0) + max(obstacleGrid[j][idx-1], 0)
                    
        return max(obstacleGrid[-1][-1], 0)
            
        
            
        