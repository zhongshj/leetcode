class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
            
        product = 0
        for i in range(len(num1)):
            for j in range(len(num2)):
                product = product + (ord(num1[-i-1])-48)*(ord(num2[-j-1])-48)*10**(i+j)
                
        return str(product)