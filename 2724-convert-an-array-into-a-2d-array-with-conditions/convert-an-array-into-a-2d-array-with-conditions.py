from collections import Counter
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result=[]
        x=Counter(nums)
        high_freq=max(x.values())
        for _ in range(high_freq):
            a=[]
            for i in x.keys():
                if x[i]!=0:
                    a.append(i)
                    x[i]-=1
            result.append(a)
        return result