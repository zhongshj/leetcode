class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        
        # find shift first
        front = 0
        end = len(nums) - 1
        
        if nums[front] > nums[end]:     # if shifted, found half

            while end - front > 1:
                if nums[(front + end) // 2] > nums[front]:   # middle in left, search right
                    front = (front + end) // 2
                else:                                   # middle in right, search, left
                    end = (front + end) // 2

            # do binary search in part of list
            if target > nums[-1]:    # on the left
                end = front
                front = 0            
            else:
                front = end
                end = len(nums) - 1
            
        while end - front > 1:
            if nums[(front + end) // 2] > target:
                end = (front + end) // 2
            elif nums[(front + end) // 2] < target:
                front = (front + end) // 2
            else:
                return (front + end) // 2
        
        if target == nums[front]:
            return front
        elif target == nums[end]:
            return end
        else:
            return -1