class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        li = []
        for i in xrange(2**n):
            bits = format(i, 'b')
            li = li+[[nums[j]  for j in xrange(len(bits)) if bits[-1-j] == '1']]
            
        return li
