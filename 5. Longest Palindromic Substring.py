class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        # go through the string, try to check the maximum palindrome centered here
        
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s[0]
        
        max_len = 1
        max_str = s[0]
        
        for i in range(len(s)-2):
            # abba
            if s[i] == s[i+1]:
                count = 0
                while i-count >= 0 and i+1+count < len(s) and s[i-count] == s[i+1+count]:
                    count += 1
                count = 2*count
                if count > max_len:
                    max_len = count
                    max_str = s[i-count//2+1:i+1+count//2]
            
            # aba
            if s[i] == s[i+2]:
                count = 0
                while i-count >= 0 and i+2+count < len(s) and s[i-count] == s[i+2+count]:
                    count += 1
                count = 2*count+1
                if count > max_len:
                    max_len = count
                    max_str = s[i-count//2+1:i+2+count//2]
          
        # if last two element like 'aa', it cannot be detected with the loop
        if max_len < 2 and s[-1] == s[-2]:
            return s[-2:]
                                     
        return max_str
                
            