class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # add 1 to last digit. if carry, do plusOne for digit[:-1]
        if digits == []:
            return [1]
        
        digits[-1] += 1
        if digits[-1] == 10:
            digits[-1] = digits[-1]-10
            digits[:-1] = self.plusOne(digits[:-1])

        return digits
