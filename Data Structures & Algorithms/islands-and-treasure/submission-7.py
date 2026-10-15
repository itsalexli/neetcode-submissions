from collections import deque

class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        #multisource queue, 
        INF = 2147483647

        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])


        def addRoom(r,c,d):
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == INF:
                q.append((r,c))
                grid[r][c] = d


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        dist = 0
        while q:
            #pop gates
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist        
                addRoom(r + 1, c, dist)
                addRoom(r - 1, c, dist)
                addRoom(r, c + 1, dist)
                addRoom(r, c - 1, dist)
            dist += 1



        

        


        
           


        