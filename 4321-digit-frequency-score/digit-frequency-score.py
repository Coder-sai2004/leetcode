from collections import Counter
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s=str(n)
        res=[]
        ans=0
        for i in s:
            res.append(int(i))
        d=Counter(res)
        for val,freq in d.items():
            ans+=(val*freq)
        return ans