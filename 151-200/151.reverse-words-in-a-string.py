class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        s = list(s)
        result = []
        
        # clear space in head and tail
        while s[0] == ' ':
            s.pop(0)
            if len(s) == 0:
                return ""
        while s[-1] == ' ':
            s.pop(-1)

        i = 0
        j = 0
        while j < len(s):
            if s[j] == ' ':
                result.insert(0, s[i:j])
                result.insert(0, ' ')
                while s[j] == ' ':
                    j += 1
                i = j
            else:
                j += 1
        result.insert(0, s[i:j])
        result = [''.join(x) for x in result]
        result = ''.join(result)
        return result
