class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # 0~j no duplicates
        # if duplicates, only i+1
        # if different, copy i to j+1
        
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j = j + 1
                nums[j] = nums[i]
                                
        return j + 1