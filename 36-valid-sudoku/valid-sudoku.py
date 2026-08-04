class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=[]
        c=[]
        b=[]
        for i in range(len(board)):
            x={}
            y={}
            for j in range(len(board[0])):
                #calculating row hash table
                if board[i][j]!='.':
                    x[board[i][j]]=x.get(board[i][j],0)+1
                #calculating column hash table
                if board[j][i]!='.':
                    y[board[j][i]]=y.get(board[j][i],0)+1
            r.append(x)
            c.append(y)

        si=0
        se=0
        ei=3
        ee=3
        for k in range(len(board)):
            if k!=0:
                if k%3==0:
                    si+=3
                    ei+=3
                    se=0
                    ee=3
                else:
                    se+=3
                    ee+=3

            z={}
            #calculating 3*3 box hash table
            for i in range(si,ei):
                for j in range(se,ee):
                    if board[i][j]!='.':
                        z[board[i][j]]=z.get(board[i][j],0)+1
            b.append(z)

        start1=0
        start2=0
        end1=3
        end2=3
        counter=-1

        for k in range(len(board)):
            if k!=0:
                if k%3==0:
                    start1+=3
                    end1+=3
                    start2=0
                    end2=3
                else:
                    start2+=3
                    end2+=3
            
            for i in range(start1,end1):
                for j in range(start2,end2):
                    if board[i][j]!='.':
                        #checking row,column and box to make sure there is no other duplicate
                        row=r[i]
                        col=c[j]
                        box=b[k]
                        if row[board[i][j]]>1 or col[board[i][j]]>1 or box[board[i][j]]>1:
                            return False
        return True