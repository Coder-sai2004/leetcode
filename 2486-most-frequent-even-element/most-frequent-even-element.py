from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        x=[]
        for i in nums:
            if i%2==0:
                x.append(i)
        if len(x)==0:
            return -1
        y=Counter(x)
        m=max(y.values())
        r=[]
        for i,j in y.items():
            if j==m:
                r.append(i)
        return min(r)