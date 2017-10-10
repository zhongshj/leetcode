class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        r = True
        stack = []
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if len(stack) == 0:     # additional right-half
                    r = False
                    break
                pop = stack.pop(-1)
                if ord(i) - ord(pop) not in [1, 2]:     # mis-match
                    r = False
                    break
                    
        if len(stack) != 0:     # additional left-half
            r = False
                    
        return r