class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        a=max(nums)
        nums.remove(a)
        b=max(nums)
        c=min(nums)
        return a+b-c