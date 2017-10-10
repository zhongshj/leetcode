class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # recursively merge strings
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        if len(strs) == 2:
            return self.prefix(strs[0], strs[1])
        if len(strs) > 2:
            return self.prefix(self.longestCommonPrefix(strs[:len(strs)//2]), self.longestCommonPrefix(strs[len(strs)//2:]))
                
    def prefix(self, str1, str2):
        if len(str1) < len(str2):
            str1, str2 = str2, str1
            
        for i in range(len(str2)):
            if str1[i] != str2[i]:
                return str2[:i]
        return str2