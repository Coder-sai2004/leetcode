class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        x=matrix[::-1]
        i,j,k=0,0,0
        r,res=[],[]
        s=len(x)*len(x)
        while k<s:
            r.append(x[i][j])
            i+=1
            if i==len(x):
                res.append(r)
                r=[]
                i=0
                j+=1
            k+=1
        matrix[:]=res
        