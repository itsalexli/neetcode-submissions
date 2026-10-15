from collections import defaultdict
import heapq    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #calculate costs     
        #djikstra's algorithm
        #which node to start in
        #how to calculate costs

        #build the adj_list
        adj = defaultdict(list)
        for i in range(len(points)):
            for k in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[k]
                cost = abs(x1 - x2) + abs(y1 - y2)
                adj[(x1,y1)].append(((x2,y2), cost))
                adj[(x2,y2)].append(((x1,y1), cost))
        #put into function

        total = 0
        minheap = [(0, tuple(points[0]))]
        visited = set()
        
        while len(visited) < len(points):
            cost, coord = heapq.heappop(minheap)
            if coord in visited:
                continue

            total += cost
            visited.add(coord)

            for nei_coord, nei_cost in adj[coord]:
                if nei_coord not in visited:
                    heapq.heappush(minheap, (nei_cost, nei_coord))

        return total
            

        

        

            

                





        




