from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        x=Counter(nums)
        s=0
        for i,j in x.items():
            if j==1:
                s+=i
        return s