class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        major = nums[0]
        count = 1
        for i in nums[1:]:
            if count == 0:
                count += 1
                major = i
            elif major == i:
                count += 1
            else:
                count -= 1

        return major

    def dijkstra(self, nums, lo, hi):
        if hi-lo < 2:
            return nums
        
        v = nums[lo]
        lt = lo
        gt = hi
        i = lo
        while i <= gt:
            if nums[i] < v:
                nums[i], nums[lt] = nums[lt], nums[i]
                lt += 1
                i += 1
            elif nums[i] > v:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                i += 1
        
        nums = self.dijkstra(nums, lo, lt-1)
        nums = self.dijkstra(nums, gt+1, hi)

        return nums
            
