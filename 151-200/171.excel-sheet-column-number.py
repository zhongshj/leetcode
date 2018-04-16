class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = [ord(x)-64 for x in list(s)]    # A=1
        sums = 0
        for i in s:
            sums = sums*26
            sums += i

        return sums
