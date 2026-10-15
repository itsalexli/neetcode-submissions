class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [(0,1), (0, -1), (1, 0), (-1,0)] 
        max_area = 0
        curr_area = 0
        def dfs(r,c):
            nonlocal curr_area
            grid[r][c] = -1
            
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    dfs(nr, nc)
                    curr_area += 1


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    curr_area = 1
                    dfs(r,c)
                    max_area = max(max_area, curr_area)
                    curr_area = 0
        
        return max_area


        


        
    
            



            


            


        