import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort()
        heap, res = [],[]
        curr_time = 0
        i = 0

        while heap or i < len(tasks):
            #push ready tasks
            while i < len(tasks) and tasks[i][0] <= curr_time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if not heap:
                curr_time = tasks[i][0]
            
            else:
                duration, index = heapq.heappop(heap)
                curr_time += duration
                res.append(index)
        
        return res
            

            
            

            
