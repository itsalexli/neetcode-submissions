class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        stack = []
        count = 0
        for start, end in intervals:
            if stack and start < stack[-1][1]:
                count += 1
                #pop current one
                if end < stack[-1][1]:
                    stack.pop()
                else:
                    continue
            stack.append([start,end])
        
        return count
                
            
