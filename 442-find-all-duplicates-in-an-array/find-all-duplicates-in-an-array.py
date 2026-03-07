from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        x=Counter(nums)
        for i,j in x.items():
            if j==2:
                res.append(i)
        return res