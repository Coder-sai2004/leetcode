class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        r=start
        res=[]
        a=start
        res.append(a)
        while len(res)<n:
            a+=2
            res.append(a)
        for i in range(1,len(res)):
            r^=res[i]
        return r