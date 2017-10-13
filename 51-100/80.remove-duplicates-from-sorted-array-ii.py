class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use boolean 'twice' to mark 
        delay = 0
        twice = False
        for i in xrange(1, len(nums)):
            if nums[i] == nums[i-1]:
                if twice:   # skip it
                    delay += 1
                else:       # allow one duplicate
                    twice = True
            else:   # reset twice
                twice = False
            nums[i-delay] = nums[i]
        
        return len(nums)-delay
