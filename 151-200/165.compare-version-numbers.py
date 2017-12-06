class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # convert to list of integers
        v1 = [int(x.strip()) for x in version1.split('.')]
        v2 = [int(x.strip()) for x in version2.split('.')]
        
        # append 0 to make it same length
        if len(v1) < len(v2):
            while len(v1) < len(v2):
                v1.append(0)
        elif len(v1) > len(v2):
            while len(v1) > len(v2):
                v2.append(0)
        
        # compare
        for i in xrange(min(len(v1), len(v2))):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0
