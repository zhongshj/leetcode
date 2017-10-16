class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 1
        if len(s) == 2:
            num = 0
            if s[0] <= '2' and s[1] <= '6':
                num += 1
            if s[0] != '0' and s[1] != 0:
                num += 1
            return num

        mid = len(s)/2
        
        return self.numDecodings(s[:mid-1])*self.numDecodings(s[mid+1:])*(1+self.numDecodings(s[mid-1:mid+1]))
