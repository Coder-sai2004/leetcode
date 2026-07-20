from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        x=Counter(nums)
        ans=0
        for val in x.values():
            ans+=(val*(val-1))//2
        return ans