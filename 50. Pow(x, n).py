class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
            
        # generate a list like [0,2,3], means mul = x**(2**0)*x**(2**2)*x**(2**3)
        # then we do x = x*x, and only do mul = mul*x when it's in the list
            
        li = []
        while n > 0:
            count = 0
            i = 1
            while i*2 <= n:
                i = i*2
                count += 1
            li.append(count)
            n = n-i
        li = li[::-1]
        #print('li:', li)
        
        pointer = 0
        mul = 1
        for i in range(li[-1]+1):
            if i == li[pointer]:
                mul = mul*x
                #print('mul->', mul)
                pointer += 1
                if pointer >= len(li):
                    break
            x = x*x
            #print('x->', x)
            
        return mul



# recursive answer
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        if n == 2:
            return x*x
        if n%2 == 0:
            return self.myPow(self.myPow(x, n//2), 2)
        if n%2 == 1:
            return x*self.myPow(self.myPow(x, n//2), 2)