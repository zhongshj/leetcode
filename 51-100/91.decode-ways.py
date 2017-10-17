class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # for string s, store the decoding num of decoding last bit as 1 bit(single) or 2 bits(with 1 bit before)(double) respectively
        # when it comes to s+1, new_single=single+double because it does not care previous
        # new_double = single, only single before can result in new double

        if len(s) == 0:
            return 0
        if len(s) == 1:
            if s[0] == '0':
                return 0
            else:
                return 1
        
        if s[0] > '0' and s[1] > '0':
            single = 1
        else:
            single = 0
        if s[0] == '1' or (s[0] == '2' and s[1] <= '6'):
            double = 1
        else:
            double = 0

        for i in xrange(2, len(s)):
            if s[i] == '0' and s[i-1] != '1' and s[i-1] != '2':
                return 0

            if s[i] > '0':
                new_single = single+double
            else:
                new_single = 0
            if  s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                new_double = single
            else:
                new_double = 0

            single = new_single
            double = new_double

        return single+double
