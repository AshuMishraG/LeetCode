class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        cells = set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    cells.add((r, c))
        
        for r, c in cells:
            matrix[r] = [0] * cols
            for row in matrix:
                row[c] = 0