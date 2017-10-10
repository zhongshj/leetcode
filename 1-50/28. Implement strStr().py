class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        
        needle_len = len(needle)
        j = 0
        
        # if pointer j can reach the needle length, it is found
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i-j
            else:
                i = i-j+1
                j = 0
                
        return -1
        
        