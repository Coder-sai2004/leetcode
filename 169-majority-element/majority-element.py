from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x=Counter(nums)
        mx=max(x.values())
        for i,j in x.items():
            if j==mx:
                return i