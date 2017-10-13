class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.dfs(1, n, k)

    def dfs(self, lo, hi, k):
        if k < 1 or hi-lo < k-1:
            return [[]]
        if hi-lo == k-1:
            return [[x for x in range(lo, hi+1)]]
        
        # pick first and find k-1 in rest + skip first and find k in rest
        return [[lo]+subli for subli in self.dfs(lo+1, hi, k-1)]+self.dfs(lo+1, hi, k)

        
