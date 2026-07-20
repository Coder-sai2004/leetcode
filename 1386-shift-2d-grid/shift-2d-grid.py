class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        row=len(grid)
        col=len(grid[0])
        for x in grid:
            res.extend(x)
        n=len(res)
        s=n-(k%n)
        idx=0
        ans=res[s:]+res[:s]
        sol=[[0]*col for _ in range(row)]    
        for i in range(row):
            for j in range(col):
                sol[i][j]=ans[idx]
                idx+=1
        return sol