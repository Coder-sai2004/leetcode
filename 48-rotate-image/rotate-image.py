class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        k=0
        for i in range(len(matrix)):
            for j in range(k):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            k+=1
        for x in matrix:
            i=0
            j=len(x)-1
            while i<j:
                x[i],x[j]=x[j],x[i]
                i+=1
                j-=1
            # x.reverse()