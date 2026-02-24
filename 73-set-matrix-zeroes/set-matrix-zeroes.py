class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #taking a list,variables for converting zeroes in row and the size of row and columns
        column_zero=[]
        row_1=len(matrix)
        column_1=len(matrix[0])
        
        #zero_index for finding the index of zeroes in a list so that we can later use it to  
        #convert row zeros
        zero_index=[i for i,row_ in enumerate(matrix) if 0 in row_]

        #transpose,so we can get corresponding columns as rows so we can set them as zeroes
        transpose=[[0]*row_1 for _ in range(column_1)]
        for i in range(row_1):
            for j in range(column_1):
                transpose[j][i]=matrix[i][j]

        for y in transpose:
            if 0 in y:
                y[:]=[0]*len(y)
            column_zero.append(y)

        #again intializing sizes of trasposed matrix to convert into its original form
        row_2=len(transpose)
        column_2=len(transpose[0])
        reverse_transpose=[[0]*row_2 for _ in range(column_2)]
        for i in range(row_2):
            for j in range(column_2):
                reverse_transpose[j][i]=transpose[i][j]

        #converting row to zeroes in those list those who a atleast 1 zero initially by using 
        #the zero_index we have taken previously
        row_zero=[]
        for k in range(len(reverse_transpose)):
            temp=reverse_transpose[k]
            if k in zero_index:
                temp[:]=[0]*len(temp)
            row_zero.append(temp)
        matrix[:]=row_zero