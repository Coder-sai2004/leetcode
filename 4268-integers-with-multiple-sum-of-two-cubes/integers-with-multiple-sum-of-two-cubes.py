class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        x=[]
        k=1
        while k**3<n:
            x.append(k**3)
            k+=1
        d={}
        for i in range(len(x)-1):
            for j in range(i+1,len(x)):
                if x[i]+x[j]<=n:
                    d[x[i]+x[j]]=d.get(x[i]+x[j],0)+1
        ans=[]
        for i,j in d.items():
            if j>=2:
                ans.append(i)
        return sorted(ans)