class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # get the length
        i = 0
        while x//10**i != 0:
            i = i + 1
            
        # compare head and tail
        for j in range(i//2):
            if x%10**(j+1)//10**j != x%10**(i-j)//10**(i-j-1):
                return False
        return True
    