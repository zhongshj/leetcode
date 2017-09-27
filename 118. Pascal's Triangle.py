class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        
        li = [1]
        big_li = [[1]]
        for i in range(numRows-1):
            a = [0]+li
            b = li+[0]
            li = [x+y for x,y in zip(a,b)]
            big_li.append(li)
        return big_li