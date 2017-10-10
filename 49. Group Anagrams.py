class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for string in strs:
            hashed = self.hash_prime(string)
            if hashed not in list(dic):
                dic[hashed] = [string]
            else:
                dic[hashed].append(string)
            
        return dic.values()
        
        # either hash function below should work
        
    def hash_tuple(self, string):
        # hash function with tuple
        li = [0 for i in range(26)]
        for letter in string:
            li[ord(letter)-97] += 1
        return tuple(li)
    
    def hash_prime(self, string):
        # hash function with multiplying prime numbers
        primes = [2, 3, 5, 7, 11 ,13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 107]
        rt = 1
        for letter in string:
            rt = rt * primes[ord(letter)-97]
        return rt