class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS = len(board)
        COLS = len(board[0])


        
        #dfs function

        def dfs(r, c):

            #direction array
            direction = [(1,0), (-1, 0), (0, 1), (0, -1)]

            #if valid space:
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == "O":
                print(r,c)
                board[r][c] = "#"
                #check all 4 directions
                for dr, dc in direction:
                    nr, nc = r + dr, c + dc
                    dfs(nr, nc)

        #left
        for i in range(ROWS):
            if board[i][0] == "O":
                dfs(i, 0)
            
        #up
        for j in range(COLS):
            if board[0][j] == "O":
                print("detected up")
                dfs(0, j)

        #right

        for i in range(ROWS):
            if board[i][COLS - 1] == "O":
                dfs(i, COLS - 1)

        #down
        for j in range(COLS):
            if board[ROWS - 1][j] == "O":
                dfs(ROWS - 1, j)
        
        #after border, traverse matrix

        for r in range(ROWS):
            for c in range(COLS):
            
                #if "#", change it to a 0. 
                #if 0, change it to an X
                if board[r][c] == "O":
                    board[r][c] = "X"
                
                if board[r][c] == "#":
                    board[r][c] = "O"





        
        
















        