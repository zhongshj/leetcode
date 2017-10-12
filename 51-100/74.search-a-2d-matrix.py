class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # search it as 1-d list
        if matrix == [] or matrix == [[]]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        lo = 0
        hi = m*n-1

        while lo < hi:
            mid = (lo+hi)/2
            if matrix[mid//n][mid%n] < target:
                lo = mid+1
                print('lo->', lo)
            elif matrix[mid//n][mid%n] > target:
                hi = mid-1
                print('hi->', hi)
            else:
                return True

        return matrix[lo//n][lo%n] == target
