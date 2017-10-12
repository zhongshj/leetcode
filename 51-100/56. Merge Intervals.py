# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
    
        intervals = self.quick_sort(intervals)
        
        i = 0
        while i < len(intervals)-1:
            if intervals[i].end >= intervals[i+1].start:
                intervals[i].start = min(intervals[i].start, intervals[i+1].start)
                intervals[i].end = max(intervals[i].end, intervals[i+1].end)
                intervals.pop(i+1)
            else:
                i += 1
        
        return intervals

    
    def quick_sort(self, intervals):
        if len(intervals) < 2:
            return intervals
        
        left = []
        right = []
        pivot = intervals[0]
        
        # priority: start > end
        for i in range(1, len(intervals)):
            if intervals[i].start < pivot.start:
                left.append(intervals[i])
            elif intervals[i].start >= pivot.start:
                if intervals[i].end > pivot.end:
                    right.append(intervals[i])
                else:
                    continue
                    
        return self.quick_sort(left) + [pivot] + self.quick_sort(right)
                    