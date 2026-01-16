class Solution:
    def sortVowels(self, s: str) -> str:
        vo={'a','e','i','o','u','A','E','I','O','U'}
        v=[]
        for i in s:
            if i in vo:
                v.append(i)
        x="".join(sorted(v))
        l=list(s)
        j=0
        for i in range(len(l)):
            if l[i] in vo and j<len(x):
                l[i]=x[j]
                j+=1
        return "".join(l)