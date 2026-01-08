class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        x=original
        s=set(nums)
        for i in nums:
            if x in s:
                x*=2
        return x