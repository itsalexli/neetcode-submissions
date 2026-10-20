import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #set up adj list
        if src == dst:
            return 0
        
        adj = defaultdict(list)
        for from_flight, to_flight, flight_price in flights:
            adj[from_flight].append((to_flight, flight_price))
        
        min_heap = [(0, src, 0)]
        visited = {}

        while min_heap:
            price, node, trips = heapq.heappop(min_heap)

            if node == dst:
                return price
            
            if trips == k + 1:
                continue
            
            if node in visited and visited[node] <= trips:
                continue
            visited[node] = trips

            for nei_node, nei_price in adj[node]:
                heapq.heappush(min_heap, (price + nei_price, nei_node, trips + 1))
            
        return -1




        


        