class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        x=[]
        c=0
        for i in range(len(grid)):
            x.extend(grid[i])
        for j in x:
            if j<0:
                c+=1
        return c