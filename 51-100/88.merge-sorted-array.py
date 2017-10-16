class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if nums1 == []:
            nums1 = nums2
        if nums2 == []:
            return None

        k = m+n-1
        j = n-1
        i = m-1
        
        while True:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
            if j < 0:
                break
            if i < 0:
                for l in range(j+1):
                    nums1[l] = nums2[l]
                break

        return None
