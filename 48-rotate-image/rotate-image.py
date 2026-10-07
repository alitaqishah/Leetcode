class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose the matrix (swap across the main diagonal)
        for i in range(n-1):
            for j in range(i+1, n):
             # swap upper-triangle with lower-triangle element
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse every row to finish the 90° rotation
        for i in range(n):
            matrix[i].reverse()
        