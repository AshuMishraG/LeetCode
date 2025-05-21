class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Modifies the matrix in-place using O(1) extra space.
        This is the main function LeetCode will call.
        """
        if not matrix or not matrix[0]:
            return

        m = len(matrix)
        n = len(matrix[0])

        first_row_has_zero = False
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        first_col_has_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # Use first row (from 2nd element) and first col (from 2nd element) as markers
        # for the rest of the matrix (matrix[1:][1:])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark row i
                    matrix[0][j] = 0  # Mark col j
        
        # Zero out the inner matrix (matrix[1:][1:]) based on markers
        # Process rows first (based on matrix[i][0] markers)
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n): # Only modify from 2nd column onwards
                    matrix[i][j] = 0
        
        # Process columns (based on matrix[0][j] markers)
        # Some cells might be set to 0 twice by these two loops, but that's fine.
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m): # Only modify from 2nd row downwards
                    matrix[i][j] = 0
        
        # Zero out the first row if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Zero out the first column if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0