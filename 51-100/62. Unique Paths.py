class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if min(m, n) == 1:
            return 1
        if m == 2:
            return n
        if n == 2:
            return m
        
        dp = [[0 for x in range(m)] for y in range(n)]
        dp[0][0] = 1
        
        # first row and column
        for i in range(1, m):
            dp[0][i] = dp[0][i-1]
        for j in range(1, n):
            dp[j][0] = dp[j-1][0]
        
        # compute new state with former state
        for idx in range(1, min(m, n)):
            if idx < m:
                for i in range(idx, m):
                    dp[idx][i] = dp[idx][i-1] + dp[idx-1][i]
            if idx < n:
                for j in range(idx, n):
                    dp[j][idx] = dp[j-1][idx] + dp[j][idx-1]
                    
        return dp[-1][-1]
            
        
        