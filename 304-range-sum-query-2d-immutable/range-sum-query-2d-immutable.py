class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m=matrix
        self.pre=[[0]*len(self.m[0]) for i in range(len(self.m))]
        for i in range(len(self.m)):
            for j in range(len(self.m[0])):
                top=self.pre[i-1][j] if i>0 else 0
                left=self.pre[i][j-1] if j>0 else 0
                diag=self.pre[i-1][j-1] if i>0 and j>0 else 0
                self.pre[i][j]=self.m[i][j]+top+left-diag

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left_col=self.pre[row2][col1-1] if col1-1>-1 else 0
        up_row=self.pre[row1-1][col2] if row1-1>-1 else 0
        diag_rc=self.pre[row1-1][col1-1] if row1-1>-1 and col1-1>-1 else 0

        return (self.pre[row2][col2]-left_col-up_row+diag_rc)
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)