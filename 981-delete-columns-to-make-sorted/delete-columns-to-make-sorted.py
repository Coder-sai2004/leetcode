class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if len(strs[0])==1:
            if "".join(strs)!="".join(sorted(strs)):return 1
            else:return 0
        temp,count=[],0
        for i in strs:
            temp.append(list(i))
        column,row=len(temp),len(temp[0])
        res=[[0]*column for i in range(row)]
        for i in range(column):
            for j in range(row):
                res[j][i]=temp[i][j]
        for i in res:
            if i!=sorted(i):
                count+=1
        return count