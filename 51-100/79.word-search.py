class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # naive backtrack search
        for m in xrange(len(board)):
            for n in xrange(len(board[0])):
                if self.dfs(board, m, n, word):
                        return True
        return False

    
    def dfs(self, board, m, n, word):
        if word == "":  # no more letter to match
            return True

        # out of range or unequal
        if m < 0 or m > len(board)-1 or n < 0 or n > len(board[0])-1 or board[m][n] != word[0]:
            return False
        
        # occupy to make sure path unique
        board[m][n] = '#'

        if self.dfs(board, m-1, n, word[1:]) or self.dfs(board, m+1, n, word[1:]) or self.dfs(board, m, n-1, word[1:]) or self.dfs(board, m, n+1, word[1:]):
            return True
        
        # put the value back
        board[m][n] = word[0]

        return False
