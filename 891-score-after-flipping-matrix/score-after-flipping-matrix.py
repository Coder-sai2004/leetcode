class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row_size=len(grid)
        col_size=len(grid[0])
        t=[[0]*row_size for _ in range(col_size)]
        trow_size=len(t)
        tcol_size=len(t[0])
        ans=0
        #flipping of zeroes to one in rows if the first value of row is zero
        for x in grid:
            if x[0]==0:
                for j in range(len(x)):
                    if x[j]==1:
                        x[j]=0
                    else:
                        x[j]=1
        
        #transpose of a matrix
        for i in range(row_size):
            for j in range(col_size):
                t[j][i]=grid[i][j]
        
        #temp is to find the col in which the no of zeroes greater than ones
        temp=set()
        for k in range(len(t)):
            x=t[k]
            z=x.count(0)
            o=x.count(1)
            if z>o:
                temp.add(k)
        
        #flipping zeroes into ones in col where count of zeroes greater than one
        for k in range(len(t)):
            if k in temp:
                x=t[k]
                for j in range(len(x)):
                    if x[j]==1:
                        x[j]=0
                    else:
                        x[j]=1
        
        #retrieving the original matrix state frm transpose
        for i in range(row_size):
            for j in range(col_size):
                grid[i][j]=str(t[j][i])
        
        
        #calculating the final sum by adding their integer values
        for x in grid:
            ans+=int("".join(x),2)
        
        return ans