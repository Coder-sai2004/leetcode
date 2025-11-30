from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=Counter(nums)
        for i in x.keys():
            if x[i]==1:
                return i