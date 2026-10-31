from collections import Counter
class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        m = len(grid)  # Number of rows
        n = len(grid[0])  # Number of columns

        row = []  # Stores 0s and 1s count for each row
        col = []  # Stores 0s and 1s count for each column

        # Initialize the difference matrix
        diff = [[0] * n for _ in range(m)]

        # Transpose the grid to get columns as rows
        transposed = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                transposed[j][i] = grid[i][j]

        # Count 0s and 1s in each row
        for values in grid:
            count = Counter(values)
            row.append(count)

        # Count 0s and 1s in each column
        for values in transposed:
            count = Counter(values)
            col.append(count)

        # Calculate the difference for each cell
        for i in range(m):
            for j in range(n):
                row_ones = row[i][1]
                col_ones = col[j][1]
                row_zeros = row[i][0]
                col_zeros = col[j][0]

                diff[i][j] = row_ones + col_ones - row_zeros - col_zeros

        return diff