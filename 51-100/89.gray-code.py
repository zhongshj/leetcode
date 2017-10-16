class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # gray(n) can be obtained by 2 gray(n-1). one add 0, another add 1. also reverse to make the bridging smooth
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        
        li = self.grayCode(n-1)
        li = li + [li[-1-i]+2**(n-1) for i in range(len(li))]
        return li
