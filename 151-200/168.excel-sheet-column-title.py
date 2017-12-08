class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        n = n-1
        if n < 26:
            return chr(65+n)
        else:
            return self.convertToTitle(n//26)+chr(65+n%26)
