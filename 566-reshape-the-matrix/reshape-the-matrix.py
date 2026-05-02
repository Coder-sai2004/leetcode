class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if (len(mat)*len(mat[0]))!=(r*c):
            return mat
        res=[]
        m=0
        n=1
        temp=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if n<c:
                    temp.append(mat[i][j])
                    n+=1
                elif n==c:
                    temp.append(mat[i][j])
                    res.append(temp)
                    n=1
                    temp=[]
                    m+=1
        return res