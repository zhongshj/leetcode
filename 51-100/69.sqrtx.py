class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # newton method
        r = x
        while r*r > x:
            r = (r+x/r)/2
        return r
