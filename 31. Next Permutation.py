class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) >= 2:
            swapped = False
            
            for i in range(len(nums)-1):
                if nums[-1-i] > nums[-2-i]:     # lower found
                    
                    # find the conditional-minimum at right(right side is reversely sorted now)
                    for j in range(len(nums)-1):
                        if nums[-1-j] > nums[-2-i]:
                            break
                            
                    # swap with conditional-minimum at right side
                    nums[-1-j], nums[-2-i] = nums[-2-i], nums[-1-j]
                    
                    # sort right side
                    nums[-1-i:] = sorted(nums[-1-i:])
                    
                    swapped = True
                    break

            if swapped == False:    # reverse
                print('reverse')
                for i in range(len(nums)//2):
                    nums[i], nums[-i-1] = nums[-i-1], nums[i]