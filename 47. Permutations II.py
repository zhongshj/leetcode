class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.bfs(nums)
        
        
    def bfs(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        
        li = []
        
        # for each element, permute the rest and append with the element
        for i in range(len(nums)):
            # if duplicate, skip
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue
            li = li+[[nums[i]]+sub_li for sub_li in self.bfs(nums[:i]+nums[i+1:])]
            
        return li