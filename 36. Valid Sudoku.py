class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check rows
        for i in range(9):
            if not self.valid(list(board[i])):
                return False
            
        # check columns
        for i in range(9):
            if not self.valid(list(map(list, zip(*board)))[i]):
                list(map(list, zip(*board)))[i]
                return False
            
        # check 3*3
        for i in range(3):
            for j in range(3):
                li = board[3*i][3*j:3*j+3]+board[3*i+1][3*j:3*j+3]+board[3*i+2][3*j:3*j+3]
                if not self.valid(li):
                    return False
            
        return True
         
        
    def valid(self, li):
        dic = {}
        for i in li:
            if i == '.':
                continue
            if ord(i) < 49 and ord(i) > 57:
                return False
            if i in list(dic):
                return False
            else:
                dic[i] = 1
        return True