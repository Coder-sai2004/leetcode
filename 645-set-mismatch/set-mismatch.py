from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res=[]
        x=Counter(nums)
        for i,j in x.items():
            if j>1:
                res.append(i)
        y=set(nums)
        m=len(nums)
        for k in range(1,m+1):
            if k not in y:
                res.append(k)
                break
        return res