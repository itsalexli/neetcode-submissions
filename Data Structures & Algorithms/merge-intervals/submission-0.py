class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #notes:
        #not in sorted order
        #all positive
        #multiple overlapping, merge all
        #non overlapping, leave same
        #order -> any order

        #steps:
        #identify merged intervals
        #merging intervals

        #empty -> return []
        if not intervals:
            return []
        #if one element, return intervals
        if len(intervals) == 1:
            return intervals
        #sorting 

        intervals.sort()

        merged = []

        for i in range(len(intervals)):
            # check if 1st index <= 2nd index in stack
            if merged and intervals[i][0] <= merged[-1][1]:
                # update interval or not inside stack -> max of 2nd indexes
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])
        
        return merged
        
        




        
