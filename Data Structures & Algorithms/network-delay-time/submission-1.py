from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        #first time a node pops off a heap, it is the shortes
        # 1: [(2, 1), (4,4)]
        # 2: [(3,1)]
        # 3:[(4, 1)]
        # 4:

        #create adj list
    
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v,w))

        minheap = [(0,k)]
        visited = set()
        min_time = 0

        while minheap:
            time, node = heapq.heappop(minheap)
            if node in visited:
                continue

            visited.add(node)
            min_time = max(min_time, time)

            for nei, nei_time in adj[node]:
                if nei not in visited:
                    heapq.heappush(minheap, (time + nei_time, nei))
        
        return min_time if len(visited) == n else -1


        
        
    
    
        




        