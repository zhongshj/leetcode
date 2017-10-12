class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [''.join(i) for i in self.dfs(n, n)]
        
    def dfs(self, left, right):
        if left == 0 and right == 0:
            return [[]]
        if left == 0 and right > 0:
            return [[')']+subli for subli in self.dfs(left, right-1)]
        if left == right:
            return [['(']+subli for subli in self.dfs(left-1, right)]
                
        return [[')']+subli for subli in self.dfs(left, right-1)]+[['(']+subli for subli in self.dfs(left-1, right)]
            