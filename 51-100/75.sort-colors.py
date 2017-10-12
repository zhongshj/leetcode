class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # case 0, move all pointers, write 0 in rp
        # case 1, move wp, bp, write 1 in wp
        # case 2, move bp, write 2 in bp

        rp = 0
        wp = 0
        bp = 0
        for bp in range(len(nums)):
            val = nums[bp]
            nums[bp] = 2
            if val < 2:
                nums[wp] = 1
                wp += 1
            if val == 0:
                nums[rp] = 0
                rp += 1

        return None
