class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] 
        self.min = []   # save minimum in each state

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack) == 0:
            self.stack.append(x)
            self.min.append(x)
        else:
            self.stack.append(x)
            if x < self.min[-1]:    # append x
                self.min.append(x)
            else:   # append a same minimum
                self.min.append(self.min[-1])

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop(-1)
        self.min.pop(-1)
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
