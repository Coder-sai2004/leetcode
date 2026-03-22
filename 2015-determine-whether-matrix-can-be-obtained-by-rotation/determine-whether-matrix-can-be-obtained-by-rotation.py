class Solution:
    def rotate(self,matrix):
        res=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        m=len(matrix)-1
        n=0
        for i in range(len(matrix)):
            m=len(matrix[0])-1
            for j in range(len(matrix[0])):
                res[i][j]=matrix[m][n]
                m-=1
            n+=1
        return res
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        c=0
        y=mat
        while c<4:
            x=self.rotate(y)
            if x==target:
                return True
            c+=1
            y=x
        return False