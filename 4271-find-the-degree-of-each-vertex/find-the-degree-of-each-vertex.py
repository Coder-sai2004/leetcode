class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res=[]
        for i in range(len(matrix)):
            temp=0
            for j in range(len(matrix[0])):
                if matrix[i][j]==1:
                    temp+=1
            res.append(temp)
        return res