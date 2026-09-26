class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        res=0
        d={}
        k=3

        if len(s) < k:
            return 0


        for i in range(k):
            d[s[i]]=d.get(s[i],0)+1
        if len(d.keys())==k:
            res+=1

        for i in range(k,len(s)):
            d[s[i]]=d.get(s[i],0)+1
            if d[s[i-k]]==1:
                del d[s[i-k]]
            else:
                d[s[i-k]]-=1

            if len(d.keys())==k:
                res+=1

        return res