class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]:
            return 0
        
        m = 0
        n = len(nums)
        
        # binary search
        while n-m > 1:
            if target <= nums[(m+n)/2]:
                n = (m+n)/2
            else:
                m = (m+n)/2
                    
        return n