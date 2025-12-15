class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        x=sorted(nums)
        return abs(sum(x[:k])-sum(x[-k:]))