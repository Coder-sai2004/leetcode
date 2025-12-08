class Solution:
    def countTriples(self, n: int) -> int:
        c=0
        sq=[i**2 for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                s=sq[i]+sq[j]
                k=(int(s**0.5))
                if k<=n and sq[k]==s:
                    c+=1
        return c