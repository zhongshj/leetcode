class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        min_idx = 0
        sums = gas[0]-cost[0]
        minimum = gas[0]-cost[0]
        for i in xrange(1, len(gas)):
            sums = sums+gas[i]-cost[i]
            if sums < minimum:
                min_idx = i
                minimum = sums

        if sums < 0:
            return -1
        
        return (min_idx+1)%len(gas)
