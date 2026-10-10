'''

1. find how many connected squares, calculate perim, dfs

2. calculate perim, dfs()
connected_sq = 2
perim: = 4 - connected_sq


dfs on the sides:

'''

class Solution:

    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [(1,0), (-1,0), (0, 1), (0, -1)]
        total_perim = 0
        seen = set()

        def dfs(r: int, c: int) -> None:
            nonlocal total_perim
            curr_perim = 4
            seen.add((r,c))

            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                #if valid
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    curr_perim -= 1
                    if (nr, nc) not in seen:
                        dfs(nr, nc)

            total_perim += curr_perim
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return total_perim
        
        return 0

                    
                


            

            


            


            
            


        
        