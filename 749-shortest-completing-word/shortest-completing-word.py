from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        x=''
        for i in licensePlate.lower():
            if i.isalpha():
                x+=i
        y=Counter(x)
        res=[]
        for word in words:
            z=Counter(word)
            c=0
            for i,j in y.items():
                if y[i]<=z[i]:
                    c+=1
            if c==len(y):
                res.append(word)
        m=float('inf')
        f=''
        for k in res:
            if len(k)<m:
                m=len(k)
                f=k
        return f

                    