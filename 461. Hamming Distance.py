class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        hdist = 0
        for bit in range(32):
            xr = x % 2
            yr = y % 2
            x = x // 2
            y = y // 2
            if xr != yr:
                hdist = hdist + 1
            
        return hdist