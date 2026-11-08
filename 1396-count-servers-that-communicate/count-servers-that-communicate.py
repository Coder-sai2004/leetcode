class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        row_count = {}
        col_count = {}
        total = 0

        # Count the number of servers in each row and column
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:

                    row_count[i] = row_count.get(i,0) + 1
                    col_count[j] = col_count.get(j,0) + 1

        # Count servers that can communicate with another server
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    total += 1

        return total