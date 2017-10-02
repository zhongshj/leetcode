class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # first sort the list
        li = []
        nums.sort()

        # fix one element, and search for the other 2 on the right
        for fix in range(len(nums)):
            # ignore duplicate
            if fix > 0 and nums[fix] == nums[fix-1]:
                continue
            i = fix+1
            j = len(nums)-1
            # approach solution from both side to the middle
            while i < j:
                if nums[i] + nums[j] < -nums[fix]:
                    i += 1
                elif nums[i] + nums[j] > -nums[fix]:
                    j -= 1
                else:
                    li.append([nums[fix], nums[i], nums[j]])
                    i += 1
                    # ignore duplicate
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
        return li