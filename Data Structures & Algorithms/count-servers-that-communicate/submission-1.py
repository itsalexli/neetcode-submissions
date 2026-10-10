class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        row_count = {i: set() for i in range(ROWS)}
        col_count = {j: set() for j in range(COLS)}


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row_count[r].add((r,c))
                    col_count[c].add((r,c))
        
        count = 0
        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 1:
                    row_count[r].remove((r,c))
                    col_count[c].remove((r,c))

                    if len(row_count[r]) > 0  or len(col_count[c]) > 0 :
                        count += 1
                    
                    row_count[r].add((r,c))
                    col_count[c].add((r,c))   
        return count





        