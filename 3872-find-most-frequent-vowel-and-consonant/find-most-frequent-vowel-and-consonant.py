from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        v={'a','e','i','o','u'}
        vow=[]
        con=[]
        a,b=0,0
        for i in s:
            if i in v:
                vow.append(i)
            else:
                con.append(i)
        x=Counter(vow)
        y=Counter(con)
        for j in x.values():
            if j>a:
                a=j
        for k in y.values():
            if k>b:
                b=k
        return a+b