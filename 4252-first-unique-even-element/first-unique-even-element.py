from collections import Counter
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        x=Counter(nums)
        for i in nums:
            if i%2==0 and x[i]==1:
                return i
        return -1