class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        sums = 0
        for i in xrange(len(prices)-1):
            if prices[i+1] > prices[i]:
                sums = sums+prices[i+1]-prices[i]

        return sums
