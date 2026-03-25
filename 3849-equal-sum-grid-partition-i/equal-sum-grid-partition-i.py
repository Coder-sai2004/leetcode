class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        r = len(grid)
        c = len(grid[0])
        res=[[0]*c for _ in range(r)]

        #calculating prefix sum for the grid
        for i in range(r):
            for j in range(c):
                top=res[i-1][j] if i-1 >= 0 else 0
                left=res[i][j-1] if j-1 >= 0 else 0
                diag=res[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0
                res[i][j]=top + left + grid[i][j] - diag
        print(res)

        #k1 and i for checking horizontal partition
        #k2 and j for checking vertical partition
        k1 = c-1
        k2 = r-1
        k=0
        i = 0
        j = 0
        #horizontal partitions
        while i < r:
            if res[i][c-1] == (res[r-1][c-1]) - (res[i][c-1]):
                return True
            i += 1
        #vertical partition
        while j< c:
            if res[r-1][j] == (res[r-1][c-1]) - (res[r-1][j]):
                return True
            j += 1

        return False