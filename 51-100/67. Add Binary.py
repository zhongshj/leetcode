class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a
        
        a = list(a)
        b = list(b)
        i = -1
        li = []
        
        # compute sum list with [0, 1, 2, 3]
        while True:
            li.insert(0, int(a[i]) + int(b[i]))
            i -= 1
            if -i > len(a):
                li = [int(x) for x in b[0:len(b)+i+1]] + li
                break
            if -i > len(b):
                li = [int(x) for x in a[0:len(a)+i+1]] + li
                break
                
        # process carry
        li.insert(0, 0)
        for i in range(1, len(li)):
            if li[-i] >= 2:
                li[-i] -= 2
                li[-i-1] += 1
        if li[0] == 0:
            li.pop(0)
        return ''.join(str(x) for x in li)
            



# a recursive solution

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1], b[0:-1]) + '0'
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + '1'