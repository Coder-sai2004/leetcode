class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                a=i-1
                b=j-1
                if matrix[i][j]!=matrix[a][b]:
                    return False
        return True