class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # maintain a dp array, dp[i] is True if s[i-w:i] in wordDict and dp[i-w] is True
        dp = [False for i in xrange(len(s))]
        for word in wordDict:
            if word == s[:len(word)]:
                dp[len(word)-1] = True

        for i in xrange(1, len(dp)):
            for word in wordDict:
                if word == s[i:i+len(word)] and dp[i-1] == True:
                    if i+len(word) <= len(dp):
                        dp[i+len(word)-1] = True

        return dp[-1]
                    
