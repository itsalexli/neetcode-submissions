from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        count_fresh = 0

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count_fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        minutes = 0
        while q and count_fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                
                #rot fruit
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        count_fresh -= 1

            minutes += 1

        return minutes if count_fresh == 0 else -1
                


        

        

        

        