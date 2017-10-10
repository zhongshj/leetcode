class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_sum = nums[0]+nums[1]+nums[2]
        # fix one element, search the other two from both side
        for fix in range(len(nums)):
            if fix > 0 and nums[fix] == nums[fix-1]:
                continue
            i = fix+1
            j = len(nums)-1
            while i < j:
                # update minimum
                sums = nums[i]+nums[j]+nums[fix]
                if abs(target-sums) < abs(min_sum-target):
                    min_sum = sums
                    
                # control the search direction
                if sums < target:
                    i += 1
                elif sums > target:
                    j -= 1
                else:
                    return target
                
        return min_sum
                    