class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        li = [1]
        
        for i in xrange(rowIndex):
            li = [1]+[li[j]+li[j+1] for j in xrange(i)]+[1]

        return li
