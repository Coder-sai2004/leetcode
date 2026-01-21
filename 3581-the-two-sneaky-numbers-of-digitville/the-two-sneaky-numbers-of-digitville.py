from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        x=Counter(nums)
        res=[]
        for i,j in x.items():
            if j==2:
                res.append(i)
        return res