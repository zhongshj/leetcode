class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        rt = [[1]]
        li = [1]
        for i in xrange(numRows-1):
            li = self.next_row(li)
            rt.append(li)

        return rt


    def next_row(self, li):
        return [1]+[li[i]+li[i+1] for i in xrange(len(li)-1)]+[1]
