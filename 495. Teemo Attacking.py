class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0
        
        poison = 0
        for i in range(len(timeSeries)-1):
            # poison for interval or the whole duration
            poison = poison + min(timeSeries[i+1] - timeSeries[i], duration)
         
        # last attack poisons a duration
        poison = poison + duration
        
        return poison