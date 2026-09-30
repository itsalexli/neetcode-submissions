class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_set = set()
        a_set = set()

        ROWS = len(heights)
        COLS = len(heights[0])

        
        def dfs(r, c, ocean):
            
            #directions
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            o_set = p_set
            #add to set
            
            if ocean == "p":
                p_set.add((r,c))
            else:
                a_set.add((r,c))
                o_set = a_set

            
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in o_set and heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, ocean)
        
        for i in range(ROWS):
            dfs(i,0,"p")
            dfs(i, COLS - 1, "a")

        for i in range(COLS):
            dfs(0,i, "p")
            dfs(ROWS - 1, i, "a")
        

        res = []
        for r, c in p_set:
            if (r, c) in a_set:
                res.append([r,c])
        
        return res
                
                



        

            
            

        

            
        


                
            

            

            


        