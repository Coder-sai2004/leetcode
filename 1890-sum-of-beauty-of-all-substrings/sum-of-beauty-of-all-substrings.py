from collections import Counter 
class Solution:
    def beautySum(self, s: str) -> int:
        res=[]
        ans=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                res.append(s[i:j+1])
        for x in res:
                c=Counter(x)
                ans+=max(c.values())-min(c.values())
        return ans