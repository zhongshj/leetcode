class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # G(n) = G(0)G(n-1)+G(1)G(n-2)+...+G(n-1)G(0)
        dp = [0 for i in xrange(n+1)]
        dp[0] = 1
        dp[1] = 1

        for i in xrange(2, n+1):
            for j in xrange(i):
                dp[i] += dp[j]*dp[i-j-1]

        return dp[-1]
