class NumMatrix:

        #brute force: go through each row from left to right from the left coordinate to the bottom right coordinate

        #Time complexity: O(r2 - r1 * c2 - c1)
        #work for O(1)

        #solution: precompute values for each row and col

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])

        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                self.sumMat[r + 1][c + 1] = prefix + self.sumMat[r][c+1]
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.sumMat[row2 + 1][col2 + 1]
        above = self.sumMat[row1][col2 + 1]
        left = self.sumMat[row2 + 1][col1]
        topLeft = self.sumMat[row1][col1]

        return bottomRight - above - left + topLeft




        


        



        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)