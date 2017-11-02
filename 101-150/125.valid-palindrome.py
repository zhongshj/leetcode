class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        if i > j:
            return True

        while True:
            if ord(s[i]) < 65 or (ord(s[i]) > 90 and ord(s[i]) < 97) or ord(s[i]) > 122:
                i += 1
                if i >= j:
                    return True
                continue
            if ord(s[j]) < 65 or (ord(s[j]) > 90 and ord(s[j]) < 97) or ord(s[j]) > 122:
                j -= 1
                if i >= j:
                    return True
                continue
            print(i, j)
            if s[i] == s[j] or ord(s[i])-ord(s[j]) == 32 or ord(s[j])-ord(s[i]) == 32:
                i += 1
                j -= 1
                if i >= j:
                    return True
            else:
                return False
