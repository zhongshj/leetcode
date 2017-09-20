class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        
        j = 0
        for i in range(len(nums)):
            if nums[i] != val: 
                nums[j] = nums[i]   # overwrite the array with non-val only
                j = j + 1
                
        return j
                