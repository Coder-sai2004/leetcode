class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        x=max(nums)
        return nums.index(x)