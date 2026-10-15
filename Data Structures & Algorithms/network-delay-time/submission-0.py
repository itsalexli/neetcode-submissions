from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        #first time a node pops off a heap, it is the shortes
        # 1: [(2, 1), (4,4)]
        # 2: [(3,1)]
        # 3:[(4, 1)]
        # 4:

        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        
        visited = set()
        time = 0

        heap = [(0,k)]
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
            
            visited.add(n1)
            time = max(time, w1)

            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(heap,(w2 + w1, n2))
        
        return time if len(visited) == n else -1
        




        