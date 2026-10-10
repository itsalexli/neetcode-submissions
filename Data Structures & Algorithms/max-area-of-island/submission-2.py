class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c):

            area = 1
            grid[r][c] = 0
            
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    area += dfs(nr, nc)

            return area

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(area, max_area)
        
        return max_area
        
        
    
            



            


            


        