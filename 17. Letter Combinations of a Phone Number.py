class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # exp: "23", first initialize "2" as ['a', 'b', 'c'], then enlarge as ['a','a','a','b','b','b','c','c','c'],
        # for a, b, c, append d, e, f
        
        if not digits:
            return []
        
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        li = []
        for letter in dic[digits[0]]:
            li.append(letter)
            
        for digit in digits[1:]:
            num_original = len(li)
            num_append = len(dic[digit])
            new_li = []
            for i in range(num_original):
                new_li = new_li + [li[i] for j in range(num_append)]
                for j in range(num_append):
                    new_li[i*num_append+j] = "".join(list(new_li[i*num_append+j])+[dic[digit][j]])
            li = new_li
        return li
                
    