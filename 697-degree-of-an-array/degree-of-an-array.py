from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        x=Counter(nums)
        m=max(x.values())
        r=[]
        for i,j in x.items():
            if j==m:
                r.append(i)
        s=50000
        for k in r:
            a=nums.index(k)
            b=len(nums)-1-nums[::-1].index(k)
            c=b-a+1
            if c<s:
                s=c
        return s