from collections import Counter
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        #take temp for getting postion of 1 in the matrix
        #row_count and col_count is used to count the frequency of how many times 1 appeared in row and col
        #unique_row,unique_col used to store the unique occurence of position 1 where others are zeroes
        ans=0
        temp=set()
        row_count,col_count=Counter(),Counter()
        unique_row,unique_col=[],[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    temp.add((i,j))
                    row_count[i]+=1
                    col_count[j]+=1

        #below is the process of getting unique row and column positions where it is occured only 1 time
        for val,freq in row_count.items():
            if freq==1:
                unique_row.append(val)
        for val,freq in col_count.items():
            if freq==1:
                unique_col.append(val)

        #counting the number of special positions in the matrix
        for i in unique_row:
            for j in unique_col:
                if (i,j) in temp:
                    ans+=1
        return ans