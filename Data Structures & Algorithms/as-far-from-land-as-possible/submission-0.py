from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTION = [(0,1), (0,-1), (1,0), (-1,0)]

        q = deque()
        visited = set()
        
        #place land cells into queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append((r,c))
                    visited.add((r,c))
        
        if not q or len(q) == ROWS * COLS:
            return -1
        
        
        largest_dist = 0 #or layer
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTION:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            largest_dist += 1
        return largest_dist - 1
                
                    
                

                
        


        
