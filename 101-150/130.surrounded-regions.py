class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # do dfs at boundary to find non-surrounded "O", mark it as "T"
        # go through the board, set "O" to "X", and "T" to "O"

        if len(board) == 0:
            return None

        m = len(board)
        n = len(board[0])

        for i in xrange(m):
            board = self.dfs(board, i, 0, m, n)
            board = self.dfs(board, i, n-1, m, n)
        for j in xrange(n):
            board = self.dfs(board, 0, j, m, n)
            board = self.dfs(board, m-1, j, m, n)
        
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"

        return None

    def dfs(self, board, i, j, m, n):
        if board[i][j] != "O":
            return board

        board[i][j] = "T"
        if i > 0:
            board = self.dfs(board, i-1, j, m, n)
        if i < m-1:
            board = self.dfs(board, i+1, j, m, n)
        if j > 0:
            board = self.dfs(board, i, j-1, m, n)
        if j < n-1:
            board = self.dfs(board, i, j+1, m, n)
        
        return board
