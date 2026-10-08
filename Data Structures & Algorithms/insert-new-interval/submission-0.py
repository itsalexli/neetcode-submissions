class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_index = self.binarySearch(intervals, newInterval[0])
 
        if insert_index > 0 and intervals[insert_index - 1][1] >= newInterval[0]:
            insert_index -= 1
        
        r = insert_index
        while r < len(intervals) and intervals[r][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[r][0]), max(newInterval[1], intervals[r][1])]
            r += 1
        
        return intervals[:insert_index] + [newInterval] + intervals[r:]
        


    

    #Start a pointer r = insert_index.
# While r is in bounds and intervals[r][0] <= newInterval[1], it overlaps, so stretch newInterval to min of the starts and max of the ends, then r += 1.
# Return everything before insert_index, then the merged interval, then everything from r on.







    
    def binarySearch(self,intervals, target):
        l, r = 0, len(intervals) - 1
        
        while l <= r:
            mid = (l + r)//2
            if target == intervals[mid][0]:
                return mid
            if target > intervals[mid][0]:
                l = mid + 1
            else:
                r = mid - 1
        return l

    
        




        