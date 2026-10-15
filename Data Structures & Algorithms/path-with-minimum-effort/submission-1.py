
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        min_heap = [[0, 0, 0]] #diff, (row, col)
        
        while min_heap:
            
        
            diff, r, c = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            
            visited.add((r,c))
            
            if (r,c) == (ROWS - 1, COLS - 1):
                return diff
            
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    new_diff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                    heapq.heappush(min_heap, [new_diff, nr, nc])
        
        return 0


            
                

        
        

