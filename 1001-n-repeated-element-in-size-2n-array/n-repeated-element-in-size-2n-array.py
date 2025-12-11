from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        x=Counter(nums)
        s=set(nums)
        for i,j in x.items():
            if j*2==len(nums) and  j+1==len(s):
                return i