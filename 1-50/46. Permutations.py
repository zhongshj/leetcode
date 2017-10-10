class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        
        li = []
        
        # for each element, permute the rest and append with the element
        for i in range(len(nums)):
            li = li+[[nums[i]]+sub_li for sub_li in self.permute(nums[:i]+nums[i+1:])]
            
        return li