class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        temp=[]
        c=0
        res=0
        r=[]
        for x in bank:
            if '1' in x:
                r.append(x)
        for y in r:
            c=y.count('1')
            temp.append(c)
        for i in range(len(temp)-1):
            res+=temp[i]*temp[i+1]
        return res