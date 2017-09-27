class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = quick_sort(nums)
        sums = 0
        for i in range(len(nums)/2):
            sums = sums + nums[2*i]
        return sums
    
def quick_sort(nums):
    if len(nums) < 2:
        return nums
    pivot = nums[0]
    left = []
    right = []
    for i in range(1, len(nums)):
        if nums[i] <= pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])
    return sort(left) + [pivot] + sort(right)
        

