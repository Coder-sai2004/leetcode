class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        #x,y are the top-left corner indexes of submatrix
        #k1,k2 are the right-bottom corner indexes of submatrix
        #m1,m2 are the indexes that iterate from last for swapping

        k1 = x + k
        k2 = y + k
        m1 = k1 - 1
        m2 = y
        #c is refer to the no of iterations
        #l is the required no of iterations we need to do to flip the submatrix
        c= 0
        l = k // 2
        for i in range(x,k1):
            if l == c:
                break
            for j in range(y,k2):
                if i >= x and j >= y and i < k1 and j < k2:
                    grid[i][j],grid[m1][m2] = grid[m1][m2],grid[i][j]
                    m2 += 1
            c += 1
            m1 -= 1
            m2 = y
        return grid