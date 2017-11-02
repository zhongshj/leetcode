class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # first construct dp matrix for isPalindrome between i, j
        pair = [[False for i in xrange(len(s))] for j in xrange(len(s))]
        for i in xrange(len(s)):
            pair[i][i] = True
            intv = 1
            while i-intv >= 0 and i+intv < len(s):
                if s[i-intv] != s[i+intv]:
                    break
                pair[i-intv][i+intv] = True
                intv += 1

        for i in xrange(len(s)-1):
            intv = 0
            while i-intv >= 0 and i+1+intv < len(s):
                if s[i-intv] != s[i+1+intv]:
                    break
                pair[i-intv][i+1+intv] = True
                intv += 1

        li = self.par(s, 0, pair)
        return li

    def par(self, s, start, pair):
        # for s, a palindrome set can be for each True i in dp matrix, s[start:i]+par(s[i:])
        if start == len(s)-1:
            return [[s[-1]]]
        if start > len(s)-1:
            return [[]]
        li = []
        for i in xrange(start, len(s)):
            if pair[start][i]:
                li = li+[[s[start:i+1]]+next_li for next_li in self.par(s, i+1, pair)]
        return li
