class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 2 will be adequate, count how many 5 they met,
        # 25 count as 5^2, 125 as 5^3...
        if n == 0:
            return 0
        else:
            return n//5+self.trailingZeroes(n//5)
