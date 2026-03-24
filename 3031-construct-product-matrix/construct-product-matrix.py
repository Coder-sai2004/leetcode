class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        #converting array into 1d array
        temp=[]
        for x in grid:
            temp.extend(x)
        #initializing the size of 1d arr and declaring prefix,suffix product and resultant array
        n=len(temp)
        pre=[1]*n
        suf=[1]*n
        res=[0]*n
        i=0
        j=n-1
        idx=0
        ans=[[0]*len(grid[0]) for _ in range(len(grid))]
        #performing prefix and suffix product
        while i<n:
            pre[i]=(temp[i]*(1 if i==0 else pre[i-1]))%12345
            suf[j]=(temp[j]*(1 if j==n-1 else suf[j+1]))%12345
            i+=1
            j-=1
        #calculating the product of array except itself
        for k in range(n):
            left=1 if k==0 else pre[k-1]
            right=1 if k==n-1 else suf[k+1]
            res[k]=left*right
        #reconverting the 1d array into 2d array
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans[i][j]=res[idx]%12345
                idx+=1
        return ans