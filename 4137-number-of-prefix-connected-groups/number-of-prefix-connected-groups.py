from collections import Counter
class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        c=0
        res=[]
        for w in words:
            t=w[:k]
            if len(t)==k:
                res.append(t)
        x=Counter(res)
        for j in x.values():
            if j>1:
                c+=1
        return c