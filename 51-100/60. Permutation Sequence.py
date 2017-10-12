class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # get approximate n! for k(num of digit inferred)
        li = [x+1 for x in range(n)]
        c = 1
        i = 1
        while k > c:
            i = i + 1
            c = c * i      
        inferred_num = i
        
        # only compute inferred part
        li = li[:n-inferred_num] + self.permute(li[n-inferred_num:], k-1, c)
        return ''.join([str(x) for x in li])
        
    def permute(self, li, k, c):
        if len(li) < 2:
            return li
        c = c / len(li)
        idx = k // c
        k = k % c
        x = li.pop(idx)
        return [x] + self.permute(li, k, c)
        