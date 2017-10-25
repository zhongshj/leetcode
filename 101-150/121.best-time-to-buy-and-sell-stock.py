class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        buy = prices[0]
        max_profit = 0

        for i in prices:
            buy = min(buy, i)
            max_profit = max(max_profit, i-buy)

        return max_profit
