class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # for numbers in a particular row i, add its smaller child as the sum of this sub-path
        # do it from bottom to top, then the peak will be minimum total
        row = len(triangle)-2
        while row >= 0:
            for i in xrange(len(triangle[row])):
                triangle[row][i] += min(triangle[row+1][i], triangle[row+1][i+1])
            row -= 1

        return triangle[0][0]
