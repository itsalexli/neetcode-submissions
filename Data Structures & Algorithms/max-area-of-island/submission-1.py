class Solution:

    max_area = 0
    curr_area = 0


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(w,h):
            if not (0 <= w < WIDTH) or not (0 <= h < HEIGHT) or grid[h][w] == 0:
                return
            
            if grid[h][w] == 1:
                grid[h][w] = 0
                self.curr_area += 1
            
            dfs(w + 1, h)
            dfs(w - 1, h)
            dfs(w, h + 1)
            dfs(w, h - 1)


        WIDTH = len(grid[0])
        HEIGHT = len(grid)


        for h in range(HEIGHT):
            for w in range(WIDTH):
                if grid[h][w] == 1:
                    dfs(w, h)
                    self.max_area = max(self.curr_area, self.max_area)
                    self.curr_area = 0
        
        return self.max_area

        



            




        