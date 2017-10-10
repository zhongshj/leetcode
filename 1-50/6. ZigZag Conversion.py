class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s
        
        li = [[] for i in range(numRows)]
        add = 1
        i = 0
        for letter in s:
            li[i].append(letter)
            i += add
            if i == 0 or i == numRows-1:
                add = -1 * add
                
        zigzag = []
        for i in li:
            zigzag = zigzag + i
        return ''.join([x for x in zigzag])
            
            
            