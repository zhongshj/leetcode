class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_water = 0
        while i < j:
            max_water = max(max_water, (j-i)*min(height[i], height[j]))
            if height[i] < height[j]:
                temp = height[i]
                i += 1
                while height[i] <= temp and i < j:
                    i += 1
            else:
                temp = height[j]
                j -= 1
                while height[j] <= temp and i < j:
                    j -= 1
                
        return max_water
                