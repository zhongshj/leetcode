class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return [''.join(x) for x in self.valid_ip(list(s), 4)]

    
    def valid_ip(self, s, n):
        if len(s) < n or len(s) > 3*n:  # s length impossible for n
            return []

        if n == 1:  # last period, return if legitimate, else return []
            if len(s) == 1:
                return [s]
            elif len(s) == 2:
                if s[0] != '0':
                    return [s]
                else:
                    return []
            else:
                if s[0] != '0' and int(''.join(s)) < 256:
                    return [s]
                else:
                    return []

        # recursive for 1~3 digits cases
        s1 = [s[:1]+['.']+x for x in self.valid_ip(s[1:], n-1)]
        
        s2 = []
        if s[0] != '0':
            s2 = [s[:2]+['.']+x for x in self.valid_ip(s[2:], n-1)]
        
        s3 = []
        if s[0] != '0' and int(''.join(s[:3])) < 256:
            s3 = [s[:3]+['.']+x for x in self.valid_ip(s[3:], n-1)]

        return s1+s2+s3
