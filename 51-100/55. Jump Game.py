class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # start from goal
        i = len(nums) - 1
        jump_len = 0
        while i >= 0:
            if nums[i] >= jump_len:  # can it reach the goal?
                if i == 0:     # already in start, return true
                    return True
                else:           # set as sub-goal
                    jump_len = 1
                    i -= 1
                    continue
            else:
                i -= 1
                jump_len += 1
                
        return False