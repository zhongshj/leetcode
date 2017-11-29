class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # assume only integer
        ma = nums[0]
        mi = nums[0]
        result = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] < 0:
                ma, mi = mi, ma
            ma = max(nums[i], ma*nums[i])
            mi = min(nums[i], mi*nums[i])
            result = max(result, ma)

        return result
