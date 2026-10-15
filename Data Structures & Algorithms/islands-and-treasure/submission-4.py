from collections import deque

class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        q = deque()
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])


        def addRoom(r,c):
            if 0 <= r < ROWS and 0 <= c < COLS and (r,c) not in visit and grid[r][c] != -1:
                visit.add((r,c))
                q.append((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        dist = 0
        while q:
            #pop gates
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist        
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1



        

        


        
           


        