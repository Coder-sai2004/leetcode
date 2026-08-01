class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        d={}
        s={}
        for w in s1:
            s[w]=s.get(w,0)+1

        k=len(s1)
        for i in range(k):
            d[s2[i]]=d.get(s2[i],0)+1

        b=True
        for key in s.keys():
            if key not in d or s[key]!=d[key]:
                b=False
        if b:
            return b

        for i in range(k,len(s2)):
            b=True
            if d[s2[i-k]]==1:
                del d[s2[i-k]]
            else:
                d[s2[i-k]]-=1
            
            d[s2[i]]=d.get(s2[i],0)+1

            for key in s.keys():
                if key not in d or s[key]!=d[key]:
                    b=False
            if b:
                return b
        return False