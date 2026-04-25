class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for i in range(len(operations)):
            if operations[i]!='C' and operations[i]!='D' and operations[i]!='+':
                res.append(int(operations[i]))
            elif operations[i]=='C':
                y=res.pop()
            elif operations[i]=='D':
                z=2*res[-1]
                res.append(z)
            elif operations[i]=='+':
                k=res[-1]+res[-2]
                res.append(k)
        return sum(res)