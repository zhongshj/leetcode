class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        word_len = 0
        for i in range(len(s)):
            if s[-i-1] == ' ' and word_len != 0:
                break
            if s[-i-1] != ' ':
                word_len += 1
            
        return word_len   