from collections import Counter
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        #take temp for getting postion of 1 in the matrix
        #row_count and col_count is used to count the frequency of how many times 1 appeared in row and col
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

        #counting the number of special positions in the matrix
        for x in temp:
            if row_count[x[0]]==1 and col_count[x[1]]==1:
                    ans+=1
        return ans