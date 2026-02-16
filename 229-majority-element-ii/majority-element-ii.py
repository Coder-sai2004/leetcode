from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        x=Counter(nums)
        t=len(nums)//3
        for i,j in x.items():
            if j>t:
                res.append(i)
        return res