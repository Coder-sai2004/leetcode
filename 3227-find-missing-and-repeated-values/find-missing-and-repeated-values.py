class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        d={}
        r=0
        m=0
        res=[]
        for x in grid:
            res.extend(x)
        s=set(res)
        for i in res:
            d[i]=d.get(i,0)+1
            if d[i]==2:
                r=i
                break
        for i in range(1,len(res)+1):
            if i not in s:
                m=i
                break
        return [r,m]