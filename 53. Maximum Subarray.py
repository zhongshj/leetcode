class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        local_sum = nums[0]
        max_sum = nums[0]
        
        for num in nums[1:]:
            local_sum = max(local_sum+num, num)
            max_sum = max(max_sum, local_sum)
            
        return max_sum