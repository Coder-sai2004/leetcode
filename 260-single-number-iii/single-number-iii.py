from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x=Counter(nums)
        res=[]
        for i,j in x.items():
            if j==1:
                res.append(i)
        return res