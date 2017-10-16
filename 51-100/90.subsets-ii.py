class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[], [nums[0]]]

        # when update the set from i to i+1, just enlarge the set with set[i]+(i+1)
        # if duplicate, enlarge the set with sub_li[i]+(i+1) from last iteration
        nums.sort()
        li = [[], [nums[0]]]
        sub_li = [[nums[0]]]

        for i in xrange(1, len(nums)):
            if nums[i] != nums[i-1]:
                sub_li = [x+[nums[i]] for x in li]
                li = li+sub_li
            else:
                sub_li = [x+[nums[i]] for x in sub_li]
                li = li+sub_li

        return li

