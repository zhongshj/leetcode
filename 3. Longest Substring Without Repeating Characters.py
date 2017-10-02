class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        max_len = 0
        dic = {}
        
        # save the position of element(last appear) in dic, and update 
        # if j find duplicate between i and j, set i to dic[s[j]]+1(new start)
        for j in range(len(s)):
            if s[j] in list(dic) and dic[s[j]] >= i:
                i = dic[s[j]] + 1
            else:
                if j - i + 1 > max_len:
                    max_len = j - i + 1
            dic[s[j]] = j
        
        return max_len