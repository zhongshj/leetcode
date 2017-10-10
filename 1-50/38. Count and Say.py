class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        li = [1]
        new_li = [1]
        for i in range(n-1):
            new_li = []
            current = li[0]
            count = 1
            for j in li[1:]:
                if j == current:
                    count = count + 1
                else:
                    new_li.append(count)
                    new_li.append(current)
                    current = j
                    count = 1
            new_li.append(count)
            new_li.append(current)
            li = new_li
            
        return ''.join(str(i) for i in new_li)
            
            